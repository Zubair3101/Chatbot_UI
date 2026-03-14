import streamlit as st
from groq import Groq
import os

# Get API key from Streamlit secrets
client = Groq(api_key=st.secrets["GROQ_API_KEY"])

SYSTEM_PROMPT = """
You are an expert travel planner assistant. Help users plan their trips by providing:
- Destination recommendations based on preferences
- Suggested itineraries with day-by-day activities
- Budget estimates and money-saving tips
- Best time to visit recommendations
- Local food and cultural experiences
- Practical travel tips and safety advice
Be concise but informative. Ask clarifying questions when needed.
"""

# Initialize conversation history
if "history" not in st.session_state:
    st.session_state.history = []

st.title("🌍 AI Travel Planner")
st.write("Plan your dream trip with AI!")

user_query = st.chat_input("Where do you want to travel?")

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


if user_query:

    st.session_state.history.append({"role": "user", "content": user_query})

    with st.chat_message("user"):
        st.write(user_query)

    with st.chat_message("assistant"):
        reply = get_travel_advice(user_query)
        st.write(reply)

    st.session_state.history.append({"role": "assistant", "content": reply})