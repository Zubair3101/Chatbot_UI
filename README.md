# 🌍 AI Travel Planner

An AI-powered travel planner web app built using Streamlit and Groq LLM.  
This application helps users plan trips by generating personalized itineraries, travel tips, and recommendations.

---

## 🚀 Features

- 🗺️ Personalized travel recommendations
- 📅 Day-wise itinerary generation
- 💰 Budget estimation tips
- 🍜 Local food suggestions
- 🌤️ Best time to visit guidance
- 💬 Chat-based interactive UI
- 🧠 Context-aware conversation (remembers previous queries)

---

## 🛠️ Tech Stack

- Frontend/UI: Streamlit
- LLM: Groq (LLaMA 3.1 8B)
- Language: Python

---

## 📂 Project Structure

```
├── app.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/travel-planner.git
cd travel-planner
```

---

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 3. Add API Key

Create a `.streamlit/secrets.toml` file:

```toml
GROQ_API_KEY = "your_groq_api_key_here"
```

---

### 4. Run the App

```bash
streamlit run app.py
```

---

## 🌐 Deployment

This app can be deployed using Streamlit Cloud:

1. Push code to GitHub  
2. Connect repo on Streamlit Cloud  
3. Add secrets (GROQ_API_KEY)  
4. Deploy 🚀  

---

## 🧠 How It Works

1. User enters a travel query  
2. Query is sent to Groq LLM  
3. LLM generates travel plan using system prompt  
4. Conversation history is maintained using session state  
5. Response is displayed in chat UI  

---

## 💡 Example Queries

- "Plan a 5-day trip to Paris"
- "Best places to visit in Japan"
- "Budget trip to Goa"
- "What to do in Dubai for 3 days?"

---

## 📌 Future Improvements

- Weather API integration  
- Hotel recommendations  
- Flight search  
- Map integration  
- Agent-based tool usage  

---

## 👨‍💻 Author

Zubair Ansari

---
