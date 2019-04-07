import cv2
import numpy as np

def main() :
    data = np.array([
        [1,1,1,0,1,1,1,1,1,1],
        [1,1,1,0,1,1,1,1,1,1],
        [1,1,0,0,1,1,1,1,1,1],
        [0,0,0,0,1,1,1,1,1,1],
        [0,0,0,0,1,1,1,0,1,1],
        [0,1,1,1,1,1,1,1,1,1],
        [0,0,0,1,1,1,1,1,1,0],
        [0,0,0,1,1,1,1,1,1,0],
        [0,0,0,1,1,1,1,1,1,0],
        [0,0,0,1,1,1,1,1,1,0]
        ], dtype = np.uint8
    )

    quadrados = np.zeros((10,10), dtype=np.uint8)
    ele = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))

    print('\nElemento\n')
    print(ele)

    plotImg(data, 'Imagem', 50)

    print('\n\nOriginal\n')
    print(data)

    count = erosao(data, ele, quadrados)

    print('\n\nQuadrados')
    print(quadrados)

    print('\n\nQuantidade de quadrados: {}'.format(count))

    plotImg(quadrados, 'Erosão', 50)
        
    cv2.waitKey()
    cv2.destroyAllWindows()

def erosao(data, ele, quadrados) :
    count = 0
    j = 3
    x = 3

    for w in range(len(data[0])) :
        for i in range(len(data[0])) :
            if (j <= len(data[0])) :
                if (np.array_equal(data[w:x, i:j], ele)) :
                    count += 1
                    data[w:x, i:j].fill(0)
                    quadrados[w:x, i:j].fill(1)
            else :
                break
            
            j += 1
        x += 1
        j = 3

    return count

def plotImg(img, windowName, tam):
    newimg = np.zeros((img.shape[0]*tam, img.shape[1]*tam), np.uint8)
    for i in range(img.shape[0]) :
        for j in range(img.shape[1]) :
            tam = newimg.shape[0]/img.shape[0]
            radius = int(tam/2)
            x = int((i*tam) + (tam/2))
            y = int((j*tam) + (tam/2))

            if img[i, j] == 1:
                color = 255
            else:
                color = 0

            cv2.circle(newimg, (y, x), radius, (color, color, color), -1)

    ret,thresh1 = cv2.threshold(newimg, 0, 255, cv2.THRESH_BINARY_INV)
    img = np.array(thresh1)
    cv2.imshow(str(windowName), thresh1)

if __name__ == "__main__" :
    main()
