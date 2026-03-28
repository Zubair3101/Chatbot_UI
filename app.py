import streamlit as st
from groq import Groq

# Initialize Groq client
client = Groq(api_key=st.secrets["GROQ_API_KEY"])

# System Prompt
SYSTEM_PROMPT = """
You are a STRICT travel planner assistant.

RULES:
- ONLY answer travel-related questions.
- If not travel-related, politely refuse.
- Be concise and helpful.

If not travel-related, say:
"I'm here to help with travel planning only. Please ask a travel-related question."
"""

# Initialize session state
if "history" not in st.session_state:
    st.session_state.history = []

st.title("🌍 AI Travel Planner")
st.write("Ask me anything about travel ✈️")

# ✅ STEP 1: DISPLAY CHAT HISTORY FIRST
for msg in st.session_state.history:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# Chat input
user_query = st.chat_input("e.g. Plan a 5-day trip to Bali under ₹50,000")

# Keyword filter
def is_travel_related(query):
    keywords = [
        "travel", "trip", "vacation", "holiday", "tour",
        "destination", "itinerary", "hotel", "flight",
        "visit", "tourism", "budget", "food", "culture"
    ]
    query = query.lower()
    return any(word in query for word in keywords)

# LLM call
def get_travel_advice(user_query):
    messages = [{"role": "system", "content": SYSTEM_PROMPT}]
    messages.extend(st.session_state.history)
    messages.append({"role": "user", "content": user_query})

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=messages,
        temperature=0.7,
        max_tokens=1024
    )

    return response.choices[0].message.content

# Main logic
if user_query:

    # Show user message instantly
    with st.chat_message("user"):
        st.write(user_query)

    # Store user message
    st.session_state.history.append({"role": "user", "content": user_query})

    # Check domain
    if not is_travel_related(user_query):
        reply = "❌ I'm here to help with travel planning only. Please ask a travel-related question."
    else:
        reply = get_travel_advice(user_query)

    # Show assistant response
    with st.chat_message("assistant"):
        st.write(reply)

    # Store assistant response
    st.session_state.history.append({"role": "assistant", "content": reply})

    # Limit history
    if len(st.session_state.history) > 20:
        st.session_state.history = st.session_state.history[-20:]
