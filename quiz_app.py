
import streamlit as st

st.set_page_config(
    page_title="Quiz Examination System",
    page_icon="📝",
    layout="centered"
)

st.title("Quiz Examination System")
st.caption("CM25112")
st.write("Test your Python knowledge!")

questions = [
    {
        "question": "1. Which language is used for web page structure?",
        "options": ["Python", "HTML", "C++", "Java"],
        "answer": "HTML"
    },
    {
        "question": "2. Which keyword is used to define a function in Python?",
        "options": ["function", "fun", "def", "define"],
        "answer": "def"
    },
    {
        "question": "3. Which symbol is used for comments in Python?",
        "options": ["//", "#", "/*", "$"],
        "answer": "#"
    },
    {
        "question": "4. Which function displays output in Python?",
        "options": ["input()", "print()", "show()", "write()"],
        "answer": "print()"
    },
    {
        "question": "5. Which data type stores True or False?",
        "options": ["int", "str", "bool", "float"],
        "answer": "bool"
    },
    {
        "question": "6. Which collection stores multiple items in order?",
        "options": ["list", "int", "bool", "float"],
        "answer": "list"
    },
    {
        "question": "7. Which operator checks equality?",
        "options": ["=", "==", "!=", ">"],
        "answer": "=="
    },
    {
        "question": "8. Which loop repeats while a condition is true?",
        "options": ["if", "while", "def", "return"],
        "answer": "while"
    },
    {
        "question": "9. What is the output of 2 ** 3?",
        "options": ["5", "6", "8", "9"],
        "answer": "8"
    },
    {
        "question": "10. Which keyword is used for a decision?",
        "options": ["if", "for", "import", "print"],
        "answer": "if"
    }
]

if "result" not in st.session_state:
    st.session_state.result = None

with st.form("quiz_form"):
    name = st.text_input("Student Name")

    selected_answers = []

    for i, q in enumerate(questions):
        st.subheader(f"Question {i + 1}")
        st.write(q["question"])

        answer = st.radio(
            "Select your answer:",
            q["options"],
            index=None,
            key=f"question_{i}"
        )
        selected_answers.append(answer)

    submitted = st.form_submit_button("Submit Quiz")

    if submitted:
        if not name.strip():
            st.warning("Please enter your name.")
        elif any(a is None for a in selected_answers):
            st.warning("Please answer all questions.")
        else:
            score = sum(
                selected_answers[i] == questions[i]["answer"]
                for i in range(len(questions))
            )

            st.session_state.result = {
                "name": name.strip(),
                "answers": selected_answers,
                "score": score
            }

if st.session_state.result is not None:
    result = st.session_state.result
    score = result["score"]
    total = len(questions)
    percentage = score / total * 100

    st.divider()
    st.success("Quiz submitted successfully!")
    st.header(f"Score: {score}/{total}")
    st.write(f"**Student:** {result['name']}")
    st.write(f"**Percentage:** {percentage:.0f}%")

    if percentage >= 80:
        st.success("Performance: Excellent")
    elif percentage >= 50:
        st.info("Performance: Good")
    else:
        st.warning("Performance: Needs Improvement")

    st.subheader("Answer Review")

    for i, q in enumerate(questions):
        st.write(f"**{q['question']}**")
        st.write(f"Your answer: {result['answers'][i]}")
        st.write(f"Correct answer: {q['answer']}")

        if result["answers"][i] == q["answer"]:
            st.write("Result: Correct")
        else:
            st.write("Result: Incorrect")

        st.divider()

    if st.button("Restart Quiz"):
        st.session_state.result = None
        for i in range(len(questions)):
            st.session_state.pop(f"question_{i}", None)
        st.rerun()
  
