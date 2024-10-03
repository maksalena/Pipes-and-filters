# Pipes-and-Filters Video Processing Application

## Project Description
This project demonstrates the **pipes-and-filters pattern** for real-time video processing using Python and OpenCV. The application reads video streams from your webcam or a video file, processes the frames through a series of filters (Black and White, Mirror, Resize, and Edge Detection), and displays the processed frames in real-time.

## Features
- **Input**: Capture video frames from a webcam or video file.
- **Processing**: Apply multiple filters such as Black & White, Mirror, Resize, and Edge Detection to the video frames.
- **Output**: Display the processed video in real-time.

## Filters Implemented
1. **Black & White (Grayscale)**: Converts the video frames to grayscale.
2. **Mirror Effect**: Flips the video horizontally.
3. **Resize**: Resizes the video to a smaller scale.
4. **Edge Detection**: Applies Canny edge detection to highlight the edges.

## Requirements
- Python 3.x
- OpenCV (cv2) library

## Installation

Follow these steps to set up the environment and run the application:

1. **Install Python3**: Download and install the latest version of Python 3 from the official [website](https://www.python.org/downloads/).

2. **Verify Installation**: After installing Python 3, check if `python3` and `pip3` are correctly installed by running the following commands:
   ```bash
   python3 --version
   pip3 --version

3. **Create a Virtual Environment**: To isolate the project dependencies, create a virtual environment in your project directory:
   ```bash
   python3 -m venv .venv

4. **Activate the Virtual Environment**: Activate the virtual environment using the following command:
   ```bash
   source .venv/bin/activate
   
5. **Upgrade pip**: Make sure pip is updated to the latest version:
   ```bash
   pip3 install --upgrade pip
   
6. **Install OpenCV**: Install the OpenCV Python package using pip3:
   ```bash
   pip3 install opencv-python

## Running the Application

1. Navigate to the folder where main.py is located.
2. Run the application:
   ```bash
   python3 main.py
   
The application will start capturing video from your webcam (or video file if configured) and display the processed frames with the applied filters.

## Video file configuration

Chenge '0' to the path for your video file in line 73:
```python
video_pipe = VideoCapturePipe(0) # e.g "myVideo.mp4"
```

## How to Exit

To stop the application, press 'q' while the video window is active.

## Demo

You can find video demonstation [here](https://drive.google.com/file/d/1TuLyf4TApBMfBikHLjY15VazVKS3QBO0/view?usp=sharing).

## License

This project is licensed under the MIT License.
