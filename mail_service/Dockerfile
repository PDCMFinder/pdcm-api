FROM python:3.6.12-alpine

COPY requirements.txt /
RUN pip3 install -r /requirements.txt

COPY . /app
WORKDIR /app

EXPOSE 5000
RUN chmod +x gunicorn.sh

ENTRYPOINT ["./gunicorn.sh"]