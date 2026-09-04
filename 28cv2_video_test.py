# opencv 라이브 카메라 테스트
import numpy as np
import cv2
import time

elapsed_time = 0                    # 전체 프레임 처리에 걸린 누적 시간(초)
title_name = 'opencv video test'    # 영상을 표시할 창 제목

def detectAndDisplay(image):
    # 한 프레임을 화면에 표시하고 처리 시간을 측정하는 함수
    start_time = time.time()        # 프레임 처리 시작 시각
    (h, w) = image.shape[:2]        # 프레임의 높이(h), 너비(w)

    cv2.imshow(title_name, image)   # 창에 현재 프레임 출력

    # 이미지 처리 확인
    end_time = time.time()          # 프레임 처리 종료 시각
    frame_time = end_time - start_time   # 이번 프레임 처리에 걸린 시간
    #print(start_time, end_time)
    global elapsed_time
    elapsed_time += frame_time      # 누적 처리 시간에 더함
    # print("Frame time {:.10f} seconds".format(frame_time))
    cv2.imshow(title_name, image)

# 비디오 사용, 0번 캠
vc = cv2.VideoCapture(0)            # 0번 카메라(기본 웹캠) 열기
time.sleep(5.0) # 5초 지연          # 카메라 초기화 대기
if not vc.isOpened:                 # 카메라가 열리지 않았으면 종료
    print('### Error opening video ###')
    exit(0)
vc.set(cv2.CAP_PROP_FRAME_WIDTH, 640)    # 캡처 해상도 너비 설정
vc.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)   # 캡처 해상도 높이 설정
while True:
    ret, frame = vc.read()         # 카메라에서 한 프레임 읽기 (ret: 성공 여부, frame: 이미지)
    print(ret, frame)
    # time.sleep(1.0) # 5초 지연
    if frame is None:              # 더 이상 읽을 프레임이 없으면 반복 종료
        print('### No more frame ###')
        vc.release()
        break
    detectAndDisplay(frame)        # 프레임을 화면에 표시

    if cv2.waitKey(1) & 0xFF == ord('q'):   # 'q' 키를 누르면 반복 종료
        break


# 메모리 정리
vc.release()                       # 카메라 자원 해제
cv2.destroyAllWindows()            # 모든 OpenCV 창 닫기
