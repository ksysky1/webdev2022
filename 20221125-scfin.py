import cv2
import numpy as np
import sys

from PIL import Image
import pytesseract

img = cv2.imread('u.jpg')
cv2.imshow('Original', img)
cv2.waitKey(0)

draw = img.copy()
# 그레이 스케일 변환 & 캐니 에지
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (3, 3), 0)
edged = cv2.Canny(gray, 75, 100)
win_name = 'Scanning...'
cv2.imshow(win_name, edged)
cv2.waitKey(0)

# 컨투어 찾기
cnts, h = cv2.findContours(edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
print(len(cnts))
cv2.drawContours(draw, cnts, -1, (0, 255, 0))
cv2.imshow(win_name, draw)
cv2.waitKey(0)

# 4개 꼭지점 찾기 (가장 큰 컨투어에서)
cnts = sorted(cnts, key=cv2.contourArea, reverse=True)
for c in cnts:
    print(c.shape)
    vertices = cv2.approxPolyDP(c, 0.01*cv2.arcLength(c, True), True)
    if len(vertices) == 4:
        print(vertices.shape)
        print(vertices)
        break

# 찾은 꼭지점 4X1X2 배열 -> 4X2로 변경
pts = vertices.reshape(4, 2)
print(pts.shape)
print(pts)
for x, y in pts:
    cv2.circle(draw, (x, y), 10, (0, 255, 0), -1)

cv2.imshow(win_name, draw)
cv2.waitKey(0)

sum = np.sum(pts, axis=1)
diff = np.diff(pts, axis=1)

topLeft = pts[np.argmin(sum)]  # x+y 최솟값
bottomRight = pts[np.argmax(sum)]  # x+y 최댓값
topRight = pts[np.argmin(diff)]  # x-y 최솟값
bottomLeft = pts[np.argmax(diff)]  # x-y 최댓값

# 변환 전 4개 좌표
pts1 = np.float32([topLeft, topRight, bottomRight, bottomLeft])

w1 = abs(bottomRight[0] - bottomLeft[0])
w2 = abs(topRight[0] - topLeft[0])
h1 = abs(topRight[1] - bottomRight[1])
h2 = abs(topRight[1] - bottomLeft[1])
width = max([w1, w2])
height = max([h1, h2])

# 변환 후 4개 좌표
pts2 = np.float32([[0, 0], [width - 1, 0], [width - 1, height - 1], [0, height - 1]])

# 변환행렬 계산
mtrx = cv2.getPerspectiveTransform(pts1, pts2)
# 원근 변환 적용
dst = cv2.warpPerspective(img, mtrx, (width, height))

cv2.imshow(win_name, dst)
cv2.imwrite("Clear.jpg", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
###### 여기까지 스캐너 기능

img = cv2.imread('Clear.jpg')

rimg90= cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
cv2.imwrite('ClearR1.jpg', rimg90)

rimg180 = cv2.rotate(img, cv2.ROTATE_180)
cv2.imwrite('ClearR2.jpg', rimg180)

rimg270 = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
cv2.imwrite('ClearR3.jpg', rimg270)
##### 여기까지 회전 기능

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
text = pytesseract.image_to_string(Image.open('Clear.jpg'), lang="kor")
print(text)

with open("Clear.txt", "w", encoding="utf8") as f:
    f.write(text)
    f.write("\n\n\n")
##### 여기까지 문자 인식 기능


img = cv2.imread('Clear.jpg')
cv2.namedWindow('image')
X = Y = -1
def on_mouse(event, x, y, flags, param):
    global X, Y

    if event == cv2.EVENT_LBUTTONDOWN:
        X, Y = x, y

    elif event == cv2.EVENT_MOUSEMOVE:
        if flags & cv2.EVENT_FLAG_LBUTTON:
            cv2.circle(img, (x, y), 3, (255, 0, 255), -1)
            cv2.imshow('image', img)
            X, Y = x, y

cv2.setMouseCallback('image', on_mouse, img)

cv2.imshow('image', img)
cv2.waitKey()

cv2.destroyAllWindows()
##### 여기까지 그림그리기 기능
