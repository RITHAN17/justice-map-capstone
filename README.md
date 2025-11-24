# JusticeMap: The Vernacular AI Agent Converting Spoken Grievances into Actionable Legal Documents

**Track:** Agents for Good | **Core Concept:** Multi-Agent Legal Triage

---

## 1. 🎯 The Problem and Value Proposition

The Indian legal system is blocked by a **literacy and language barrier**. JusticeMap eliminates this by using a **Voice-First, Vernacular AI Agent** to automate the time-consuming administrative intake. This frees up human legal experts (PLVs/Lawyers) to focus on counsel, acting as an **Efficiency Multiplier** for the system.

## 2. 🏗️ Agent Architecture and Concepts Demonstrated

JusticeMap uses a Sequential Multi-Agent System to ensure high-fidelity data collection: 

| Agent / Component | Course Concept | Role in JusticeMap |
| :--- | :--- | :--- |
| **Root Agent** | **Sequential Agent** + **Sessions & Memory** | Orchestrates the entire flow (Validation → Drafting) and shares facts across agents. |
| **Triage Agent** | **LLM Agent (Gemini)** | Conducts the vernacular conversation and extracts facts (e.g., 'applicant_name'). |
| **Loop Agent** | **Loop Agent** | **Validates data quality.** Runs a loop to ensure ALL critical facts are collected before proceeding. |
| **Drafting Agent** | **A2A Protocol** + **Custom Tool** | Receives structured facts and executes the Custom Tool to finalize the document. |
| **`generate_nalza_draft`** | **Custom Tool** | Deterministically formats the verified facts into the final, legally structured template. |

## 3. 🚀 Setup and Run Instructions

1.  **Environment Setup:**
    ```bash
    # Create and activate environment
    python -m venv venv
    .\venv\Scripts\activate

    # Install dependencies
    pip install google-adk
    ```
2.  **API Key:** Set your key as an environment variable (crucial for running):
    ```powershell
    $env:GEMINI_API_KEY='YOUR_API_KEY_HERE'
    ```
3.  **Execution:** Run the test script:
    ```bash
    python run_justice_map.py
    ```

---

## 4. 📈 Expected Outcomes

* **System Efficiency:** Reduces manual PLV intake time by **50%+**.
* **Access Metric:** Increases the **Grievance-to-Application Conversion Rate** for vulnerable users.