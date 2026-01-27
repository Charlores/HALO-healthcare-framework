import pandas as pd

data = {
    "patient_id": [1, 2, 3, 4, 5],
    "condition": ["Hypertension", "Diabetes", "Asthma", "Heart Disease", "Obesity"],
    "risk_score": [0.72, 0.81, 0.33, 0.90, 0.65]
}

df = pd.DataFrame(data)

def clinical_interpretation(row):
    if row["risk_score"] >= 0.8:
        return {
            "risk_tier": "HIGH",
            "priority_code": "CIS-H3",
            "summary": "High clinical risk. Immediate intervention recommended.",
            "interop_tag": "urgent-care"
        }
    elif row["risk_score"] >= 0.6:
        return {
            "risk_tier": "MODERATE",
            "priority_code": "CIS-M2",
            "summary": "Moderate clinical risk. Active monitoring required.",
            "interop_tag": "care-management"
        }
    else:
        return {
            "risk_tier": "LOW",
            "priority_code": "CIS-L1",
            "summary": "Low clinical risk. Routine follow-up appropriate.",
            "interop_tag": "preventive-care"
        }

interpretations = df.apply(clinical_interpretation, axis=1, result_type="expand")
df = pd.concat([df, interpretations], axis=1)

print("Standardized Clinical Interpretation Layer:")
print(df)
