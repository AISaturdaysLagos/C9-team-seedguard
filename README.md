# 🌱 SeedGuard AI
**Mapping the GMO Narrative Landscape for True Agricultural Empowerment & Sovereignty**

![Seed_image](./187.jpg)

---

## 📘 Overview
---
SeedGuard AI is a Natural Language Processing (NLP) and Machine Learning (ML) project that explores the global conversation surrounding **genetically modified organisms (GMOs)** and **seed sovereignty** across Africa. By collecting thousands of publicly available discussions from **X App (Twitter)** and **Reddit**, our system identifies, analyzes, and maps emerging narratives, emotional tones, and stakeholder perspectives shaping Africa’s agricultural future.

---

## 🎯 Objectives
---
- Collect and preprocess text data from online platforms such as X (Twitter) and Reddit using targeted keywords (e.g., *African seed sovereignty*, *agroecology*, *genetically modified maize*, etc.).
- Apply advanced NLP models (DistilBERT, BERTopic) to automatically **cluster**, **categorize**, and **analyze** public opinions.
- Map connected topics, sentiment shifts, and emotional distributions across African regions.
- Support evidence-based discussions and policy decisions on agricultural sovereignty and biotechnology.

---

## 🧩 Project Workflow
---

### **1️⃣ Data Collection & Preprocessing**
- Tools: `snscrape`, `PRAW`, `BeautifulSoup`, `requests`
- Cleaning: Remove stopwords, URLs, emojis, duplicates.
- Languages: English (focus), others optional via translation models.
- Output: Structured CSV/JSON for modeling.

### **2️⃣ NLP Modeling & Clustering**
- Embedding Model: `DistilBERT` via `sentence-transformers`
- Topic Modeling: `BERTopic` with `UMAP` + `HDBSCAN`
- Sentiment Analysis: `VADER`, `TextBlob`
- Classification: Predict stakeholder groups (e.g., farmers, companies, NGOs).

### **3️⃣ Visualization & Insights**

- Tools: `Plotly`, `Seaborn`, `Matplotlib`, `Folium`
- Dashboards: Topic frequency charts, sentiment maps, stakeholder influence graphs.
- Platforms: Streamlit or Dash for deployment.

---

## 🏗️ Folder Structure
---
```
C9-team-seedguard/
│
├── data/
│   ├── raw/                # Unprocessed data (excluded from Git)
│   
│   
│
├── notebooks/              # Jupyter notebooks for exploration
│
│   ├── preprocessed.ipynb
│   ├── classification.ipynb
│   ├── topic_modeling.ipynb
│   ├── sentiment_analysis.ipynb
│   └── visualization.ipynb
│
├── results/                # Generated insights, plots, figures
├── requirements_data.txt   # Dependencies for data & visualization
├── requirements_model.txt  # Dependencies for model training
├── .gitignore
└── README.md
```

---

## ⚙️ Installation & Setup
---

### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/AISaturdaysLagos/C9-team-seedguard.git
cd C9-team-seedguard
```

### **2️⃣ Create a Virtual Environment**
```bash
python -m venv venv
venv\Scripts\activate   # For Windows
# or
source venv/bin/activate  # For Mac/Linux
```

### **3️⃣ Install Dependencies**
For data processing only:
```bash
pip install -r requirements_data.txt
```
For model training:
```bash
pip install -r requirements_model.txt
```

### **4️⃣ Setup API Keys**
Create a `.env` file and add your credentials:
```
TWITTER_BEARER_TOKEN=your_twitter_api_key
REDDIT_CLIENT_ID=your_reddit_client_id
REDDIT_SECRET=your_reddit_secret
```

---

## 🧠 Key Technologies
---
- **Data Collection:** `snscrape`, `PRAW`, `BeautifulSoup`
- **NLP & Modeling:** `DistilBERT`, `BERTopic`, `Transformers`, `HDBSCAN`, `UMAP`
- **Visualization:** `Plotly`, `Folium`, `Seaborn`, `Dash`, `Streamlit`
- **Languages:** Python, Jupyter Notebook

---

## 📊 Expected Deliverables
---
- Clean dataset of GMO-related discussions across Africa.
- NLP model capable of identifying key narratives and stakeholder categories.
- Interactive visualization dashboard for exploring topic and sentiment trends.
- Technical report summarizing findings, insights, and recommendations.

---

## 👥 Team Roles
---
| Role | Name | Responsibilities |
|------|------|------------------|
| **Tech Lead** | *Ismail O. Daud* | Project structure, workflow, integration, model supervision |
| **Data Engineers** | *Agoro Zeenat* | Data collection, cleaning, and preprocessing |
| **ML Engineers** |*Elijah Aremu*, *Tijani O.*  | Topic modeling, embeddings, classification |
| **Visualization Analysts** |*All team members*  | Charts, dashboards, storytelling |
| **Documentation Lead** | *Ismail O. Daud* | Reports, README, presentation materials |

---

## 🚀 Future Extensions
---
- Add multilingual sentiment analysis for Francophone and Arabic-speaking Africa.
- Integrate real-time social media tracking APIs.
- Develop a Streamlit dashboard with live trend updates.
- Deploy models to Hugging Face or Google Cloud for public access.

---

## 📜 License
---
This project is developed under the **AI Saturdays Lagos Cohort 9** program for machine learning and research purpose.

---

## 💬 Contact
For inquiries or collaborations:
- 📧 **ai6lagos@gmail.com**
