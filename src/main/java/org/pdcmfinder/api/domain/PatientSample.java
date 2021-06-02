package org.pdcmfinder.api.domain;

import lombok.Data;

import javax.persistence.Entity;
import javax.persistence.Id;

@Data
@Entity
public class PatientSample {

    @Id
    Integer id;
    String providerId;


//    Model model;
}
