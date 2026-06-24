import streamlit as st
from google import genai
import random
import time
import re


client = genai.Client(
    api_key="AQ.Ab8RN6JvrjBd4x1F-K-TBepWVE7O6QPuonXEadcUw0qLXaeKnw"
)


st.set_page_config(
    page_title="AI Fact Battle",
    page_icon="🚀"
)


st.title("🚀 AI FACT BATTLE 🚀")
st.write("Find the fake fact!")


topics = [
    "Space",
    "Dinosaurs",
    "Technology",
    "Ocean",
    "Animals"
]


if "topic" not in st.session_state:
    st.session_state.topic = random.choice(topics)


if "facts" not in st.session_state:

    text = ""

    with st.spinner("🤖 Creating facts..."):

        for attempt in range(3):

            try:
                response = client.models.generate_content(
                    model="gemini-2.5flash",
                    contents=f"""
Create 3 amazing facts about {st.session_state.topic}.

One fact is fake.

Write:
1. fact
2. fact
3. fact

Then write:
ANSWER: number
"""
                )

                text = response.text

                if "ANSWER:" in text:
                    break

            except Exception:
                time.sleep(5)


    if not text:
        st.error("⚠️ Gemini is busy. Try again.")
        st.stop()


    # Get answer using regex (no split)
    answer_match = re.search(
        r"ANSWER:\s*(\d)",
        text
    )

    if answer_match:
        st.session_state.answer = answer_match.group(1)
    else:
        st.error("Could not find answer.")
        st.stop()


    # Remove answer line without split
    st.session_state.facts = re.sub(
        r"ANSWER:.*",
        "",
        text,
        flags=re.DOTALL
    )



st.subheader(
    f"🎯 Topic: {st.session_state.topic}"
)


st.write(
    st.session_state.facts
)


guess = st.radio(
    "Which fact is fake?",
    ["1", "2", "3"]
)


if st.button("✅ Check Answer"):

    if guess == st.session_state.answer:
        st.success(
            "🏆 Correct! You're a fact detective!"
        )
    else:
        st.error(
            f"❌ Wrong! Fact {st.session_state.answer} was fake."
        )


if st.button("🔄 New Game"):

    st.session_state.clear()
    st.rerun()