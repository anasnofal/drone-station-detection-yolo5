# USAGE
# python einstein_face.py --path 0 for cam or video path
import torch
from matplotlib import pyplot as plt
import numpy as np
import cv2
import argparse
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--path", required=True,help="path to input")
args = vars(ap.parse_args())
#Loding the model 
model = torch.hub.load('ultralytics/yolov5', 'custom', path='D:/Python project/drone/best.pt', force_reload=True)
model.conf = 0.5  # confidence threshold (0-1)
model.iou = 0.5  # NMS IoU threshold (0-1)  
cap = cv2.VideoCapture(args['path'])
while cap.isOpened():
    ret, frame = cap.read()
    
    # Make detections 
    results = model(frame)
    cv2.imshow('YOLO', np.squeeze(results.render()))
    
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()