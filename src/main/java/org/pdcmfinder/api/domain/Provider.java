package org.pdcmfinder.api.domain;

import lombok.Data;

import javax.persistence.Entity;
import javax.persistence.Id;

@Data
@Entity
public class Provider {

    @Id
    Long id;

    String name;
    String url;
}
