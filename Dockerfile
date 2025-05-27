# 1. 베이스 이미지: Python 3.9 slim
FROM python:3.9-slim

# 2. 작업 디렉토리 지정
WORKDIR /app

# 3. 파이썬 패키지 인덱스 업데이트 및 필수 패키지 설치
RUN apt-get update && apt-get install -y \
    build-essential \
    gcc \
    # PDF 변환 등 필요 시 추가 패키지(예: wkhtmltopdf, poppler-utils 등)
    && rm -rf /var/lib/apt/lists/*

# 4. 파이썬 의존성 사전 설치(캐싱 최적화)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 5. 소스 전체 복사
COPY . .

# 6. (권장) 언어/타임존/인코딩 환경 변수 설정
ENV LANG=C.UTF-8 \
    TZ=Asia/Seoul \
    PYTHONUNBUFFERED=1

# 7. .env 파일은 실행 시 mount 권장 (이미지 내 COPY도 가능)
COPY .env . 

# 8. 포트 노출(Flask 기본 5000, 운영용 8000 등)
EXPOSE 8000

# 9. Gunicorn(운영)/Flask(개발) 선택 실행
# 운영 서버: gunicorn으로 실행 (app:Flask인스턴스명)

CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]