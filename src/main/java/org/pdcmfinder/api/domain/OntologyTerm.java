package org.pdcmfinder.api.domain;

import lombok.Data;

@Data
public class OntologyTerm {
    String id;
    String term;

    public String getOntology() {
        if (id.contains(":")) {
            return id.split(":")[0];
        } else if (id.contains("_")) {
            return id.split("_")[0];
        }
        return id;
    }
}
