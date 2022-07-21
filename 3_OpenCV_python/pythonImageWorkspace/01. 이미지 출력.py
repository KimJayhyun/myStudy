import cv2
path = "C:/Users/User1/Desktop/code/gitFolder/myStudy/3_OpenCV_python/Data"

#==========================================================================================================================#

print(cv2.__version__)

#==========================================================================================================================#

# 해당 경로의 파일 읽어오기
img = cv2.imread(path + '/img.jpg')

# test 라는 window에 img 표시
cv2.imshow('test', img)

# 지정된 ms동안 사용자 키 입력 대기(0은 계속 대기)
# 누른 키의 ASCII Code 반환
key = cv2.waitKey(0)

print(key)

cv2.destroyAllWindows()

#==========================================================================================================================#

### 읽기 옵션 ###

## 1. cv2.IMREAD_COLOR
# 컬러 이미지, 투명 영역은 무시 (기본값)

## 2. cv2.IMREAD_GRAYSCALE
# 흑백 이미지

## 3. cv2.IMREAD_UNCHANGED
# 투명 영역까지 포함

img_color = cv2.imread(path + '/img.jpg', cv2.IMREAD_COLOR)
img_gray = cv2.imread(path + '/img.jpg', cv2.IMREAD_GRAYSCALE)
img_unchange = cv2.imread(path + '/img.jpg', cv2.IMREAD_UNCHANGED)

cv2.imshow('color', img_color)
cv2.imshow('gray', img_gray)
cv2.imshow('unchange', img_unchange)

cv2.waitKey(0)
cv2.destroyAllWindows()

#==========================================================================================================================#

### Shape ###
# 이미지의 height와 wigth, channel 정보

img = cv2.imread(path + '/img.jpg')
print(img.shape)

