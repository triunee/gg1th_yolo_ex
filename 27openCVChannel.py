import cv2 
import numpy as np  # 빈 채널 배열 생성을 위한 numpy 불러오기

print("OpenCV version:")  # 안내 문구 출력
print(cv2.__version__)  # 설치된 OpenCV 버전 확인

img = cv2.imread("images_opencv/bts-03.jpg")  # 이미지를 BGR 컬러로 읽어오기
print("image shape : {} pixels".format(img.shape))  # (높이, 너비, 채널) 형태 출력
print("width: {} pixels".format(img.shape[1]))  # 이미지 너비(가로 픽셀 수)
print("height: {} pixels".format(img.shape[0]))  # 이미지 높이(세로 픽셀 수)
print("channels: {}".format(img.shape[2]))  # 색상 채널 수(3: B, G, R)

(height, width) = img.shape[:2]  # 높이, 너비만 분리해서 저장
center = (width // 2, height // 2)  # 이미지 중심 좌표

cv2.imshow("bts original", img)  # 원본 이미지 표시

# img의 이미지의 color channel 분리
(B, G, R) = cv2.split(img)  # 컬러 이미지를 B, G, R 단일 채널 3개로 분리

# cv2.imshow("Red Channel", R)  # 빨강 채널을 흑백 강도로 표시
# cv2.imshow("Green Channel", G)  # 초록 채널을 흑백 강도로 표시
# cv2.imshow("Blue Channel", B)  # 파랑 채널을 흑백 강도로 표시
# cv2.waitKey(0)  # 키 입력 대기

# 색상을 머지함
# zeros_img = np.zeros(img.shape[:2], dtype = "uint8")  # 값이 0인 빈 채널 생성
# cv2.imshow("Red", cv2.merge([zeros_img, G, R]))  # B를 0으로 채워 병합
# cv2.imshow("Green", cv2.merge([zeros_img, G, zeros_img]))  # G만 남기고 병합
# cv2.imshow("Blue", cv2.merge([B, zeros_img, zeros_img]))  # B만 남기고 병합
# cv2.waitKey(0)  # 키 입력 대기

# 필터 적용
# gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 흑백으로 변환
# cv2.imshow("Gray Filter", gray_img)  # 흑백 결과 표시

# hsv : 색상(Hue), 채도(Saturation), 명도(Value)
# hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)  # HSV 색공간으로 변환
# cv2.imshow("HSV Filter", hsv_img)  # HSV 결과 표시

#  Lab Color 채널을 이용해 이미지 선명도를 높이기 위한 필터
# lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)  # Lab 색공간으로 변환
# cv2.imshow("LAB Filter", lab)  # Lab 결과 표시
# cv2.waitKey(0)  # 키 입력 대기

BGR = cv2.merge([B, G, R])  # 분리했던 B, G, R 채널을 다시 하나의 컬러 이미지로 병합
cv2.imshow("Blue, Green and Red", BGR)  # 병합 결과 표시(원본과 동일)

cv2.waitKey(0)  # 키 입력이 있을 때까지 대기
cv2.destroyAllWindows()  # 열려 있는 모든 OpenCV 창 닫기
