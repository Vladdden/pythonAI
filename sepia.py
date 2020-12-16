#outputRed = (inputRed * .393) + (inputGreen *.769) + (inputBlue * .189)
#outputGreen = (inputRed * .349) + (inputGreen *.686) + (inputBlue * .168)
#outputBlue = (inputRed * .272) + (inputGreen *.534) + (inputBlue * .131)


import cv2

def Sepia(color):
    outputRed = int((color[0] * .393) + (color[1] * .769) + (color[2] * .189))
    outputGreen = int((color[0] * .349) + (color[1] * .686) + (color[2] * .168))
    outputBlue = int((color[0] * .272) + (color[1] * .534) + (color[2] * .131))
    if (outputRed>255):
        outputRed=255
    if (outputGreen > 255):
        outputGreen=255
    if (outputBlue>255):
        outputBlue=255
    return [outputRed, outputGreen, outputBlue]


img = cv2.imread('picture.jpg')
width = 1920-1
height = 1080-1
for i in range(height):
    for j in range(width):
        img[i][j] = Sepia(img[i][j])

cv2.imwrite('picture2.jpg', img)

for i in range(height):
    for j in range(width):
        new_color = sum(img[i][j])/3
        img[i][j] = [new_color, new_color, new_color]

cv2.imwrite('picture3.jpg', img)
