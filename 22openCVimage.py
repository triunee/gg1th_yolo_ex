# OpenCV 이미지 읽기, 쓰기, 표시

import cv2  

print("OpenCV version:")  # 안내 문구 출력
print(cv2.__version__)  # 설치된 OpenCV 버전 확인

img = cv2.imread("images_opencv/bts-01.jpg")  # 이미지를 BGR 컬러로 읽어오기
print("image shape: {} pixels".format(img.shape))  # (높이, 너비, 채널) 형태 출력
print("width: {} pixels".format(img.shape[1]))  # 이미지 너비(가로 픽셀 수)
print("height: {} pixels".format(img.shape[0]))  # 이미지 높이(세로 픽셀 수)
print("channels: {}".format(img.shape[2]))  # 색상 채널 수(컬러는 3: B, G, R)

cv2.imshow("bts", img)  # "bts" 창에 원본 컬러 이미지 표시

# gray scale로 img 바꾸기
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # BGR 컬러 이미지를 흑백으로 변환

cv2.imshow("bts - gray", gray)  # "bts - gray" 창에 흑백 이미지 표시

# 이미지 파일로 HDD 지정 폴더에 쓰기
cv2.imwrite("images_opencv/bts-1_gray.jpg", gray)  # 흑백 이미지를 파일로 저장

# 아무키나 누를때까지 기다림
cv2.waitKey(0)  # 키 입력이 있을 때까지 대기

# 창 종료
cv2.destroyAllWindows()  # 열려 있는 모든 OpenCV 창 닫기
