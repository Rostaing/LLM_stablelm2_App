import streamlit as st 
import ollama
import time

st.set_page_config(page_title="LLM - Multilanguage App", page_icon="image/Logo_RostaingAI.jpeg")

def stream_data(text, delay:float=0.02):
    for word in text.split():
        yield word + " \n " 
        time.sleep(delay)


def llm_model():

    st.header("Large Language Model - Multilanguage App")
    prompt = st.chat_input("Ask anything")
    
    if prompt:
        with st.chat_message("user"):
            st.write(prompt)
        
        with st.spinner("Progress ..."):
            result = ollama.chat(model="stablelm2", messages=[{"role":"user", "content":prompt}])
            response = result["message"]["content"]
            st.write_stream(stream_data(response))

            
def main():
    llm_model()
    
if __name__ == "__main__":
    main()