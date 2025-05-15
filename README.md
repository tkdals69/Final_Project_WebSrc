<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Adu: AI 기반 진로 추천 웹앱 소개</title>
  <style>
    body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background: #f9fafb; color: #333; margin: 2rem; line-height: 1.6; }
    h1, h2, h3 { color: #6b21a8; }
    h1 { font-size: 2.5rem; margin-bottom: 1rem; }
    h2 { font-size: 1.8rem; margin-top: 2rem; margin-bottom: 1rem; }
    h3 { font-size: 1.4rem; margin-top: 1.5rem; margin-bottom: 1rem; }
    p { margin-bottom: 1rem; }
    ul, ol { margin-left: 2rem; margin-bottom: 1rem; }
    table { border-collapse: collapse; width: 100%; margin-bottom: 2rem; }
    th, td { border: 1px solid #ddd; padding: 0.5rem 1rem; }
    th { background-color: #e9d5ff; text-align: left; }
    code { background: #f3f4f6; padding: 0.2rem 0.4rem; border-radius: 3px; font-family: monospace; }
    blockquote { border-left: 4px solid #a78bfa; padding-left: 1rem; color: #6b21a8; font-style: italic; margin: 1rem 0; }
    .emoji { font-size: 1.2rem; margin-right: 0.3rem; vertical-align: middle; }
  </style>
</head>
<body>

  <h1><span class="emoji">🚀</span>Adu: AI 기반 진로 추천 웹앱 소개</h1>
  
  <h2><span class="emoji">🌟</span>프로젝트 개요</h2>
  <p><strong>프로젝트 이름:</strong> Adu – Career Recommendation Web Application</p>
  <p>이 프로젝트는 <strong>사용자의 성격과 관심 분야를 분석해 AI가 맞춤형 직업을 추천하고, 관련 커리큘럼을 설계하며, 자기소개서 첨삭까지 제공하는 올인원 진로 추천 웹 서비스</strong>입니다.</p>
  <ul>
    <li>🧑‍🎓 <strong>누구를 위한 서비스인가요?</strong> 취업 준비생, 진로 상담사, 교육기관, HR담당자 등 개인과 기업 모두를 대상으로 합니다.</li>
    <li>🛠️ <strong>어떤 문제를 해결하나요?</strong>
      <ul>
        <li>개인별 맞춤 진로 컨설팅의 부재</li>
        <li>객관적이고 체계적인 커리큘럼 안내 부족</li>
        <li>자기소개서 첨삭에 대한 전문성 부족 문제</li>
      </ul>
    </li>
    <li>💡 <strong>주요 기능</strong>
      <ol>
        <li>성격 기반 직업 추천</li>
        <li>관심 직업 기반 커리큘럼 추천</li>
        <li>자기소개서 첨삭 및 피드백 제공</li>
      </ol>
    </li>
    <li>🧰 <strong>사용 기술 스택</strong>
      <ul>
        <li>Backend: Python 3.8+ / Flask</li>
        <li>Frontend: Tailwind CSS</li>
        <li>AI API: Google Gemini LLM</li>
        <li>기타: Docker, CI/CD, Markdown 렌더링, PDF 변환</li>
      </ul>
    </li>
  </ul>
  
  <h2><span class="emoji">📂</span>디렉토리 구조 및 파일 설명</h2>
  <pre><code>Webpj/
├── app.py                     # Flask 앱 메인 실행 파일
├── .env                       # API 키, 비밀키 등 환경 변수
├── package.json               # Node.js 패키지 및 빌드 스크립트
├── tailwind.config.js         # Tailwind CSS 설정
├── src/
│   └── input.css              # Tailwind 빌드용 CSS 입력 파일
├── static/
│   ├── tailwind.css           # 빌드된 Tailwind CSS 파일
│   └── loading.js             # 로딩 애니메이션 스크립트
├── templates/
│   ├── base.html              # 공통 레이아웃 템플릿
│   ├── index.html             # 메인 기능 선택 페이지
│   ├── recommend_form.html    # 성격 기반 직업 추천 입력 폼
│   ├── curriculum_form.html   # 관심 직업 커리큘럼 입력 폼
│   ├── edit.html              # 자기소개서 첨삭 입력 폼
│   ├── result.html            # 직업 추천 결과 페이지
│   ├── curriculum_result.html # 커리큘럼 추천 결과 페이지
│   └── result_edit.html       # 자기소개서 첨삭 결과 페이지
</code></pre>

  <h2><span class="emoji">⚙️</span>설치 및 환경 설정</h2>
  <h3>필수 요구사항</h3>
  <ul>
    <li>Python 3.8 이상</li>
    <li>Node.js 16 이상 (LTS 권장)</li>
    <li>npm (Node.js 설치 시 자동 포함)</li>
  </ul>

  <h3>개발 환경 구축 가이드</h3>
  <ol>
    <li>
      <strong>가상환경 생성 및 활성화</strong><br />
      <code>python3 -m venv venv</code><br />
      <code>source venv/bin/activate</code> (Linux / macOS)<br />
      <code>venv\Scripts\activate</code> (Windows)
    </li>
    <li>
      <strong>Python 패키지 설치</strong><br />
      <code>pip install -r requirements.txt</code>
    </li>
    <li>
      <strong>Node.js 패키지 설치</strong><br />
      <code>npm install</code>
    </li>
    <li>
      <strong>Tailwind CSS 빌드</strong><br />
      배포용 압축 빌드: <code>npm run build-css</code><br />
      개발용 실시간 감시: <code>npm run watch-css</code>
    </li>
    <li>
      <strong>환경변수 설정</strong><br />
      프로젝트 루트에 <code>.env</code> 파일 생성<br />
      예시:<br />
      <code>GEMINI_API_KEY=your_google_gemini_api_key</code><br />
      <code>FLASK_SECRET_KEY=your_flask_secret_key</code>
    </li>
  </ol>

  <h2><span class="emoji">▶️</span>빌드 및 실행 방법</h2>
  <ul>
    <li><strong>Flask 개발 서버 실행</strong><br />
      <code>flask run --host=0.0.0.0 --port=5000</code>
    </li>
    <li><strong>Tailwind CSS 빌드 명령어</strong><br />
      배포용: <code>npm run build-css</code><br />
      개발 모드: <code>npm run watch-css</code>
    </li>
    <li><strong>Docker 이미지 빌드 및 실행 (옵션)</strong><br />
      <code>docker build -t adu-career-app .</code><br />
      <code>docker run -p 5000:5000 --env-file .env adu-career-app</code>
    </li>
  </ul>

  <table>
    <thead>
      <tr>
        <th>명령어</th>
        <th>설명</th>
      </tr>
    </thead>
    <tbody>
      <tr><td><code>pip install -r requirements.txt</code></td><td>Python 의존성 설치</td></tr>
      <tr><td><code>npm install</code></td><td>Node.js 의존성 설치</td></tr>
      <tr><td><code>npm run build-css</code></td><td>Tailwind 프로덕션 빌드</td></tr>
      <tr><td><code>npm run watch-css</code></td><td>Tailwind 개발 감시</td></tr>
      <tr><td><code>flask run</code></td><td>Flask 서버 실행</td></tr>
      <tr><td><code>docker build</code></td><td>Docker 이미지 빌드</td></tr>
      <tr><td><code>docker run</code></td><td>Docker 컨테이너 실행</td></tr>
    </tbody>
  </table>

  <h2><span class="emoji">💼</span>주요 기능 설명</h2>
  <h3>1. 성격 기반 직업 추천</h3>
  <ul>
    <li>사용자의 성격과 관심 분야 입력</li>
    <li>AI가 맞춤 직업 추천, 추천 이유, 주요 업무, 관련 학과, 자격증, 커리어 경로, 전망과 장단점까지 마크다운 형식으로 응답</li>
    <li>가독성 높은 UI로 결과 출력</li>
  </ul>

  <h3>2. 관심 직업 기반 커리큘럼 추천</h3>
  <ul>
    <li>희망 직업명 입력</li>
    <li>AI가 직업 설명, 적합 역량, 교육 과정, 추천 자격증, 커리어 경로, 학습 팁 등을 체계적으로 제안</li>
    <li>마크다운을 UI에 맞게 깔끔하게 렌더링</li>
  </ul>

  <h3>3. 자기소개서 첨삭 및 피드백</h3>
  <ul>
    <li>자기소개서 전문 입력</li>
    <li>AI가 문법, 표현력, 흐름, 장단점, 총평까지 문단별 첨삭</li>
    <li>마크다운 형식으로 결과 제공하여 가독성 향상</li>
  </ul>

  <h3>AI API 연동</h3>
  <p>Google Gemini API를 REST 방식으로 호출하며, Flask 백엔드에서 API 키를 안전하게 관리하며 서비스 운영합니다.</p>

  <h2><span class="emoji">🚀</span>배포 및 운영 가이드</h2>
  <ul>
    <li><strong>CI/CD 연동</strong>  
      <br/>GitHub Actions, Jenkins 등으로 자동 빌드, 테스트, Docker 이미지 생성, 배포 프로세스 구현 가능
    </li>
    <li><strong>보안 관리</strong>  
      <br/>API 키 및 시크릿은 <code>.env</code> 파일이나 시크릿 매니저에서
