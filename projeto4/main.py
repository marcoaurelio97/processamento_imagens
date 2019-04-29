import cv2


def main():
    video = cv2.VideoCapture('dados_video.mp4')

    if not video.isOpened():
        print('Error')

    while video.isOpened():
        ret, frame = video.read()

        if ret:
            img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            ret, thresh = cv2.threshold(img, 150, 255, cv2.THRESH_BINARY_INV)

            thresh_filter = cv2.medianBlur(thresh, 21)

            contours, hierarchy = cv2.findContours(thresh_filter, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

            cv2.drawContours(frame, contours, -1, (255, 0, 0), 2)

            for contour in contours:
                x, y, w, h = cv2.boundingRect(contour)
                roi = frame[y:y + h, x:x + w]

                detector = cv2.SimpleBlobDetector_create()
                keypoints = detector.detect(roi)

                if len(keypoints) > 0:
                    cv2.putText(frame, str(len(keypoints)), (x + w - 55, y + h - 40),
                                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)

            cv2.imshow('Frame', frame)
        else:
            break

        # if cv2.waitKey(1) & 0xFF == ord('q'):
        #     break

    video.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
