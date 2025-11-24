# agent.py

from google.genai import Client
from tools import CRITICAL_FACTS, generate_justice_document
import json
import re


class JusticeMapAgent:

    def __init__(self, api_key: str, model="gemini-2.0-flash"):
        self.client = Client(api_key=api_key)
        self.model = model
        self.facts = {key: "" for key in CRITICAL_FACTS}
        self.stage = "collecting"

    # ------------------------------------------------------------
    # CLEANUP FUNCTION FOR ALL EXTRACTED FACTS
    # ------------------------------------------------------------
    def clean_value(self, value: str) -> str:
        if not value:
            return value

        # Remove garbage prefixes
        value = re.sub(r"\b(my|name is|i am|i'm|s name is)\b", "", value, flags=re.I)
        value = value.strip(" .,")

        # Proper title case for names
        if len(value.split()) <= 4:
            value = value.title()

        return value.strip()

    # ------------------------------------------------------------
    # REGEX-FIRST EXTRACTOR + LLM FALLBACK
    # ------------------------------------------------------------
    def extract_fact(self, user_message: str, target_fact: str) -> str:
        text = user_message.lower()

        patterns = {
            "applicant_name": r"(?:my name is|i am|i'm)\s+([A-Za-z ]+)",
            "father_name": r"(?:father|dad|appa|my father's name is)\s+([A-Za-z ]+)",
            "address": r"(?:live at|located at|address is|reside at)\s+(.+)",
            "employer_name": r"(?:boss|employer|manager|my boss is)\s+([A-Za-z\. ]+)",
            "incident_date": r"(?:happened|occurred|between|from|on|during)\s+(.+)",
            "amount_claimed": r"(?:money owed is|total money owed is|claim amount is|amount is|rupees|₹)\s*([0-9A-Za-z ]+)"
        }

        # Try REGEX first
        if target_fact in patterns:
            match = re.search(patterns[target_fact], text)
            if match:
                value = match.group(1).strip().rstrip(".")
                return self.clean_value(value)

        # ---------------------------
        # LLM fallback if regex fails
        # ---------------------------
        prompt = f"""
Extract ONLY the value for: {target_fact}
User message: "{user_message}"

Rules:
- Return ONLY the value
- No explanations
- If not found return "__NONE__"
"""

        resp = self.client.models.generate_content(
            model=self.model,
            contents=prompt
        )

        raw = resp.text.strip()

        if not raw or "__NONE__" in raw:
            return "__NONE__"

        return self.clean_value(raw)

    # ------------------------------------------------------------
    # NEXT MISSING FACT
    # ------------------------------------------------------------
    def next_missing_fact(self):
        for fact in CRITICAL_FACTS:
            if not self.facts[fact]:
                return fact
        return None

    # ------------------------------------------------------------
    # MAIN CONVERSATION LOGIC
    # ------------------------------------------------------------
    def handle_message(self, user_message: str) -> str:

        # ---------- FACT COLLECTION ----------
        if self.stage == "collecting":

            missing = self.next_missing_fact()

            if missing is None:
                self.stage = "drafting"
                return "All required details are collected. I am now preparing your bilingual legal document."

            value = self.extract_fact(user_message, missing)

            if value == "__NONE__":
                return f"I couldn't find **{missing}** in your message. Please provide ONLY your {missing}."

            self.facts[missing] = value

            next_missing = self.next_missing_fact()
            if next_missing:
                return f"Got it. Next, please tell me: **{next_missing}**"
            else:
                self.stage = "drafting"
                return "All required details are collected. Preparing your document..."

        # ---------- DOCUMENT GENERATION ----------
        elif self.stage == "drafting":
            result = generate_justice_document(self.facts)

            if result["status"] == "success":
                return "Here is your bilingual legal aid application:\n\n" + result["document"]
            else:
                return "Error generating document: " + result["error"]
