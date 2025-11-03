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
