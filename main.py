# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


#img = cv2.imread('picture.jpg')
#for i in range(1000):
#    for j in range(1000):
#        img[i][j] = [0, 255, 0]

#x1, y1 = 1100, 650
#x2, y2 = 1380, 850
#color = [0, 255, 0]
#width = 5

#x, y = 1200, 640
#font_size = 2;
#font = cv2.FONT_HERSHEY_SIMPLEX
#text = 'car'


#img = cv2.putText(img, text, (x,y), font, font_size, color, width)

#img = cv2.rectangle(img, (x1,y1),(x2,y2), color, width)
#cv2.imwrite('picture1.jpg', img)


import cv2
import random

size = (2560 // 2, 1440 // 2)
#codec = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
codec = cv2.VideoWriter_fourcc(*'mp4v')
writer = cv2.VideoWriter('output.mp4', codec, 25, size)

cap = cv2.VideoCapture('cars.mp4')

#codec = cv2.VideoWriter_fourcc(*'MJPG')
#out = cv2.VideoWriter('output.avi', codec, 5, size)

while cap.isOpened():
    print('.', end='')

    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.resize(frame, size)
    for i in range(200):
        for j in range(200):
            frame[i][j] = [random.randint(0,255), random.randint(0,255), random.randint(0,255)]
    writer.write(frame)

cap.release()
writer.release()