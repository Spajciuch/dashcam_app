import cv2

vid = cv2.VideoCapture(0)

width = int(vid.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(vid.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(vid.get(cv2.CAP_PROP_FPS))

writer = cv2.VideoWriter("test_video.mp4", cv2.VideoWriter_fourcc(*'DIVX'), fps, (width, height))

while(True):
    ret, frame = vid.read()

    cv2.putText(frame, "COOOO NIEMOŻLIWE")

    cv2.imshow("frame", frame)
    writer.write(frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

vid.release()
writer.release()
cv2.destroyAllWindows()