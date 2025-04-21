FROM python:3.10-slim

# Install OS packages
RUN apt-get update && apt-get install -y \
    git \
    libgl1 \
    ffmpeg \
    libsm6 \
    libxext6 \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Install Python build tools
RUN pip install --upgrade pip setuptools wheel cython

# Install core Python dependencies
RUN pip install torch torchvision torchaudio matplotlib opencv-python numpy

# Clone YOLOv5 manually and install its requirements
RUN git clone https://github.com/ultralytics/yolov5.git
WORKDIR /app/yolov5
RUN pip install -r requirements.txt
RUN pip uninstall -y opencv-python
RUN pip install opencv-python-headless


# Copy your own script(s) into the container
WORKDIR /app
COPY . .

# Set the default command
CMD ["python", "your_script.py"]
