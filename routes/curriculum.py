# routes/curriculum.py

from flask import Blueprint, render_template, request
from services.gemini_service import call_gemini

bp = Blueprint('curriculum', __name__, url_prefix='/curriculum')


@bp.route('/', methods=['GET', 'POST'])
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
