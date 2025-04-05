import cv2
import numpy as np

def gExpr(c):
    cl = c / 255
    if c <= 10:
        return cl / 12.92
    return pow((cl+0.055)/1.055,2.4)


filePath = "./sheep.png"

endW = 92
endH = 56
#endW = 1920
#endH = 1080



img = cv2.imread(filePath)

grey = ['@', '%', '#', '*', '+', '=', '-', ':', '.', ' ']



rows,cols,_ = img.shape
end = np.zeros((endH, endW, 3), np.uint8)


ratioH = rows/endH
ratioW = cols/endW


#scaling picture
#for i in range(endH):
#    for j in range(endW):
#        end[i,j] = img[int(i * ratioH),int(j * ratioW)]

tmp = np.zeros((endH, endW, 3), np.float64)

#scaling with wages
for i in range(endH):
    for j in range(endW):
        for x in range(int(ratioW-1)):
            for y in range(int(ratioH-1)):
                tmp[i, j,:] += img[int(i * ratioH) + x,int(j * ratioW) + y, :]        
        
tmp[:,:,:] /= (ratioW-1) * (ratioH-1)
end = tmp



#ttt = end.copy()

end = np.where( end / 255 <= 0.04045, end / 255 / 12.92, np.power(( end / 255 + 0.055 ) / 1.055, 2.4))

x = end[:,:, 0] * 0.2126 + end[:, :, 1] * 0.7152 + end[:, :, 2] * 0.0722
end[:,:,0] = x
end[:,:,1] = x
end[:,:,2] = x

npend = np.array(end)
npend *= 2
end = npend
#for i in range(endH):
#    for j in range(endW):
#        # gamma = gExpr(end[i,j,0])*0.2126 + gExpr(end[i,j,1])*0.7152 + gExpr(end[i,j,2])*0.0722
#        end[i,j,:] = end[i,j,0] * 0.2126 + end[i,j,1] * 0.7152 + end[i,j,2] * 0.0722
#        # end[i,j] = gamma * 255


asciiRow = ""

for i in range(endH):
    for j in range(endW):
        asciiRow = asciiRow + grey[int(end  [i,j,0] * 10)] + " "
    print(asciiRow)
    asciiRow = ""


cv2.imshow(filePath, img)
cv2.imshow("end", end)

#f not (end == ttt).all():
#    print(end, shape)
#print(end.shape, ttt.shape)  

cv2.waitKey(0)
cv2.destroyAllWindows()