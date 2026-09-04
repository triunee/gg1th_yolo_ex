import cv2 

print("OpenCV version:")  # 안내 문구 출력
print(cv2.__version__)  # 설치된 OpenCV 버전 확인

img = cv2.imread("images_opencv/bts-02.webp")  # 이미지를 BGR 컬러로 읽어오기
print("image shape: {} pixels".format(img.shape))  # (높이, 너비, 채널) 형태 출력
print("width: {} pixels".format(img.shape[1]))  # 이미지 너비(가로 픽셀 수)
print("height: {} pixels".format(img.shape[0]))  # 이미지 높이(세로 픽셀 수)
print("channels: {}".format(img.shape[2]))  # 색상 채널 수(3: B, G, R)

cv2.imshow("bts", img)  # "bts" 창에 원본 이미지 표시

# b, g, r 순서 지키기
(b, g, r) = img[0, 0]  # (y=0, x=0) 픽셀의 색상값을 B, G, R 순서로 꺼내기
print("Pixel at (0, 0) - Red: {}, Green: {}, Blue: {}".format(r,
g, b))  # 해당 픽셀의 R, G, B 값 출력

# 높이, 너비
img[100:150, 50:100] = (0, 0, 255)  # [y 100~150, x 50~100] 영역을 빨간색(R=255)으로 채우기

#cv2.rectangle(img, (좌, 상), (우, 하), (b, g, r), 선굵기)
cv2.rectangle(img, (150, 100), (200, 150), (255, 0, 0), 5)  # 파란색 사각형 테두리 그리기(선굵기 5)

#cv2.circle(img, (좌, 상), 반지름, (b, g, r), 선굵기) # -1 모두 채움
cv2.circle(img, (275, 125), 25, (0, 255, 255), -1)  # 중심(275,125), 반지름 25인 노란색 원을 색으로 채우기

#cv2.line(img, (좌, 상), (우, 하), (b, g, r), 굵기)
cv2.line(img, (350, 100), (400, 150), (255, 0, 0), 5)  # (350,100)~(400,150)을 잇는 파란색 선 그리기

#cv2.putText(img, '문자열', 시작위치(좌, 상), font_style, 폰트크기, (b, g, r), 폰트굵기)
cv2.putText(img, 'Hello~ BTS', (450, 150), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 4)  # 흰색 텍스트 그리기

cv2.imshow("bts - draw", img)  # 도형/텍스트를 그린 이미지를 "bts - draw" 창에 표시

cv2.waitKey(0)  # 키 입력이 있을 때까지 대기
cv2.destroyAllWindows()  # 열려 있는 모든 OpenCV 창 닫기
