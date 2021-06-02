package org.pdcmfinder.api.domain.patient;

import lombok.Data;
import org.pdcmfinder.api.domain.PatientSnapshot;
import org.pdcmfinder.api.domain.Provider;

import javax.persistence.Entity;
import javax.persistence.Id;
import javax.persistence.ManyToOne;
import javax.persistence.OneToMany;
import java.util.Date;
import java.util.List;

@Data
@Entity
public class Patient {

    @Id
    Long id;
    String age;
    String initialDiagnosis;
    Date dateOfInitialDiagnosis;

    @ManyToOne
    Provider provider;

    @OneToMany
    List<PatientSnapshot> patientSnapshots;

}
