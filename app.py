import cv2, time, os
from datetime import datetime

# Purging local storage after specified time ---

# Variables necessary for file deletion

directory = "videos"
expiration = 1

os.chdir(os.path.join(os.getcwd(), directory))
fileList = os.listdir()
currentTime = time.time()
day = 86400

# Loop for deleting files 

for i in fileList:
    fileLocation = os.path.join(os.getcwd(), i)
    fileTime = os.stat(fileLocation).st_mtime

    if(fileTime < currentTime - day*expiration):
        print(f"[expired] Removed: {i}")
        os.remove(fileLocation)

# Recording video part ---

vid = cv2.VideoCapture(0)

# Video capture parameters
width = int(vid.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(vid.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(vid.get(cv2.CAP_PROP_FPS))

# Timestamp settings
position = (400, 470)
font = cv2.FONT_HERSHEY_DUPLEX
scale = .7
color = (255,255,255)
thickness = 2
lineType = cv2.LINE_AA

writer = cv2.VideoWriter(f"{datetime.now().strftime('%d.%m.%Y - %H.%M.%S')}.mp4", cv2.VideoWriter_fourcc(*'mp4v'), fps, (width, height))

while(True):
    ret, frame = vid.read()

    now = datetime.now()
    current_time = now.strftime("%d.%m.%Y %H:%M:%S")

    editedFrame = cv2.putText(frame, current_time, position, font, scale, color, thickness, lineType)

    # cv2.imshow("Webcam Preview", editedFrame)
    writer.write(editedFrame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

vid.release()
writer.release()
cv2.destroyAllWindows()
