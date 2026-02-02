AI can observe

AI can summarize

AI can suggest

AI cannot decide

AI cannot overwrite standardized data

AI cannot act without a human

          ┌──────────────┐
          │  Raw Patient │
          │   Data       │
          └───────┬──────┘
                  │
                  ▼
       ┌─────────────────────┐
       │  Data Cleaning &     │
       │  Validation Layer    │
       └────────┬────────────┘
                │
                ▼
       ┌─────────────────────┐
       │  Risk Calculation    │
       │   (Risk Scores)      │
       └────────┬────────────┘
                │
                ▼
       ┌─────────────────────┐
       │  Standardization     │
       │  Layer (HL7/FHIR)   │
       └────────┬────────────┘
                │
      ┌─────────┴─────────┐
      ▼                   ▼
┌───────────────┐   ┌───────────────┐
│ AI Advisory    │   │ Clinician /   │
│ Layer          │   │ Human Review  │
│ (ai_summary,   │   │               │
│ ai_alert)      │   │               │
└───────┬───────┘   └───────────────┘
        │
        ▼
   ┌───────────────┐
   │ Logged /      │
   │ Auditable     │
   │ Outputs       │
   └───────────────┘
