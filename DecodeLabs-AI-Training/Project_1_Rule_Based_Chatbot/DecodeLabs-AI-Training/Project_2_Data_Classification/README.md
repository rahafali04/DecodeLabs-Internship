# Project 2: Data Classification Using AI 
**DecodeLabs AI Training Kit - Predictive Phase** **Intern Name:** Rahaf Ali  
**Domain:** Software Engineering (Data Science & AI Concentration)

---

##  Executive Overview
[span_6](start_span)Moving away from the rule-based, deterministic constraints of Project 1, **Project 2** establishes the core foundation of **Supervised Machine Learning**[span_6](end_span). [span_7](start_span)[span_8](start_span)Under this predictive track, we construct a fully automated, end-to-end AI classification pipeline utilizing pure algorithmic logic without hand-coding conditional scripts[span_7](end_span)[span_8](end_span).

[span_9](start_span)[span_10](start_span)[span_11](start_span)The objective is to ingest the historical **Iris Benchmark Dataset**, scale its mathematical dimensions, map strategic decision boundaries, and categorize unseen biological samples into their respective classes with absolute precision[span_9](end_span)[span_10](end_span)[span_11](end_span).

---

## Architectural Paradigm (IPO Framework)
[span_12](start_span)The system architecture follows a clean **Input-Process-Output (IPO)** design pattern[span_12](end_span):

### 1. Input Phase 
* **[span_13](start_span)Dataset Ingestion:** Loading the canonical **Iris Benchmark** (150 balanced samples, 3 morphological classes: *Setosa, Versicolor, Virginica*, and 4 continuous spatial dimensions)[span_13](end_span).
* **[span_14](start_span)The Gatekeeper Rule (Feature Scaling):** Implementing `StandardScaler` to realign all 4 mathematical feature spaces to a uniform distribution where $\text{Mean} = 0$ and $\text{Variance} = 1$[span_14](end_span). [span_15](start_span)This neutralizes numerical scale bias, preventing distance-based distortion within the algorithm[span_15](end_span).

### 2. Process Phase 
* **[span_16](start_span)Structural Integrity (The Split):** Splitting the scaled dataset into a **80% Training Set** for pattern recognition and a **20% Test Set** for pure validation[span_16](end_span). [span_17](start_span)The data is randomly shuffled prior to splitting to eliminate any inherent **Order Bias**[span_17](end_span).
* **[span_18](start_span)[span_19](start_span)Engine Tuning (KNN Core):** Applying the **K-Nearest Neighbors (KNN)** algorithm[span_18](end_span)[span_19](end_span). The hyperparameter is tuned to $K = 5$ (an odd number to avoid majority voting stalemates). [span_20](start_span)As a **Lazy Learner**, the model stores the historical representation during training and derives the complex geometric logic dynamically during inference[span_20](end_span).

### 3. Output Phase 
* **[span_21](start_span)Diagnostic Tool (Confusion Matrix):** A spatial alignment matrix mapping absolute accurate classifications (diagonal axis) against any potential model misclassifications or cross-class confusion[span_21](end_span).
* **[span_22](start_span)System Validation (F1-Score):** Computing the Macro F1-Score as the absolute measure of evaluation quality and model generalization capabilities[span_22](end_span).

---

##  Repository Directory Structure
To maintain industrial-grade standardization, the file must be delivered inside the unified training repository exactly as follows:
```text
DecodeLabs-AI-Training/
├── Project_1_Rule_Based_Chatbot/
│   └── chatbot.py
└── Project_2_Data_Classification/
    ├── classification.py   <- Core AI Pipeline Script
    └── README.md           <- Technical Documentation