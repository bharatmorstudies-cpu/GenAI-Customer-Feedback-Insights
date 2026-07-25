# 📊 COURSE CAPSTONE: GENAI CUSTOMER FEEDBACK ASSISTANT
**Project Portfolio Deck**  
**Author:** Bharat Mor  
**Role:** Capstone AI Systems Engineer & Technical Analyst  
**Repository Link:** https://github.com/bharatmorstudies-cpu/GenAI-Customer-Feedback-Insights.git

---

## 🛝 Slide 1: Project Title & Business Problem Context

### Core Focus
*   **Project Title:** GenAI-Powered Customer Feedback Insights Assistant
*   **The Business Problem:** Manual review processing introduces severe operational bottlenecks, customer response delays, and heavy inconsistencies in tracking feedback trends.
*   **Strategic Mission:** Build an automated system pipeline to parse unstructured text inputs and convert them into immediate, structured operational data.
*   **Expected Business Value:** Reduce administrative decision cycles from days to seconds, allowing operations teams to address critical service vulnerabilities immediately.

---

## 🛝 Slide 2: Ingestion Scope & Dataset Baseline

### Data Metrics Summary
*   **Data Provenance:** Sourced from the official **UCI Machine Learning Repository** (Sentiment Labelled Sentences).
*   **Total Volumes Parsed:** Exactly 2,000 unique customer data records.
*   **Platform Segmentation:** Balanced 50/50 split across distinct operational areas:
    *   `1,000` rows of Amazon physical product reviews.
    *   `1,000` rows of Yelp restaurant service reviews.
*   **Label Configuration:** 50% Positive sentiment entries (`1`) and 50% Negative sentiment entries (`0`).
*   **Pre-Processing Asset:** Consolidated using a custom deterministic Python pipeline file (`data_process.py`) into a standardized output layer (`capstone_customer_feedback.csv`).

---

## 🛝 Slide 3: GenAI Ingestion Workflow Architecture

### System Execution Mapping
```text
[Raw Unstructured Inputs] ➔ (amazon_cells_labelled.txt / yelp_labelled.txt)
            │
            ▼
[Data Preprocessing Layer] ➔ (data_process.py script standardizes CSV schemas)
            │
            ▼
[Prompt Engineering Engine] ➔ (Executes 6 structured role-assigned templates)
            │
            ▼
[Human-in-the-Loop Audit] ➔ (Strictly filters hard data facts from assumptions)
            │
            ▼
[Executive Delivery Output] ➔ (Live markdown tables / automated action roadmaps)
```

---

## 🛝 Slide 4: Reusable Prompt Engineering Strategy

### Production System Architecture
To maximize structural integrity, the system bypasses open-ended prompts in favor of an **engineered production template library** featuring explicit persona assignments and strict structural output constraints.

### Core Implementation Examples (From `prompt_library.txt`)
1.  **The Extraction Persona:** Enforces the role of *Lead Customer Experience Analyst* to output rigid, data-anchored markdown summary matrices.
2.  **The Auditor Persona:** Establishes an *Operations and Business Auditor* frame to force a strict boundary layer separating literal explicit evidence from inferred assumptions.
3.  **The Copywriter Persona:** Applies a *Chief of Staff* format to clean technical summaries into crisp, professional business executive overviews.

---

## 🛝 Slide 5: Analytical Findings Summary Matrix

### Extracted Theme Performance (Automated Metric Output)

| Theme Name | Source | Sentiment Direction | Brief Description | Evidence Snippet from Data |
| :--- | :--- | :--- | :--- | :--- |
| **International Compatibility** | Amazon | Negative | Product incompatible with U.S. power grid without extra accessories. | `"no way for me to plug it in here in the US unless I go by a converter."` |
| **Poor Battery Performance** | Amazon | Negative | Device hardware requires continuous tethering to a charging device. | `"Tied to charger for conversations lasting more than 45 minutes. MAJOR PROBLEMS!!"` |
| **Connection Integrity** | Amazon | Negative | Physical sizing anomalies result in unstable audio and power input. | `"I have to jiggle the plug to get it to line up right to get decent volume."` |
| **Food Safety & Cleanliness** | Yelp | Negative | Foreign component contamination presents direct customer safety risk. | `"A lady at the table next to us found a live green caterpillar in her salad."` |
| **Kitchen Assembly Gaps** | Yelp | Negative | Food quality misses standard benchmarks (stale textures, lack of seasoning). | `"The refried beans... were dried out and crusty and the food was bland."` |
| **Transaction Service Latency** | Yelp | Negative | Process bottleneck occurs during final customer payment touchpoint. | `"drawing out the time it took to bring the check."` |

---

## 🛝 Slide 6: Operational Root-Cause Analysis

### Audit Disconnect Metrics
A key step in our pipeline is separating verified text entries from secondary business assumptions to minimize model hallucinations.

*   **1. Observed Hardware Deficit:** Poor charging connections and sudden battery life termination.
    *   *Explicit Evidence from Data:* Texts explicitly detailing a 45-minute battery capacity constraint and loose plug designs.
    *   *Inferred Operational Root Cause:* Insufficient pre-launch hardware testing and a lack of localization QA for target regional consumer markets.
*   **2. Observed Dining Service Deficit:** Extreme food-contamination event and stale food presentation.
    *   *Explicit Evidence from Data:* Verified discovery of live insects inside served salad selections.
    *   *Inferred Operational Root Cause:* Broken supplier washing protocols and weak internal kitchen checkpoint controls.

---

## 🛝 Slide 7: Prioritized Action Framework

### Strategic Execution Roadmap
Action plans are systematically prioritized by balancing expected customer retention impact against immediate operational complexity.

1.  **Immediate Kitchen Washing Restructure (High Priority / Immediate Setup)**
    *   *Action:* Launch multi-phase sink prep stations to catch contaminants and eliminate inventory safety vulnerabilities.
2.  **Deploy Mobile Tableside POS Checkouts (High Priority / Rapid Execution)**
    *   *Action:* Introduce wireless checkout tablets to remove invoice handoff delays and optimize dining table cycles.
3.  **Enforce Sourcing Compliance Controls (Medium Priority / Continuous Evaluation)**
    *   *Action:* Establish strict physical dimension bounds on incoming manufacturing shipments to eliminate loose connector pins.

---

## 🛝 Slide 8: Technical Limitations & Validation

### Critical Project Evaluation
*   **GenAI Superpowers:** Replaces hundreds of hours of manual logging by organizing unstructured strings into analytical clusters within seconds.
*   **Inherent Risk Profiles:** Generative intelligence naturally leans toward *over-extending inferences* (e.g., attributing a slow check payout to systemic staff shortfalls when the review text only mentions a simple delay).
*   **System Validation Strategy:** We implemented a strict **Human-in-the-Loop** random sampling framework. Every theme generated by the AI engine must be checked against original data spreadsheet rows to ensure absolute accuracy.
*   **Future Scale Enhancements:** Transition from static local file uploads to live webhooks and automated real-time analytics streaming.
