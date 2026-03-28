import streamlit as st
from groq import Groq

# Initialize Groq client
client = Groq(api_key=st.secrets["GROQ_API_KEY"])

# 🔒 Stronger System Prompt (STRICT DOMAIN CONTROL)
SYSTEM_PROMPT = """
You are a STRICT travel planner assistant.

RULES:
- ONLY answer questions related to travel, tourism, trips, destinations, itineraries, food, culture, and travel tips.
- If the question is NOT related to travel, politely refuse.
- DO NOT answer general knowledge, coding, math, or unrelated topics.
- Keep responses concise and helpful.

If a query is not travel-related, respond with:
"I'm here to help with travel planning only. Please ask a travel-related question."
"""

# Initialize session state for chat history
if "history" not in st.session_state:
    st.session_state.history = []

st.title("🌍 AI Travel Planner")
st.write("Ask me anything about travel ✈️")

# Chat input
user_query = st.chat_input("e.g. Plan a 5-day trip to Bali under ₹50,000")

# 🧠 Simple keyword-based filter (extra safety layer)
def is_travel_related(query):
    travel_keywords = [
        "travel", "trip", "vacation", "holiday", "tour",
        "destination", "itinerary", "hotel", "flight",
        "places", "visit", "tourism", "budget",
        "food", "culture", "beach", "mountain"
    ]

    query = query.lower()
    return any(word in query for word in travel_keywords)

# LLM function
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


# Main chat logic
if user_query:

    # Display user message
    with st.chat_message("user"):
        st.write(user_query)

    # 🚫 Check if query is travel-related
    if not is_travel_related(user_query):
        reply = "❌ I'm here to help with travel planning only. Please ask a travel-related question."

    else:
        # Store user message
        st.session_state.history.append({"role": "user", "content": user_query})

        # Get LLM response
        reply = get_travel_advice(user_query)

        # Store assistant response
        st.session_state.history.append({"role": "assistant", "content": reply})

        # Limit history (important for performance)
        if len(st.session_state.history) > 20:
            st.session_state.history = st.session_state.history[-20:]

    # Display assistant response
    with st.chat_message("assistant"):
        st.write(reply)
