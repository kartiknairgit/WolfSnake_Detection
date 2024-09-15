import cv2
import numpy as np
from datetime import datetime, timedelta

def add_alert_overlay(frame, text, progress):
    overlay = frame.copy()
    
   
    height, width = frame.shape[:2]
    
   
    cv2.rectangle(overlay, (0, height - 80), (width, height), (0, 0, 255), -1)
    
    alpha = 0.6 
    frame = cv2.addWeighted(overlay, alpha, frame, 1 - alpha, 0)
    
    
    text_x = 20  
    text_y = height - 30  

    
    cv2.putText(frame, text, (text_x, text_y), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
    
    center_x, center_y = width - 50, height - 40  
    radius = 30
    thickness = 5
    max_angle = int(progress * 360) 
    
    
    cv2.ellipse(frame, (center_x, center_y), (radius, radius), 270, 0, max_angle, (255, 255, 255), thickness)
    
    return frame

cap = cv2.VideoCapture(0)
fgbg = cv2.createBackgroundSubtractorMOG2(history=500, varThreshold=25, detectShadows=True)

motion_start_time = None
alert_shown = False

while True:
    ret, frame = cap.read()
    
    if not ret:
        break

    fgmask = fgbg.apply(frame)
    _, thresh = cv2.threshold(fgmask, 200, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    motion_detected = False

    for contour in contours:
        if cv2.contourArea(contour) > 500: 
            (x, y, w, h) = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            motion_detected = True
            break  

    current_time = datetime.now()

    if motion_detected:
        if motion_start_time is None:
            motion_start_time = current_time
        elapsed_time = (current_time - motion_start_time).total_seconds()
        
        if elapsed_time > 4:
            frame = add_alert_overlay(frame, "MOTION DETECTED", 1.0)  # Full progress circle after 4 seconds
        else:
            progress = elapsed_time / 4.0
            frame = add_alert_overlay(frame, "MOTION DETECTING...", progress)
    else:
        motion_start_time = None

    cv2.imshow('Motion Detection', frame)

    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()