import streamlit as st
import openai

st.title("Mì AI - Tích hợp ChatGPT vào ứng dụng Python")

# Cài đặt thông tin model
model = "code-davinci-002"#"text-davinci-003"
with open("apikey.txt","r") as f:
    openai.api_key = f.readline()


# Hàm để gọi đến OpenAPI / Phần ChatGPT
def get_response_from_chatgpt(user_question):
    response = openai.Completion.create(
        engine= model,
        prompt = user_question,
        max_tokens = 1024,
        n = 1,
        temperature = 0.5
    )

    response_text = response.choices[0].text
    return response_text


# Điều khiển giao diện
def main():
    user_question = st.text_input("Nhập câu hỏi vào đây:")
    if st.button("Chat với em đi"):
        response_text = get_response_from_chatgpt(user_question)
        return st.write(f"{user_question} {response_text}")

main()