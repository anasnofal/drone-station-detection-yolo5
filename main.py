import torch
from matplotlib import pyplot as plt
import numpy as np
import cv2
#Loding the model 
model = torch.hub.load('ultralytics/yolov5', 'custom', path='D:/drone/best.pt', force_reload=True)
model.conf = 0.9  # confidence threshold (0-1)
model.iou = 0.6  # NMS IoU threshold (0-1)  
cap = cv2.VideoCapture(0)
while cap.isOpened():
    ret, frame = cap.read()
    
    # Make detections 
    results = model(frame)
    cv2.imshow('YOLO', np.squeeze(results.render()))
    
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()