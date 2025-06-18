import streamlit as st
import requests

def main():
    st.title("AI Text Summarizer")
    st.write("Enter your text below to get a summary.")

    text = st.text_area("Text to summarize:", height=200)

    max_length = st.slider("Maximum length", 50, 500, 130)
    min_length = st.slider("Minimum length", 10, 100, 30)

    if st.button("Summarize"):
        if len(text.strip()) < 100:
            st.error("Please enter at least 100 characters of text.")
            return
        
        with st.spinner("Generating summary..."):
            try:
                response = requests.post(
                    "http://localhost:5000/summarize",
                    json={
                        "text": text,
                        "max_length": max_length,
                        "min_length": min_length
                    }
                )

                if response.status_code == 200:
                    st.success("Summary generated!")
                    st.write(response.json()["summary"])
                else:
                    st.error(f"Error: {response.json()["detail"]}")
            except Exception as e:
                st.error(f"Error connecting to the API: {e}")
                return

if __name__ == "__main__":
    main()