import cv2  
import numpy as np  # 마스크 배열 생성을 위한 numpy 불러오기

print("OpenCV version:")  # 안내 문구 출력
print(cv2.__version__)  # 설치된 OpenCV 버전 확인

img = cv2.imread("images_opencv/bts-02.jpg")  # 이미지를 BGR 컬러로 읽어오기
print("image shape: {} pixels".format(img.shape))  # (높이, 너비, 채널) 형태 출력
print("width: {} pixels".format(img.shape[1]))  # 이미지 너비(가로 픽셀 수)
print("height: {} pixels".format(img.shape[0]))  # 이미지 높이(세로 픽셀 수)
print("channels: {}".format(img.shape[2]))  # 색상 채널 수(3: B, G, R)

(height, width) = img.shape[:2]  # 높이, 너비만 분리해서 저장
center = (width // 2, height // 2)  # 이미지 중심 좌표

cv2.imshow("bts", img)  # "bts" 창에 원본 이미지 표시

mask = np.zeros(img.shape[:2], dtype = "uint8")  # 8bit로 부호없 정수 표현 → 전부 0(검정)인 마스크 생성
# print(mask)  # 마스크 배열 내용 확인
# #cv2.circle(mask, center, 반지름, (255, 255, 255), -1)
mask = cv2.circle(mask, center, 200, (255, 255, 255), -1)  # -1 : 색상으로 면을 채움 → 중심에 흰색 원 그리기
# cv2.circle(mask, center, 200, (255, 255, 255), -1)  # -1 : 색상으로 면을 채움

cv2.imshow("mask", mask)  # 만든 마스크를 "mask" 창에 표시

# # mask적용, bitwise 연산 : not, and, or, xor
# # 참고 : https://docs.opencv.org/3.4/d0/d86/tutorial_py_image_arithmetics.html
masked = cv2.bitwise_and(img, img, mask = mask)  # 마스크의 흰색 영역만 원본 이미지를 남기고 나머지는 검정 처리
cv2.imshow("bts with mask", masked)  # 마스킹 결과를 표시

cv2.waitKey(0)  # 키 입력이 있을 때까지 대기
cv2.destroyAllWindows()  # 열려 있는 모든 OpenCV 창 닫기
