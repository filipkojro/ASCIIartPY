import cv2
import numpy as np

def gExpr(c):
    cl = c / 255
    if cl <= 0.04045:
        return cl / 12.92
    return pow((cl+0.055)/1.055,2.4)


filePath = "./sheep.png"

endW = 89
endH = 71

img = cv2.imread(filePath)

grey = ['@', '%', '#', '*', '+', '=', '-', ':', '.', ' ']


rows,cols,_ = img.shape

for i in range(rows):
    for j in range(cols):
        gamma = gExpr(img[i,j,0])*0.2126 + gExpr(img[i,j,1])*0.7152 + gExpr(img[i,j,2])*0.0722

        img[i,j] = gamma * 255


end = np.zeros((endH, endW, 3), np.uint8)

for i in range(endH):
    for j in range(endW):
        end[i,j] = img[int(i * rows / endH),int(j * cols/endW)]


asciiRow = ""

for i in range(endH):
    for j in range(endW):
        asciiRow = asciiRow + grey[int(end[i,j,0] / 25.6)] + " "
    print(asciiRow)
    asciiRow = ""


cv2.imshow("Sheep", img)
cv2.imshow("end", end)

cv2.waitKey(0)
