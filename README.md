# 🌍 FLOK — Food Loss on Chain  
**AI × Blockchain system for food waste redistribution**

FLOK (Food Loss on Chain) is a **Streamlit-based data visualization and blockchain monitoring system** that tracks near-expiry food batches and redistributes them efficiently.  
The goal is to connect convenience stores, food banks, and local receivers to ensure **traceability, sustainability, and reduced waste** through data-driven insights.

---

## ✨ Features
- 🔗 **Blockchain ledger** for immutable redistribution tracking  
- 📊 **Live monitoring dashboard** for temperature, humidity, and expiry  
- 🧠 **AI-ready architecture** for predictive rerouting and optimization  
- 🌐 **Streamlit-based interactive UI** with dark theme visualization  
- 🧾 **Transparent logs** stored in `blockchain_log.json`  

---

## 🧱 Tech Stack
| Component | Technology |
|------------|-------------|
| **Frontend / Dashboard** | Streamlit |
| **Backend Logic** | Python |
| **Data Handling** | Pandas, JSON |
| **Blockchain Module** | Custom ledger (`flok_blockchain.py`) |
| **Visualization** | Plotly / Streamlit Charts |

---

## 🚀 Quickstart

```bash
# 1️⃣ Clone the repository
git clone https://github.com/<your-username>/FLOK.git
cd FLOK

# 2️⃣ (optional) create a virtual environment
python3 -m venv venv
source venv/bin/activate

# 3️⃣ Install dependencies
pip install -r requirements.txt

# 4️⃣ Run the Streamlit app
streamlit run app.py --server.port 8501
````

Then open your browser at → **[http://localhost:8501](http://localhost:8501)**

---

## 📊 Screenshot (Real Demo)

**Live Food Batch Monitoring & Blockchain Log Dashboard**

![FLOK Dashboard](data/flok_dashboard.png)

> *Figure: Real working interface showing live food batches, blockchain ledger, and reroute analytics.*

---

## 🧩 File Structure

```
FLOK/
├── app.py                 # Main Streamlit app
├── flok_blockchain.py     # Blockchain ledger logic
├── blockchain_log.json    # Local ledger data
├── logic/                 # Matching and rule-based analysis modules
├── data/                  # Screenshot and sample datasets
│   └── flok_dashboard.png
├── requirements.txt
├── .gitignore
└── venv/                  # Local environment (ignored)
```

---

## 🧠 Roadmap

* [ ] Integrate ML model for expiry & demand prediction
* [ ] Add PostgreSQL / Firebase backend support
* [ ] Build FastAPI-based REST microservice layer
* [ ] Deploy on Streamlit Cloud or Heroku
* [ ] Add real-time LINE/Slack alert system

---

## 👨‍💻 Author

**Adwait Sanjay Varekar**
Musashino University — Department of Data Science
📧 [cadadwait@gmail.com](mailto:cadadwait@gmail.com)
🌐 [github.com/ADWAITsv1](https://github.com/ADWAITsv1)

---

## 📜 License

This project is licensed under the **MIT License** — see [LICENSE](./LICENSE).

---

## 🏷️ Repository Metadata

**Description:**
AI × Blockchain dashboard for sustainable food waste redistribution.
Developed with Python and Streamlit, integrating data analytics and blockchain-style logging.

**Keywords:**
`streamlit` • `blockchain` • `ai` • `sustainability` • `data-science` • `food-waste` • `smart-city` • `fastapi-ready`

```

---


