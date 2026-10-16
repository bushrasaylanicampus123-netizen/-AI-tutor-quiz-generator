import streamlit as st
import random

st.set_page_config(
    page_title="AI Tutor & Quiz Generator",
    page_icon="📚",
    layout="centered"
)

st.title("📚 AI Tutor & Quiz Generator")
st.write("Learn topics and test your knowledge!")

st.divider()

st.header("🎓 AI Tutor")

topic = st.text_input("Enter a topic:", placeholder="Example: Artificial Intelligence")

if st.button("Explain Topic"):
    if topic.strip():
        st.subheader("Topic: " + topic)
        st.write(
            f"{topic} is a topic you can learn step by step. "
            "Start by understanding its basic definition, "
            "main concepts, real-life uses, and examples. "
            "Practice regularly to improve your understanding."
        )
        st.info("This is a basic demo explanation, not an AI-generated answer.")
    else:
        st.warning("Please enter a topic first.")

st.divider()

st.header("📝 Quiz Generator")

quiz_questions = [
    {
        "question": "What does AI stand for?",
        "options": [
            "Artificial Intelligence",
            "Automatic Internet",
            "Advanced Input",
            "Applied Information"
        ],
        "answer": "Artificial Intelligence"
    },
    {
        "question": "Which language is commonly used in AI?",
        "options": ["HTML", "Python", "CSS", "XML"],
        "answer": "Python"
    },
    {
        "question": "What is Machine Learning?",
        "options": [
            "A type of keyboard",
            "A web browser",
            "Learning patterns from data",
            "A computer screen"
        ],
        "answer": "Learning patterns from data"
    }
]

if st.button("Generate New Quiz"):
    st.session_state.quiz_order = random.sample(
        range(len(quiz_questions)), len(quiz_questions)
    )

if "quiz_order" not in st.session_state:
    st.session_state.quiz_order = list(range(len(quiz_questions)))

with st.form("quiz_form"):
    answers = {}

    for i, index in enumerate(st.session_state.quiz_order):
        question = quiz_questions[index]
        answers[index] = st.radio(
            question["question"],
            question["options"],
            key=f"answer_{i}_{index}"
        )

    submitted = st.form_submit_button("Check Score")

if submitted:
    score = sum(
        answers[index] == quiz_questions[index]["answer"]
        for index in answers
    )

    st.success(f"Your Score: {score}/{len(quiz_questions)}")

    if score == len(quiz_questions):
        st.balloons()
