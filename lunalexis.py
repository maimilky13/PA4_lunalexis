import streamlit as st
import openai

# Sidebar สำหรับป้อน API Key
st.sidebar.title("API Settings")
api_key = st.sidebar.text_input("Enter your OpenAI API key", type="password")

if api_key:
    openai.api_key = api_key

    st.title("OpenAI API Key Test")
    st.subheader("Enter a prompt to test the API:")
    user_prompt = st.text_area("Prompt:", placeholder="Type something to test the OpenAI API...")

    if st.button("Submit"):
        if user_prompt.strip():
            try:
                # เรียกใช้ OpenAI API
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "user", "content": user_prompt}
                    ]
                )
                # แสดงผลลัพธ์ที่ได้
                output_text = response.choices[0].message["content"].strip()
                st.subheader("API Response:")
                st.write(output_text)
            except Exception as e:
                st.error(f"Error: {e}")
        else:
            st.warning("Please enter a prompt to test!")
else:
    st.warning("Please enter your OpenAI API key in the sidebar.")
