import streamlit as st
from openai import OpenAI
import os

# API Key는 코드에 절대 적지 않는다!
client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

st.title("📄 AI 파일 요약 + 감정 분석기")

uploaded_file = st.file_uploader("분석할 텍스트 파일을 업로드하세요 (.txt)", type=["txt"])

if uploaded_file is not None:
    text = uploaded_file.read().decode("utf-8")

    st.subheader("📌 원문 내용")
    st.text(text)

    # LLM 요청
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {
                "role": "system",
                "content": """
                너는 한국어 텍스트 분석 전문가야.
                1) 글을 3~5줄로 요약하고
                2) 감정(긍정/부정/중립)을 판단하고 근거를 제시해.
                """
            },
            {
                "role": "user",
                "content": text
            }
        ]
    )

    st.subheader("🧠 분석 결과")
    st.write(response.choices[0].message.content)
