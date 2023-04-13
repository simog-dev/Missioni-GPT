import streamlit as st
from decouple import config
from qa_missioni import _run

response = False
prompt_tokens = 0
completion_tokes = 0
total_tokens_used = 0
cost_of_response = 0

OPENAI_API_KEY = config('OPENAI_API_KEY')

def make_request(question_input: str):
    response = _run(question_input)
    return response

st.set_page_config(
    page_title="Missioni GPT",
)
st.header("Missioni GPT")
question_input = st.text_input('Ask a question or enter a search query. For example: "What I have to do to request a mission?"')
rerun_button = st.button("Search")

st.markdown("""---""")

if question_input:
    response = make_request(question_input)
else:
    pass

if rerun_button:
    response = make_request(question_input)
else:
    pass

if response:
    st.write("Response:")
    st.write(response)
else:
    pass


with st.sidebar:
    st.title("Information:")
    st.markdown("""---""")
    st.write("🔴 Responses generated may contain incorrect and/or incomplete information")
    st.write("🇮🇹/🇬🇧 You can use either Italian or English")
    st.write("⚡ To get detailed answers, ask specific inquiries")
    st.write("📚 The information used to generate responses is extracted from the following documents https://github.com/simog-dev/Missioni-GPT/tree/main/data")
    st.markdown("""---""")
    st.write("https://simog-dev.github.io/")
