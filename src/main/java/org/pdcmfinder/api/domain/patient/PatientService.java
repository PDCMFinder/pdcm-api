package org.pdcmfinder.api.domain.patient;

import lombok.AllArgsConstructor;
import org.springframework.stereotype.Service;

import java.util.Optional;

@Service
@AllArgsConstructor
public class PatientService {

    final PatientRepository patientRepository;

    Optional<Patient> findById(Integer id) {
        return patientRepository.findById(id.longValue());
    }

    Patient save(Patient patient) {
        return patientRepository.save(patient);
    }
}
