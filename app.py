import cv2

vid = cv2.VideoCapture(0)

width = int(vid.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(vid.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(vid.get(cv2.CAP_PROP_FPS))

writer = cv2.VideoWriter("test_video.mp4", cv2.VideoWriter_fourcc(*'DIVX'), fps, (width, height))

while(True):
    ret, frame = vid.read()

    editedFrame = cv2.putText(frame, "COOOO NIEMOŻLIWE", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)

    cv2.imshow("Webcam Preview", editedFrame)
    writer.write(editedFrame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

vid.release()
writer.release()
cv2.destroyAllWindows()