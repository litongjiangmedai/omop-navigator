
# OMOP-Navigator

**A modular, LLM-powered natural language interface for federated querying and cohort generation across OMOP CDM networks.**

---

## 🧠 Overview

**OMOP-Navigator** is an open-source tool that empowers clinical researchers to interact with OMOP CDM databases using natural language, without writing SQL. It supports **modular querying**, **ontology translation**, and **federated execution** across multiple sites or data nodes. The interface is powered by Large Language Models (LLMs), and designed for transparency, extensibility, and accessibility.

---

## 🎯 Key Features

- 🔍 **Natural Language Interface**: Ask clinical research questions like "Find patients with type 2 diabetes and recent HbA1c tests" — and receive results from OMOP CDM.
- 🧱 **Modular Design**: Each component (LLM prompt handling, database querying, ontology resolution, frontend UI) is decoupled for easy testing and extension.
- 🌐 **Federated Querying**: Click-to-execute multi-database querying across SQLite nodes (PostgreSQL supported in future).
- 🧠 **Prompt Engineering Toolkit**: Built-in templates for varied query intents — cohort definition, concept resolution, statistical comparison.
- 💡 **Example-Driven**: Includes curated examples to demonstrate clinical questions and system responses.

---

## 🧰 Project Structure

```
omop-navigator/
├── README.md
├── requirements.txt
├── app/
│   ├── main.py                  # Gradio interface
│   ├── prompt_templates.py     # Prompt templates for various intents
│   ├── query_generator.py      # LLM + prompt → SQL query generation
│   ├── omop_vocabulary.py      # OMOP concept + vocabulary mapping
│   ├── cohort_sql_builder.py   # Cohort query builder (ATLAS compatible)
│   ├── federated_query.py      # Federated execution logic (multi-DB)
│   ├── utils.py                # Utility functions
│   └── examples/
│       └── cases.json          # Sample queries and expected results
├── data/
│   ├── sample_omop_db.sqlite         # Sample OMOP database
│   ├── synthea_omop_full_demo.sqlite # Full-scale Synthea OMOP demo
│   └── concept_relationship.csv      # Concept mapping support
```

---

## 🚀 Quickstart

1. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the App**
   ```bash
   cd app
   python main.py
   ```

3. **Try Example Queries**
   - Open Gradio in your browser
   - Try: “Show patients with hypertension and a recent lab result.”

---

## 🔄 Switch Databases

You can switch between sample and full-scale OMOP databases by editing the `db_path` in `query_generator.py` or `federated_query.py`.

For example:
```python
db_path = "data/sample_omop_db.sqlite"  # ← small demo
# db_path = "data/synthea_omop_full_demo.sqlite"  # ← realistic use
```

---

## 🧪 Testing with Fake Patients

To populate synthetic data (for federated demo):
```bash
python populate_fake_patients.py  # Inserts 500 fake patients
```

---

## 📍 Use Cases

- Clinical research question translation
- Cohort identification (LLM → ATLAS-compatible SQL)
- Cross-site query federation
- Education & training for non-technical users

---

## 📌 Acknowledgement

This tool aligns with OHDSI’s values of openness, reproducibility, and collaboration, and is designed for OHDSI UK and global OMOP communities.

---

## 📫 Contact

Project lead: **Litong Jiang**  
Email: `litongjiangmedai@gmail.com`

---

*This project is part of the OHDSI-UK 2025 software demo initiative.*
