import os
import requests
from flask import Flask, render_template, request, make_response
from dotenv import load_dotenv
from xhtml2pdf import pisa
from io import BytesIO
from markupsafe import Markup
import markdown

# 환경 변수 로드
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={GEMINI_API_KEY}"

app = Flask(__name__)
app.secret_key = 'your-secret-key'  # flash 등에서 필요

# 📌 Markdown 렌더링 필터 등록 (Jinja에서 |markdown 사용 가능)
@app.template_filter('markdown')
def markdown_filter(text):
    if not text:
        return ''
    return Markup(markdown.markdown(text))

# 📌 Gemini API 호출 함수
def call_gemini(prompt):
    headers = {"Content-Type": "application/json"}
    data = {"contents": [{"parts": [{"text": prompt}]}]}
    response = requests.post(GEMINI_URL, headers=headers, json=data)
    if response.status_code == 200:
        return response.json()['candidates'][0]['content']['parts'][0]['text']
    else:
        return f"❗ AI 응답 오류: {response.status_code} - {response.text}"

# ---------- ROUTES ----------

# 메인 홈
@app.route('/')
def index():
    return render_template('index.html')

# 1. 성격 기반 직업 추천
@app.route('/recommend', methods=['GET', 'POST'])
def recommend():
    if request.method == 'GET':
        return render_template('recommend_form.html')

    personality = request.form.get('personality', '')
    interest = request.form.get('interest', '')

    prompt = f"""
당신은 진로 전문 컨설턴트입니다.
아래 사용자 정보를 바탕으로 현실적이고 윤리적인 직업 3개를 아래 마크다운 형식으로 추천해 주세요.

## 🔹 사용자 정보
- 성격: {personality}
- 관심 분야: {interest}

## 📋 출력 형식 (아래 구조 반드시 지킬 것)

**✅ 추천 직업:**  
(직업명)

**💡 추천 이유 (2~3줄):**  
- 이유 1  
- 이유 2

**🛠 주요 업무:**  
- 업무1  
- 업무2

**🎓 관련 학과 및 전공:**  
- 학과1  
- 학과2

**📋 필수 및 추천 자격증:**  
- 자격증1  
- 자격증2

**📈 커리어 경로:**  
- 입문 단계 → 중급 → 고급

**🔍 직업 전망과 장단점:**  
- 장점/단점 요약

각 항목은 마크다운 구조(별, 제목, 줄바꿈)와 이모지를 지켜서 작성해 주세요.
    """
    recommendation = call_gemini(prompt)
    return render_template('result.html', recommendation=recommendation)

# 2. 관심 직업 기반 커리큘럼 추천
@app.route('/curriculum', methods=['GET', 'POST'])
def curriculum():
    if request.method == 'GET':
        return render_template('curriculum_form.html')

    job = request.form.get('job', '')

    prompt = f"""
당신은 커리큘럼 설계 전문가입니다.
아래 직업에 대해 실무와 학습을 고려한 커리큘럼을 항목별로 명확히, 마크다운 형식으로 추천해 주세요.

🔹 직업: {job}

## 📋 출력 예시 (꼭 구조를 맞춰서)

**🧾 직업 설명 (2~3줄 요약):**  
설명

**🤝 적합한 성격 및 역량:**  
- 역량1
- 역량2

**🏫 관련 학과 및 교육 과정:**  
- 학과1
- 과정2

**🏅 필수 및 추천 자격증:**  
- 필수: 자격증A
- 선택: 자격증B

**🧭 커리어 경로 (입문→경력):**  
- 경로1 → 경로2 → 경로3

**📚 추천 학습 순서 및 실전 팁:**  
- 단계1: (내용)
- 단계2: (내용)

**⚖️ 난이도와 전망:**  
- 난이도: (간단)
- 전망: (간단)
    """
    curriculum = call_gemini(prompt)
    return render_template('curriculum_result.html', curriculum=curriculum)

# 3. 자기소개서 첨삭
@app.route('/edit', methods=['GET', 'POST'])
def edit():
    if request.method == 'POST':
        self_intro = request.form.get('self_intro', '')

        prompt = f"""
당신은 AI 기반의 자기소개서 첨삭 전문가입니다.
아래 사용자의 자기소개서를 기준으로 각 항목을 마크다운 구조로 구분해서 첨삭 및 피드백 해주세요.

🔻 자기소개서 원문:
{self_intro}

## 📋 출력 구조 예시

**✍️ 문법 및 맞춤법 교정**  
- 예: '됩니다' → '됩니다.'

**✨ 표현력 및 문장 흐름 개선**  
- 어색한 문장 → 자연스러운 문장

**📑 문단별 첨삭 결과**
**[원문]**  
(원문)

**[수정]**  
(수정본)

**💬 잘한 점 3가지**
- 장점1
- 장점2

**🧩 아쉬운 점 3가지**
- 단점1
- 단점2

**📝 총평 (3~5줄)**
한 줄 평
        """
        feedback = call_gemini(prompt)
        return render_template('result_edit.html', feedback=feedback)
    return render_template('edit.html')

# PDF 다운로드 (출력 안전 처리)
@app.route('/download_pdf', methods=['POST'])
def download_pdf():
    content = request.form.get('content', '')
    html = f"""
    <html>
    <head><meta charset='utf-8'></head>
    <body>
      <pre style="font-family:pretendard,Malgun Gothic,sans-serif;white-space:pre-wrap;">{content}</pre>
    </body>
    </html>
    """

    result = BytesIO()
    pisa.CreatePDF(html, dest=result)
    result.seek(0)

    response = make_response(result.read())
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = 'attachment; filename=output.pdf'
    return response

# 서버 실행
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
