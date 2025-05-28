# 웹 기반 객체 출입 카운팅 시스템

이 프로젝트는 YOLOv8 기반 객체 추적 및 출입 인원 카운팅 시스템을 웹에서 실행할 수 있도록 구성한 간단한 데모입니다.  
원본 프로젝트는 아래를 참고해주세요.

🔗 참고 원본: https://github.com/mahdi-marjani/object-tracking-entry-exit

---

## ✅ 주요 기능

- YOLOv8을 이용한 사람 추적 및 IN/OUT 카운팅
- 기준선을 넘는 객체 수를 자동 기록 (`report.txt`)
- 웹 버튼 클릭으로 `main.py` 실행 가능
- 결과 영상 저장 및 실시간 화면 출력

---

## 📁 디렉토리 구조 예시

```

├── main.py                    # 객체 추적 및 카운팅 실행 파일
├── download\_model.py         # yolov8n.pt 모델 다운로드 스크립트
├── server.py                 # Flask 웹 서버
├── index.html                # 실행 버튼 UI
├── models/
│   └── yolov8n.pt            # YOLOv8 모델 파일
├── videos/
│   ├── people.mp4            # 입력 영상
│   └── object\_counting\_output.mp4  # 결과 저장 영상
└── report.txt                # 출입 기록 로그

````

---

## 🛠 설치 및 실행 방법

### 1. 레포지토리 클론
```bash
git clone https://github.com/yourname/yourrepo.git
cd yourrepo
```

### 2. uv 설치 (처음 사용하는 경우)
```bash
# Windows (PowerShell)
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

# macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### 3. 가상환경 생성 및 활성화
```bash
# 가상환경 생성
uv venv

# 가상환경 활성화
# Windows (PowerShell)
.venv\Scripts\Activate.ps1

# Windows (Command Prompt)
.venv\Scripts\activate.bat

# macOS/Linux
source .venv/bin/activate
```

### 4. 프로젝트 의존성 설치
```bash
# 프로젝트를 editable 모드로 설치 (의존성 포함)
uv pip install -e .
```

### 5. YOLO 모델 다운로드
```bash
python download_model.py
```

### 6. 웹 서버 실행
```bash
python server.py
```

### 7. 웹 브라우저 접속

* [http://localhost:5000](http://localhost:5000) 으로 접속
* ▶ Run main.py 버튼 클릭 시 영상 분석 시작

---

## 📝 로그 기록

* 출입 내역은 `report.txt`에 시간과 함께 저장됩니다.
* 분석 결과 영상은 `videos/object_counting_output.mp4`로 저장됩니다.

---

## 📌 참고

* 본 프로젝트는 [mahdi-marjani/object-tracking-entry-exit](https://github.com/mahdi-marjani/object-tracking-entry-exit) 를 기반으로 일부 구조를 변경하고, 웹 실행 기능을 추가한 예시입니다.

```

---

원하시면 영어/일본어 병기, 이미지/데모 영상 링크 삽입 버전도 드릴 수 있습니다!
 