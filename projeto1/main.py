import cv2
import glob
import numpy as np

watermark = cv2.imread("facens2.png")
watermark = cv2.cvtColor(watermark, cv2.COLOR_BGR2BGRA)
width = 640
height = 480
tam_borda = 20
alpha = 0.6
images = []

for file in glob.glob("imagens/*.jpg") :
    img = cv2.imread(file)
    img = cv2.resize(img, (width, height))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)

    overlay = np.zeros((img.shape[0], img.shape[1], 4), dtype="uint8")
    overlay[img.shape[0] - watermark.shape[0] : img.shape[0], 0 : watermark.shape[1]] = watermark
    cv2.addWeighted(overlay, alpha, img, 1.0, 0, img)
    
    img = cv2.copyMakeBorder(img, tam_borda, tam_borda, tam_borda, tam_borda, cv2.BORDER_CONSTANT, value=[0, 0, 0])
    images.append(img)

fim = False
idx1 = 0
idx2 = 0

def fadeIn (img1, img2, len=20) :
    for IN in range(0, len) :
        fadein = IN/float(len)
        dst = cv2.addWeighted(img1, 1-fadein, img2, fadein, 0)
        cv2.imshow('window', dst)
        key = cv2.waitKey(50)

        if (key == 113) :
            return True
            
    return False

cv2.imshow('window', images[idx1])
cv2.waitKey(2000)

while (True) :
    for i in range(0, len(images)) :
        idx1 = i
        idx2 = i + 1

        if (i == len(images) - 1) :
            idx2 = 0

        fim = fadeIn(images[idx1], images[idx2], 20)

        if (fim) :
            break
        
        key = cv2.waitKey(2000)

        if (key == 113) :
            fim = True
            break
    if (fim) :
        break

cv2.destroyAllWindows()