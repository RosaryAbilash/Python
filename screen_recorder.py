import cv2
import numpy as np
import pyautogui
import time

screen_size = (1980, 1080)

# Videowriter for screenshots
fourcc = cv2.VideoWriter_fourcc(*"XVID")
out = cv2.VideoWriter("output3.mp4", fourcc, 20.0, (screen_size))

# change your frames per second
fps = 30
prev = 0

while True:
    time_elapsed = time.time() - prev
    # Taking Screenshots
    img = pyautogui.screenshot()

    if time_elapsed > 1.0/fps:
        prev = time.time()
        # putting Screenshots in array
        frames = np.array(img)
        # Colors for video
        frames = cv2.cvtColor(frames, cv2.COLOR_BGR2RGB)
        # Convert Screenshots to video
        out.write(frames)

    cv2.waitKey(40)

cv2.destroyAllWindows()
out.release()



# packages Required
# OpenCV, pyautogui,numpy, time, pillow