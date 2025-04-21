# drone-station-detection-yolo5

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
