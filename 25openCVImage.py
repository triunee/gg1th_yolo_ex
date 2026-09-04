import cv2  
import numpy as np 

print("OpenCV version:")  # 안내 문구 출력
print(cv2.__version__)  # 설치된 OpenCV 버전 확인

img = cv2.imread("images_opencv/bts-02.jpg")  # 이미지를 BGR 컬러로 읽어오기
print("image shape: {} pixels".format(img.shape))  # (높이, 너비, 채널) 형태 출력
print("width: {} pixels".format(img.shape[1]))  # 이미지 너비(가로 픽셀 수)
print("height: {} pixels".format(img.shape[0]))  # 이미지 높이(세로 픽셀 수)
print("channels: {}".format(img.shape[2]))  # 색상 채널 수(3: B, G, R)

(height, width) = img.shape[:2]  # shape에서 높이, 너비만 분리해서 저장

# 이미지의 중간값
center = (width // 2, height // 2)  # % : 나눗셈의 나머지 계산 , // 몫을 계산 → 이미지 중심 좌표

cv2.imshow("bts", img)  # "bts" 창에 원본 이미지 표시

# move = np.float32([[1, 0, 왼쪽에서], [0, 1, 윗쪽에서]])
# 1, 0 좌우 움직임, 0, 1 상하 움직임
# move = np.float32([[1, 0, -100], [0, 1, 100]])  # x축 -100, y축 +100 이동 매트릭스
# moved_img = cv2.warpAffine(img, move, (width, height))  # 이동 변환 적용
# cv2.imshow("Moved down: +, up: - and right: +, left - ", moved_img)  # 이동 결과 표시

# 회전
# rotate = cv2.getRotationMatrix2D(center, 90, 1.0)  # -90 : 시계 방향 90도, scale → 회전 매트릭스
# rotated_img = cv2.warpAffine(img, rotate, (width, height))  # 회전 변환 적용
# cv2.imshow("Rotated clockwise degrees", rotated_img)  # 회전 결과 표시

# 이미지 resize

# ratio = 200.0 / width  # 200px / 현재 너비 → 축소 비율 계산
# dimension = (200, int(height * ratio))  # (width, height) → 비율을 유지한 새 크기

# # interpolation(보관법) = cv2.INTER_AREA(축소시) , interpolation = cv2.INTER_LINEAR(확대시)
# # 일반적으로 cv2.INTER_AREA 사용
# resized = cv2.resize(img, dimension, interpolation = cv2.INTER_LINEAR)  # 크기 변경
# cv2.imshow("Resized", resized)  # 리사이즈 결과 표시

# 대칭으로 만들기
#lipped Horizontal 1, Vertical 0, both(대각선) -1
flipped = cv2.flip(img, 1)  # 1: 좌우 대칭, 0: 상하 대칭, -1: 상하좌우 대칭
cv2.imshow("Flipped Horizontal 1, Vertical 0, both -1 ", flipped)  # 대칭 결과 표시

cv2.waitKey(0)  # 키 입력이 있을 때까지 대기
cv2.destroyAllWindows()  # 열려 있는 모든 OpenCV 창 닫기
