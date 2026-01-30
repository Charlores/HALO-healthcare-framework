# Day 10 – Safe AI Integration & Governance

## Purpose
HALO integrates AI to support clinical interpretation, not replace it.
AI outputs must be auditable, standardized, and separated from core clinical logic.

---

## Principles for Safe AI

1. **Separation of Concerns**
   - AI outputs are **advisory**, not authoritative
   - Risk scores and priority codes remain the source of truth

2. **Auditability**
   - Every AI output must be traceable to input data
   - No “black box” summaries without logging

3. **Standardized Output**
   - AI summaries should conform to the **CIS / FHIR mapping**
   - Example: `ClinicalImpression.summary`

4. **Human-in-the-loop**
   - Clinicians or trained personnel must review AI suggestions
   - AI aids, humans decide

---

## Example Mapping (AI → FHIR)

| HALO AI Output | FHIR Resource | Notes |
|----------------|--------------|------|
| ai_summary     | ClinicalImpression | Readable insight for clinicians |
| ai_alert       | Observation | Optional flag for follow-up |

---

## Governance Checklist

- [ ] Inputs validated and cleaned  
- [ ] Outputs standardized to HALO-CIS v1.0  
- [ ] AI logs retained for audit  
- [ ] Human review before any clinical action  
