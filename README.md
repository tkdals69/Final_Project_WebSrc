# Adu: AI 기반 진로 추천 웹앱

---

## 1. 프로젝트 개요

**프로젝트 이름:** Adu - Career Recommendation Web Application

**목적:**  
사용자의 성격과 관심 분야를 기반으로 AI가 맞춤형 직업 추천, 커리큘럼 설계, 자기소개서 첨삭을 제공하는 웹 서비스입니다.  
본 프로젝트는 취업 준비생과 진로 상담 서비스를 제공하는 기관, 기업을 대상으로 하며, 객관적이고 개인화된 진로 컨설팅을 실현합니다.

**주요 기능:**  
- 성격 기반 직업 추천  
- 관심 직업 기반 커리큘럼 추천  
- 자기소개서 첨삭 및 피드백  

**기술 스택:**  
- Backend: Python 3.8+ / Flask  
- Frontend: Tailwind CSS  
- AI API: Google Gemini API (LLM)  
- 기타: Docker, CI/CD, Markdown 렌더링, PDF 변환  

---

## 2. 디렉토리 구조 및 파일 설명

Webpj/
├── app.py # Flask 메인 애플리케이션 엔트리 포인트
├── .env # 환경변수 파일 (API 키, 비밀키 등)
├── package.json # Node.js 패키지 및 빌드 스크립트 관리
├── tailwind.config.js # Tailwind CSS 설정
├── src/
│ └── input.css # Tailwind CSS 빌드용 소스 CSS
├── static/
│ ├── tailwind.css # 빌드된 Tailwind CSS 파일
│ └── loading.js # 로딩 애니메이션 JS
├── templates/
│ ├── base.html # 공통 레이아웃 템플릿
│ ├── index.html # 메인 기능 선택 페이지
│ ├── recommend_form.html # 직업 추천 입력 폼
│ ├── curriculum_form.html # 커리큘럼 추천 입력 폼
│ ├── edit.html # 자기소개서 첨삭 입력 폼
│ ├── result.html # 직업 추천 결과
│ ├── curriculum_result.html # 커리큘럼 추천 결과
│ └── result_edit.html # 자기소개서 첨삭 결과

yaml
복사

---

## 3. 설치 및 환경 설정 방법

### 필수 요구 사항

- Python 3.8 이상  
- Node.js 16 이상 (LTS 권장)  
- npm (Node.js 설치 시 포함)  

### 개발 환경 구축

1. **Python 가상환경 생성 및 활성화**

   ```bash
   python3 -m venv venv
   source venv/bin/activate    # Linux / MacOS
   venv\Scripts\activate       # Windows
Python 의존성 설치

bash
복사
pip install -r requirements.txt
Node.js 패키지 설치

bash
복사
npm install
Tailwind CSS 빌드

프로덕션 빌드 (압축 포함)

bash
복사
npm run build-css
개발 중 실시간 빌드 감시

bash
복사
npm run watch-css
환경 변수 설정

프로젝트 루트에 .env 파일 생성

다음 예시 참고

ini
복사
GEMINI_API_KEY=your_google_gemini_api_key
FLASK_SECRET_KEY=your_flask_secret_key
4. 빌드 및 실행 방법
로컬 개발 서버 실행

bash
복사
flask run --host=0.0.0.0 --port=5000
Tailwind CSS 빌드 명령어

bash
복사
npm run build-css     # 배포용
npm run watch-css     # 개발용 실시간 감시
Docker 이미지 빌드 및 실행 (옵션)

bash
복사
docker build -t adu-career-app .
docker run -p 5000:5000 --env-file .env adu-career-app
주요 커맨드 요약

명령어	설명
pip install -r requirements.txt	Python 패키지 설치
npm install	Node.js 패키지 설치
npm run build-css	Tailwind CSS 프로덕션 빌드
npm run watch-css	Tailwind CSS 개발 감시
flask run	Flask 앱 실행
docker build	Docker 이미지 빌드
docker run	Docker 컨테이너 실행

5. 기능 설명
1) 성격 기반 직업 추천
사용자의 성격과 관심 분야 입력

AI가 직업 추천, 추천 이유, 주요 업무, 관련 학과, 자격증, 커리어 경로, 전망과 장단점을 마크다운 형식으로 응답

결과는 가독성 높은 UI로 출력

2) 관심 직업 기반 커리큘럼 추천
희망 직업명 입력

AI가 직업 설명, 적합 역량, 교육 과정, 추천 자격증, 커리어 경로, 학습 팁 등을 체계적으로 제안

마크다운 형태로 출력해 UI에 맞게 렌더링

3) 자기소개서 첨삭 및 피드백
자기소개서 전문 입력

AI가 문법, 표현, 흐름, 장단점, 최종 피드백까지 문단별로 첨삭

마크다운 형식으로 출력하여 UI에서 보기 좋게 처리

AI API 연동
Google Gemini API를 REST 방식으로 호출

Flask 백엔드에서 API 키 보안 유지하며 호출 및 응답 처리

6. 배포 및 운영 관련 안내
CI/CD 연동

GitHub Actions, Jenkins 등으로 빌드 → 테스트 → Docker 이미지 생성 → 배포 자동화 가능

보안 관리

API 키 및 시크릿은 .env 또는 시크릿 매니저 활용

공개 저장소에 노출 금지

권장 배포 환경

Docker 기반 컨테이너 배포 (AWS ECS, GCP Cloud Run, Kubernetes 등)

HTTPS 적용 및 인증서 관리

운영 모니터링

Prometheus, Grafana, ELK 스택 등 로그·메트릭 수집 도구 활용

장애 대응 체계 마련
