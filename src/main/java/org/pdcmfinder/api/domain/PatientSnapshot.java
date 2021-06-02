package org.pdcmfinder.api.domain;

import lombok.Data;

import javax.persistence.Entity;
import javax.persistence.Id;
import javax.persistence.OneToOne;

@Data
@Entity
public class PatientSnapshot {

    @Id
    Long id;

    // Apply an order to the snapshots by sorting on index field
    String index;

    @OneToOne
    PatientSample patientSample;
}
