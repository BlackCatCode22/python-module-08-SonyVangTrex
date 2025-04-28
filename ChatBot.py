import streamlit as st
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage, AIMessage, SystemMessage

# Somethings that should be noted before for the LangChain Framework to work, 1. type into terminal "pip install langchain-openai" this will install some things so that the imports will work. 
# 2. to run in type, "streamlit run ChatBot.py", this will cause a pop-up on the lower right screen, that will need you to open in browser.
# 3. I'm not actually allowed to keep my stream key, because github has protections, and wont allow me to push it, so it may not work, instead replace the 'OPENAI_API_KEY' with your own, and it may work, I also deleted my api key already.
# 4. the chat bot may not actually work, this is because if you haven't put in your billing information for them to charge you, it doesn't actually work.

chat_model = ChatOpenAI(
    model_name="gpt-3.5-turbo",
    temperature=0.7,
    openai_api_key="OPENAI_API_KEY"
) 

if "conversation" not in st.session_state:
    st.session_state.conversation = [
        SystemMessage(content="Assume the role of a Python teacher, and think step by step. Your name is Skippy Py.")
    ]

def generate_response(user_input):
    st.session_state.conversation.append(HumanMessage(content=user_input))
    response = chat_model(st.session_state.conversation)
    st.session_state.conversation.append(AIMessage(content=response.content))
    return response.content

st.set_page_config(page_title="Python Study Bot", page_icon="🐍")
st.title("🐍 Skippy Py - Your Python Teacher Bot")

user_input = st.text_input("Ask Skippy Py a Python question:")

if st.button("Send"):
    if user_input:
        response = generate_response(user_input)
        st.text_area("Skippy Py says:", value=response, height=200)

if st.session_state.conversation:
    st.markdown("### Conversation History")
    for msg in st.session_state.conversation:
        if isinstance(msg, HumanMessage):
            st.write(f"👤 **You:** {msg.content}")
        elif isinstance(msg, AIMessage):
            st.write(f"🤖 **Skippy Py:** {msg.content}")

if st.button("Clear Conversation"):
    st.session_state.conversation = [
        SystemMessage(content="Assume the role of a Python teacher, and think step by step. Your name is Skippy Py.")
    ]
    st.experimental_rerun()
