import cv2
from ultralytics import YOLO
from ultralytics.solutions import object_counter
from datetime import datetime

# 모델 로드
model = YOLO("./models/yolov8n.pt")

# 비디오 캡처 설정
cap = cv2.VideoCapture("./videos/people.mp4")
assert cap.isOpened(), "Error reading video file"
w, h, fps = (int(cap.get(x)) for x in (
    cv2.CAP_PROP_FRAME_WIDTH,
    cv2.CAP_PROP_FRAME_HEIGHT,
    cv2.CAP_PROP_FPS
))

# 카운팅 영역 설정 (선 또는 다각형)
region_points = [(120, 380), (580, 252)]  # 선 또는 다각형 영역

# 비디오 저장 설정
video_writer = cv2.VideoWriter(
    "./videos/object_counting_output.mp4",
    cv2.VideoWriter_fourcc(*'mp4v'),
    fps,
    (w, h)
)

# ObjectCounter 초기화
counter = object_counter.ObjectCounter(
    model="./models/yolov8n.pt",
    region=region_points,
    classes=[0],  # 사람 클래스만 카운트
    show=True,  # 결과를 화면에 표시
    line_width=2,
    show_conf=True,
    show_labels=True
)

# 이전 카운트 초기화
prev_in_count = 0
prev_out_count = 0

# 프레임 처리 루프
while cap.isOpened():
    success, frame = cap.read()
    if not success:
        print("비디오 프레임을 읽을 수 없거나 처리가 완료되었습니다.")
        break

    # 프레임 처리 및 카운팅
    results = counter(frame)

    # 현재 카운트 가져오기
    current_in_count = counter.in_count
    current_out_count = counter.out_count

    # 카운트 변화 계산
    in_diff = current_in_count - prev_in_count
    out_diff = current_out_count - prev_out_count

    # 현재 시간 기록
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # 카운트 변화 기록
    if in_diff > 0:
        with open("report.txt", "a", encoding="utf-8") as file:
            file.write(f"{in_diff}명이 입장함 - {current_time}\n")
    if out_diff > 0:
        with open("report.txt", "a", encoding="utf-8") as file:
            file.write(f"{out_diff}명이 퇴장함 - {current_time}\n")

    # 이전 카운트 업데이트
    prev_in_count = current_in_count
    prev_out_count = current_out_count

    # 결과 프레임 저장
    video_writer.write(results.plot_im)

# 자원 해제
cap.release()
video_writer.release()
cv2.destroyAllWindows()

