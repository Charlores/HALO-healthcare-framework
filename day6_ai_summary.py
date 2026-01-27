import pandas as pd

# Sample patient data (from previous days)
data = {
    "patient_id": [1, 2, 3, 4, 5],
    "age": [45, 62, 29, 54, 37],
    "condition": ["Hypertension", "Diabetes", "Asthma", "Heart Disease", "Obesity"],
    "risk_score": [0.72, 0.81, 0.33, 0.90, 0.65]
}

df = pd.DataFrame(data)

def generate_summary(row):
    if row["risk_score"] >= 0.8:
        return "High risk patient. Immediate clinical attention recommended."
    elif row["risk_score"] >= 0.6:
        return "Moderate risk patient. Monitor and manage condition closely."
    else:
        return "Low risk patient. Routine follow-up suggested."

df["ai_summary"] = df.apply(generate_summary, axis=1)

print("AI-Generated Patient Summaries:")
print(df[["patient_id", "condition", "risk_score", "ai_summary"]])
