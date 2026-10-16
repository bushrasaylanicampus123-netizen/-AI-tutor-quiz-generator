import streamlit as st
import random

st.set_page_config(
    page_title="AI Tutor & Quiz Generator",
    page_icon="📚"
)

st.title("📚 AI Tutor & Quiz Generator")
st.write("Learn new topics and test your knowledge!")

topic = st.text_input("Enter a topic to learn:")

if st.button("Explain Topic"):
    if topic.strip():
        st.info(
            f"You selected: {topic}\n\n"
            "This is the basic tutor demo. "
            "AI-generated explanations will be added "
            "when an AI model is connected."
        )
    else:
        st.warning("Please enter a topic first.")

st.divider()
st.subheader("📝 Take a Quiz")

questions = {
    "What is AI?": [
        "A technology that enables intelligent tasks",
        "A keyboard",
        "A printer",
        "A mouse"
    ],
    "Which language is popular for AI?": [
        "HTML",
        "Python",
        "CSS",
        "XML"
    ],
    "What is Machine Learning?": [
        "Learning patterns from data",
        "A computer screen",
        "A typing method",
        "A web browser"
    ]
}

if "quiz" not in st.session_state:
    st.session_state.quiz = random.sample(
        list(questions.keys()), len(questions)
    )

with st.form("quiz_form"):
    answers = {}

    for i, question in enumerate(st.session_state.quiz):
        answers[question] = st.radio(
            question,
            questions[question],
            key=f"q{i}"
        )

    submitted = st.form_submit_button("Check Score")

if submitted:
    score = 0

    for question, answer in answers.items():
        if answer == questions[question][0]:
            score += 1

    st.success(f"Your Score: {score}/{len(questions)}")

    if score == len(questions):
        st.balloons()
