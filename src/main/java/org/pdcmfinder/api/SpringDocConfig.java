package org.pdcmfinder.api;

import io.swagger.v3.oas.models.ExternalDocumentation;
import io.swagger.v3.oas.models.OpenAPI;
import io.swagger.v3.oas.models.info.Info;
import io.swagger.v3.oas.models.info.License;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Configuration
public class SpringDocConfig {


    @Bean
    public OpenAPI pdcmApiConfig() {
        return new OpenAPI()
                .info(new Info().title("Patient Derived Cancer Models API")
                        .description("This serivce exposes domain object, service, and web component APIs from the PDCM resource")
                        .version("v0.0.1")
                        .license(new License().name("Apache 2.0").url("http://springdoc.org")))
                .externalDocs(new ExternalDocumentation()
                        .description("PDCM API resource Documentation")
                        .url("https://github.com/PDXFinder/pdcm-api/wiki"));
    }

}
