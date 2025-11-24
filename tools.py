from typing import Dict, Any

# ----------- BILINGUAL LEGAL AID TEMPLATE (ENGLISH + TAMIL) -----------

DOCUMENT_TEMPLATE = """
==========================
  JUSTICEMAP LEGAL AID FORM
 (WAGE NON-PAYMENT DISPUTE)
==========================

-------------------------------------------
SECTION 1: ENGLISH VERSION
-------------------------------------------

APPLICATION FOR FREE LEGAL AID – WAGE DISPUTE

Applicant Name: {applicant_name}
Father's Name: {father_name}
Residential Address: {address}

Employer Name (Respondent): {employer_name}
Date/Period of Incident: {incident_date}
Total Amount of Wages Unpaid: ₹{amount_claimed}

AFFIDAVIT:
I, {applicant_name}, hereby declare that the above information is true to the best of my knowledge.
I request free legal assistance for my wage-related grievance.

Date: ____________________
Signature: _______________

-------------------------------------------
SECTION 2: TAMIL VERSION (Simple Spoken Tamil)
-------------------------------------------

சம்பளம் கொடுக்காததற்கான சட்ட உதவி விண்ணப்பம்

விண்ணப்பதாரர் பெயர்: {applicant_name}
தந்தை பெயர்: {father_name}
வசிப்பிடம்: {address}

தொழிலடையாளர் பெயர்: {employer_name}
நிகழ்வு நடந்த நாள்/காலம்: {incident_date}
கொடுக்காமல் வைத்துள்ள சம்பளத் தொகை: ₹{amount_claimed}

உறுதிமொழி:
நான் {applicant_name}, மேலே கொடுத்துள்ள தகவல்கள் உண்மையானவை என்பதை உறுதிப்படுத்துகிறேன்.
எனக்கு சம்பளம் வழங்கப்படாத பிரச்சினைக்கு இலவச சட்ட உதவி தர வேண்டுகிறேன்.

தேதி: ____________________
கையொப்பம்: _______________
"""

# required facts
CRITICAL_FACTS = [
    "applicant_name",
    "father_name",
    "address",
    "employer_name",
    "incident_date",
    "amount_claimed"
]


# ----------- TOOL LOGIC -----------

def generate_justice_document(facts: Dict[str, str]) -> Dict[str, str]:
    missing = [k for k in CRITICAL_FACTS if k not in facts or not facts[k]]
    if missing:
        return {
            "status": "error",
            "error": f"Missing required facts: {', '.join(missing)}"
        }

    final_doc = DOCUMENT_TEMPLATE.format(**facts)

    return {
        "status": "success",
        "document": final_doc
    }
