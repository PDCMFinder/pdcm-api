FROM alpine:latest AS download-image

RUN apk add --no-cache wget

RUN wget https://github.com/PostgREST/postgrest/releases/download/v9.0.0/postgrest-v9.0.0-linux-static-x64.tar.xz && \
    tar --xz -xvf postgrest-v9.0.0-linux-static-x64.tar.xz && \
    mv postgrest /usr/local/bin/postgrest && \
    rm postgrest-v9.0.0-linux-static-x64.tar.xz

FROM nginx:latest

RUN rm -rf /usr/share/nginx/html/*
COPY nginx/default.conf /etc/nginx/conf.d/default.conf
COPY --from=download-image /usr/local/bin/postgrest /usr/local/bin/
ENTRYPOINT postgrest > postgrest.log & nginx -g 'daemon off;' 

EXPOSE 80