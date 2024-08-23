import cv2
import numpy as np
from datetime import datetime  


cap = cv2.VideoCapture(0)
fgbg = cv2.createBackgroundSubtractorMOG2(history=500, varThreshold=25, detectShadows=True)

while True:
   
    ret, frame = cap.read()
    
   
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    fgmask = fgbg.apply(frame)
    _, thresh = cv2.threshold(fgmask, 200, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)


    motion_detected = False

    for contour in contours:
        if cv2.contourArea(contour) > 500: 
            (x, y, w, h) = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            motion_detected = True  


    if motion_detected:
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  
        print(f"Motion Detected at {current_time}")


    cv2.imshow('Motion Detection', frame)

    if cv2.waitKey(30) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()
