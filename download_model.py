from ultralytics import YOLO
import os
import shutil

# 모델 디렉토리 만들기
os.makedirs("models", exist_ok=True)

# yolov8n 모델 다운로드 (자동으로 현재 디렉토리에 yolov8n.pt 저장됨)
print("📦 Downloading yolov8n.pt...")
model = YOLO("yolov8n.pt")

# 다운로드된 모델 파일이 현재 디렉토리에 있는지 확인
source_path = "./yolov8n.pt"
target_path = "./models/yolov8n.pt"

if os.path.exists(source_path):
    shutil.move(source_path, target_path)
    print(f"✅ 모델 이동 완료: {target_path}")
else:
    print("❌ yolov8n.pt 파일을 찾을 수 없습니다.")

