import cv2 

print("OpenCV version:")  # 안내 문구 출력
print(cv2.__version__)  # 설치된 OpenCV 버전 확인

img = cv2.imread("images_opencv/bts-02.jpg")  # 이미지를 BGR 컬러로 읽어오기
print("image shape: {} pixels".format(img.shape))  # (높이, 너비, 채널) 형태 출력
print("width: {} pixels".format(img.shape[1]))  # 이미지 너비(가로 픽셀 수)
print("height: {} pixels".format(img.shape[0]))  # 이미지 높이(세로 픽셀 수)
print("channels: {}".format(img.shape[2]))  # 색상 채널 수(3: B, G, R)

cv2.imshow("bts", img)  # "bts" 창에 원본 이미지 표시

# 순서 b, g, r 순서를 지켜야 함(0~255)
(b, g, r) = img[0, 0]  # (y=0, x=0) 위치 픽셀의 색상값을 B, G, R 순서로 꺼내기
print("Pixel at (0, 0) - Red: {}, Green: {}, Blue: {}".format(r,
g, b))  # 해당 픽셀의 R, G, B 값 출력

# 키 입력이 있을 때까지 대기
cv2.waitKey(0)  

# 세로 50~100, 가로 200~400 : px의 절대적 위치
dot = img[50:100, 200:400]  # 이미지에서 [y 50~100, x 200~400] 영역만 잘라내기(슬라이싱)
cv2.imshow("Dot", dot)  # 잘라낸 영역을 "Dot" 창에 표시

# 키 입력이 있을 때까지 대기
cv2.waitKey(0)  

#(b, g, r)
img[50:100, 200:400] = (255, 0, 0)  # 해당 영역을 파란색(B=255)으로 채우기

img[100:200, 200:400] = (100, 100, 0)  # 아래 영역을 청록 계열(B=100, G=100)로 채우기

cv2.imshow("bts - dotted", img)  # 색을 칠한 이미지를 "bts - dotted" 창에 표시

cv2.waitKey(0)  # 키 입력이 있을 때까지 대기
cv2.destroyAllWindows()  # 열려 있는 모든 OpenCV 창 닫기
