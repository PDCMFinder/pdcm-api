package org.pdcmfinder.api.domain;

import lombok.Data;

@Data
public class Model {
    Integer id;
    String providerId;
    OntologyTerm histology;
}
