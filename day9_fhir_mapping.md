# Day 9 – FHIR Conceptual Mapping

## What is FHIR?
FHIR (Fast Healthcare Interoperability Resources) is a healthcare data standard.
It defines how healthcare information is structured, shared, and understood
across different systems.

FHIR is not AI.
FHIR is not a database.
FHIR is a common language.

---

## Why Interoperability Fails in Healthcare
Most healthcare systems:
- Store data in different formats
- Use different names for the same concept
- Cannot easily exchange meaning

FHIR solves this by defining shared structures called "resources".

---

## Core FHIR Resources Relevant to HALO

### Patient
Represents a real human receiving care.
HALO uses patient_id, age, and demographics which map naturally to Patient.

### Observation
Represents measured or calculated data.
Risk scores and vitals belong here.

### Condition
Represents diagnosed or reported conditions.
Examples: Diabetes, Hypertension, Asthma.

### ClinicalImpression
Represents a clinician’s or system’s interpretation.
HALO’s AI-generated summaries belong here.

---

## HALO → FHIR Mapping

| HALO Concept | FHIR Resource | Reason |
|-------------|--------------|--------|
| patient_id | Patient | Identity |
| age | Patient | Demographics |
| condition | Condition | Diagnosed state |
| risk_score | Observation | Computed metric |
| ai_summary |_
