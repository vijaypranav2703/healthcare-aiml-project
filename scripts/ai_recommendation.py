def generate_recommendation(age, condition, medication, predicted_bill):
    return f"""
AI Doctor Recommendation
------------------------
Patient Age: {age}
Medical Condition: {condition}
Medication: {medication}
Predicted Billing Amount: ${predicted_bill:,.2f}

Recommendation:
The predicted billing amount suggests moderate care intensity.
Advise the patient to continue medication, maintain lifestyle habits,
and schedule a follow-up check within 2–4 weeks.

If symptoms worsen — such as fatigue, breathing issues,
irregular blood sugar levels, or unexpected side effects —
seek immediate clinical attention.

Lifestyle guidance:
- Maintain a balanced diet
- Increase physical activity gradually
- Ensure medication adherence
"""

if __name__ == "__main__":
    print(generate_recommendation(57, "Diabetes", "Aspirin", 29403.14))
