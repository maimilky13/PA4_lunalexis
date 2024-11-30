import streamlit as st
import openai

# ตั้งค่า API Key
openai.api_key = st.secrets["OPENAI_API_KEY"]

# ฟังก์ชันสำหรับเรียก GPT
def get_gpt_response(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt},
            ],
        )
        return response["choices"][0]["message"]["content"].strip()
    except Exception as e:
        return f"Error: {e}"

# สร้างหน้าเว็บด้วย Streamlit
st.title("OpenAI GPT Chat")
st.write("กรุณาใส่ข้อความเพื่อสนทนากับ GPT")

# ช่องป้อนข้อความ
user_input = st.text_area("ข้อความ:", placeholder="พิมพ์คำถามหรือข้อความที่ต้องการถาม GPT...")

# ปุ่มส่งข้อความ
if st.button("ส่ง"):
    if user_input.strip():
        with st.spinner("กำลังประมวลผล..."):
            response = get_gpt_response(user_input)
        st.write("**GPT ตอบ:**")
        st.write(response)
    else:
        st.warning("กรุณาใส่ข้อความก่อนส่ง!")

# คำเตือน
st.sidebar.header("คำแนะนำ")
st.sidebar.info("โปรดตรวจสอบว่าได้ตั้งค่า API Key ใน secrets ของ Streamlit แล้ว")
