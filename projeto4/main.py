import cv2


def main():
    video = cv2.VideoCapture('dados_video.mp4')

    while video.isOpened():
        ret, frame = video.read()

        find_cubes(frame)

        cv2.imshow('Frame', frame)

        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    video.release()
    cv2.destroyAllWindows()


def find_cubes(frame):
    img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    ret, thresh = cv2.threshold(img, 150, 255, cv2.THRESH_BINARY)

    thresh_filter = cv2.medianBlur(thresh, 21)

    contours, hierarchy = cv2.findContours(thresh_filter, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    cv2.drawContours(frame, contours, -1, (255, 0, 0), 2)

    detector = cv2.SimpleBlobDetector_create()

    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        roi = frame[y:y + h, x:x + w]

        keypoints = detector.detect(roi)

        cv2.putText(frame, str(len(keypoints)), (x + w - 55, y + h - 40),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)


if __name__ == "__main__":
    main()
