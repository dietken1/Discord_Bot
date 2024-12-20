# ai.py
import os

from openai import OpenAI
from dotenv import load_dotenv

# 환경 변수를 .env 파일에서 로딩
load_dotenv()

OPENAI_KEY = os.getenv("OPENAI_KEY")

# OpenAI 객체 설정
client = OpenAI(api_key=OPENAI_KEY)


def ask(messages, model="gpt-3.5-turbo"):   # 모델명은 원하는 모델 선택
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        max_tokens=500,
        temperature=0.5,
    )
    message = response.choices[0].message.content
    print(message)
    messages.append(response.choices[0].message)
    return message