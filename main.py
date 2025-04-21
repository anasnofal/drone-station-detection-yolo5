# USAGE

import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

import torch
from matplotlib import pyplot as plt
import numpy as np
import cv2
import argparse
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--path", required=True,help="path to input")
ap.add_argument("-m", "--model", required= True,help = " path to model" )
ap.add_argument("-o", "--output", default="output.mp4", help="Path to save annotated video")
args = vars(ap.parse_args())
#Loding the model 
model = torch.hub.load('ultralytics/yolov5', 'custom', path=args['model'], force_reload=True)
model.conf = 0.5  # confidence threshold (0-1)
model.iou = 0.5  # NMS IoU threshold (0-1)  
cap = cv2.VideoCapture(args['path'])
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

# Output video writer
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(args['output'], fourcc, fps, (width, height))

# Process video
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame)
    rendered_frame = np.squeeze(results.render())
    out.write(rendered_frame)

cap.release()
out.release()

print(f"[INFO] Output saved to: {args['output']}")
