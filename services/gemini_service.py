# 제미나이 호출
import requests
from flask import current_app


def call_gemini(prompt):
    headers = {"Content-Type": "application/json"}
    data = {"contents": [{"parts": [{"text": prompt}]}]}
    url = current_app.config['GEMINI_URL']
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        return response.json()['candidates'][0]['content']['parts'][0]['text']
    else:
        return f"❗ AI 응답 오류: {response.status_code} - {response.text}"
