import cv2  # OpenCV 라이브러리 불러오기

print("OpenCV version:")  # 안내 문구 출력
print(cv2.__version__)  # 설치된 OpenCV 버전 확인

# 이미지 읽어오기
img = cv2.imread("images_opencv/bts-01.jpg")  # 지정 경로의 이미지를 BGR 컬러로 읽어 numpy 배열로 저장
# gray scale로 변환
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # BGR 컬러 이미지를 흑백(그레이스케일)으로 변환

# 이미지 화면에 보이기
cv2.imshow("bts", img)  # "bts" 창에 원본 컬러 이미지 표시
cv2.imshow("bts - gray", gray)  # "bts - gray" 창에 흑백 이미지 표시

cv2.waitKey(0)  # 키보드 아무키나 누를 때까지 기다림
cv2.destroyAllWindows()  # 열려 있는 모든 OpenCV 창 닫기
