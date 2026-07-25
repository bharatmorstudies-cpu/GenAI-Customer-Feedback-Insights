# GenAI-Powered Customer Feedback Insights Assistant

An end-to-end Generative AI pipeline designed to automate the ingestion, structure standardization, sentiment classification, and operational root-cause analysis of raw customer text reviews. This portfolio project demonstrates how to effectively combine traditional deterministic data pipelines (Python/Pandas) with advanced generative prompt engineering frameworks to generate stakeholder-ready business insights.

## 🚀 Project Features
*   **Automated Ingestion Pipeline:** Merges unstructured data across multiple platforms into a single unified workspace.
*   **Structured Prompt Engineering Assets:** Leverages role-assigned, system-constrained prompt architectures to enforce rigid structural markdown metrics.
*   **Fact vs. Inference Separation:** Implements systemic operational audits designed to isolate strict factual review evidence from inferred operational assumptions.
*   **Prioritized Action Roadmaps:** Translates textual data points straight into high-impact operational business initiatives.

## 📁 Repository Directory Architecture
```text
GenAI-Customer-Feedback-Insights/
│
├── amazon_cells_labelled.txt      # Raw Amazon product reviews (UCI Repository)
├── yelp_labelled.txt            # Raw Yelp restaurant service reviews (UCI Repository)
├── capstone_customer_feedback.csv # Processed, unified master database (2,000 records)
├── data_process.py               # Deterministic Python/Pandas transformation script
├── prompt_library.txt            # Engineered production-grade system prompts
└── README.md                     # Comprehensive project documentation
```

## 📊 Dataset Baseline Summary
The analysis engine operates on a data baseline sourced from the official **UCI Machine Learning Repository Sentiment Labelled Sentences**. 
*   **Total Volume:** 2,000 unique records processed.
*   **Distribution Matrix:** Split evenly across sources (1,000 Amazon product records / 1,000 Yelp service records).
*   **Sentiment Balance:** Perfectly balanced distribution model featuring exactly 50% positive metrics (`1`) and 50% negative metrics (`0`).

## ⚙️ Workflow Architecture Design
```text
[Raw Inputs: TXT/CSV] ──> [Python Data Cleaning Script]
                                     │
                                     ▼
                         [Prompt Library Engine]
                ┌────────────────────┼────────────────────┐
                ▼                    ▼                    ▼
        [Theme Extraction]   [Root-Cause Audit]   [Action Recommendations]
                │                    │                    │
                └────────────────────┼────────────────────┘
                                     ▼
                        [Human Verification Check]
                                     │
                                     ▼
                  [Polished Executive Insights Output]
```

## 🔍 Analytical Findings Matrix

### Extracted Theme Performance

| Theme Name | Source | Sentiment Direction | Brief Description | Evidence Snippet from Data |
| :--- | :--- | :--- | :--- | :--- |
| **International Compatibility** | Amazon | Negative | Product incompatible with U.S. power grid without extra accessories. | `"no way for me to plug it in here in the US unless I go by a converter."` |
| **Poor Battery Performance** | Amazon | Negative | Device hardware requires continuous tethering to a charging device. | `"Tied to charger for conversations lasting more than 45 minutes. MAJOR PROBLEMS!!"` |
| **Connection Integrity** | Amazon | Negative | Physical sizing anomalies result in unstable audio and power input. | `"I have to jiggle the plug to get it to line up right to get decent volume."` |
| **Food Safety & Cleanliness** | Yelp | Negative | Foreign component contamination presents direct customer safety risk. | `"A lady at the table next to us found a live green caterpillar in her salad."` |
| **Kitchen Assembly Gaps** | Yelp | Negative | Food quality misses standard benchmarks (stale textures, lack of seasoning). | `"The refried beans... were dried out and crusty and the food was bland."` |
| **Transaction Service Latency** | Yelp | Negative | Process bottleneck occurs during final customer payment touchpoint. | `"drawing out the time it took to bring the check."` |

### Strategic Root-Cause Auditing
*   **Observed Product Deficit:** Unreliable plug adapters and rapid battery depletion.
    *   *Hard Data Evidence:* Text logs referencing 45-minute limitations and manual cord adjustment constraints.
    *   *Inferred Operational Root Cause:* Missing hardware localization QA tests for specific targeted consumer markets.
*   **Observed Service Deficit:** Restaurant contamination elements and unseasoned dining items.
    *   *Hard Data Evidence:* Documented discovery of live insects in prepared salad items and dried-out textures.
    *   *Inferred Operational Root Cause:* Weak kitchen quality-assurance checkpoints and inadequate initial ingredient inspection procedures.

## 🛠️ Prioritized Action Framework
1.  **Immediate Kitchen Safety Audit (High Priority / Immediate):** Mandate a multi-stage line washing mechanism across cold-prep stations to eliminate safety threats.
2.  **Tableside POS Terminals (High Priority / Rapid Execution):** Deploy mobile transaction systems to completely eliminate payment handoff delays.
3.  **Supplier Quality Gates (Medium Priority / Continuous):** Enforce strict physical thickness compliance requirements on raw hardware component procurement lots.

## 🎓 Capstone Reflection Summary
*   **GenAI Strengths:** Accelerates structural cluster matching across thousands of lines of unstructured natural text files in seconds.
*   **Inherent Risks & Weaknesses:** Naturally over-extends assumptions (e.g., assuming structural understaffing) from single isolated text data inputs.
*   **Mitigation Strategy:** Enforced structured human-in-the-loop audit stages explicitly partitioning source facts from operational analytical assumptions.

---
**Author:** Bharat Mor
**Project Role:** Capstone AI Systems Engineer & Technical Analyst  
