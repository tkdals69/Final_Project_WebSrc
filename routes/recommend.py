# routes/recommend.py

from flask import Blueprint, render_template, request
from services.gemini_service import call_gemini
from flask import send_file, request
import io
from fpdf import FPDF

bp = Blueprint('recommend', __name__, url_prefix='/recommend')


@bp.route('/', methods=['GET', 'POST'])
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

from flask import send_file, request
from fpdf import FPDF
import io

@bp.route('/download_pdf', methods=['POST'])
def download_pdf():
    # 폼에서 추천 결과 내용을 가져옴 (hidden input 또는 textarea로 전달 필요)
    recommendation = request.form.get('recommendation', '')

    # PDF 객체 생성
    pdf = FPDF()
    pdf.add_page()
    pdf.add_font('Nanum', '', '/usr/share/fonts/truetype/nanum/NanumGothic.ttf', uni=True)
    pdf.set_font('Nanum', size=12)  # 한글 폰트 사용

    # 줄바꿈 처리
    for line in recommendation.split('\n'):
        pdf.cell(0, 10, txt=line, ln=True)

    # PDF를 메모리로 저장
    pdf_output = io.BytesIO()
    pdf.output(pdf_output)
    pdf_output.seek(0)

    return send_file(
        pdf_output,
        as_attachment=True,
        download_name='recommendation.pdf',
        mimetype='application/pdf'
    )

