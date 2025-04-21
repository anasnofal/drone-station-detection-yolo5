# drone-station-detection-yolo5



YOLOv5 - Drone Station Detection (Hyper-Tuned Model)
This repository contains a custom YOLOv5 model specifically fine-tuned to detect drone stations. The model has been optimized to accurately identify drone stations in various environments, providing robust and reliable performance.

Key Features:
YOLOv5 Architecture: A state-of-the-art object detection model based on YOLOv5.

Hyper-Tuned: The model has been fine-tuned with specific datasets to enhance accuracy and minimize false positives for drone station detection.

Fast Inference: Leveraging the power of YOLOv5, this model delivers real-time detection with high precision.


how to run : 
Prerequisites
you must have:
docker

1-Open command line (or terminal), clone the reopsitory, then navigate to repo directory
```
cd drone-station-detection-yolo5
```

2 - build the docker image 
```
docker build -t drone .
```

3-then you can run the program
```
docker run --rm -it -v $(pwd):/app drone python main.py --path 'WhatsApp Video 2022-11-28 at 5.41.40 AM.mp4' --model 'best.pt' --output "output.mp4"
```
4- you will find an output.mp4 where you can see the result. 
