import cv2

img = cv2.imread('picture.jpg')
width = 1920-1
height = 1080-1
for i in range(height//2):
    for j in range(1920):
        img[i][j] = img[height-i][j]

cv2.imwrite('picture1.jpg', img)