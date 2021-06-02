package org.pdcmfinder.api.domain.patient;

import lombok.AllArgsConstructor;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController

@RequestMapping("/api/patients")
@AllArgsConstructor
public class PatientController {

    final PatientService patientService;

    @GetMapping("/$id")
    Patient getPatientById(Integer id) {

        return patientService.findById(id).orElse(null);
    }

    @PutMapping("/$patient")
    Patient addPatient(Patient patient) {
        return patientService.save(patient);
    }

}
