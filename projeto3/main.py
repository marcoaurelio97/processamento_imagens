import cv2
import os


def main():
    img_original = cv2.imread('dados.jpg')
    img = cv2.cvtColor(img_original, cv2.COLOR_BGR2GRAY)

    ret, thresh = cv2.threshold(img, 250, 255, cv2.THRESH_BINARY_INV)

    thresh_filter = cv2.medianBlur(thresh, 21)

    contours, hierarchy = cv2.findContours(thresh_filter, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    cv2.drawContours(img_original, contours, -1, (255, 0, 0), 2)

    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        roi = img_original[y:y+h, x:x+w]
        # cv2.imwrite('dado_recortado.jpg', roi)

        # dado = cv2.imread('dado_recortado.jpg', cv2.IMREAD_GRAYSCALE)

        detector = cv2.SimpleBlobDetector_create()
        keypoints = detector.detect(roi)

        if len(keypoints) > 0:
            cv2.putText(img_original, str(len(keypoints)), (x+w-55, y+h-40),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)

    cv2.imshow('Dados', img_original)

    # os.remove('dado_recortado.jpg')

    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
