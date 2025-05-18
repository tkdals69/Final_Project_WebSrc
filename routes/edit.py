# routes/edit.py

from flask import Blueprint, render_template, request
from utils.gemini import call_gemini

bp = Blueprint('edit', __name__, url_prefix='/edit')


@bp.route('/', methods=['GET', 'POST'])
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
