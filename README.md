# Motion Detection Using OpenCV and Background Subtraction

## Overview

This project demonstrates a simple motion detection system using OpenCV's background subtraction method. The system captures video feed from a webcam, processes each frame to detect motion, and highlights areas where motion is detected. The primary objective is to detect motion in real-time using the MOG2 (Mixture of Gaussians) algorithm, which effectively differentiates between the foreground (moving objects) and the background.

## Table of Contents

- [Overview](#overview)
- [Requirements](#requirements)
- [Installation](#installation)
- [How It Works](#how-it-works)
- [Code Explanation](#code-explanation)
- [Usage](#usage)
- [Troubleshooting](#troubleshooting)
- [Possible Enhancements](#possible-enhancements)
- [Conclusion](#conclusion)
- [References](#references)

## Requirements

To run this project, you need the following dependencies:

- Python 3.x
- OpenCV
- NumPy

You can install the required packages using the provided `requirements.txt` file.

### `requirements.txt`

```plaintext
numpy==2.1.0
opencv-python==4.10.0.84
opencv-python-headless==4.10.0.84
```

### `installation`

#### Clone the repository

```
git clone https://github.com/yourusername/motion-detection-opencv.git
cd motion-detection-opencv
```

### Set Up a Virtual Environment (Optional)

It is recommended to create a virtual environment to manage your project's dependencies separately. You can create and activate a virtual environment using the following commands:

```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

### How It Works

This motion detection system works by analyzing the difference between the current frame and a background model created from previous frames. The background model is updated over time, allowing the system to adapt to changing conditions (e.g., lighting changes).

### Key Concepts

- **Background Subtraction**: This technique is used to separate the moving objects (foreground) from the static parts of the scene (background).
- **MOG2 Algorithm**: An advanced background subtraction algorithm that handles changes in lighting and shadows, making it suitable for real-world applications.

### Motion Detection

The system checks if any contours (i.e., moving objects) are larger than a specified area. If so, it marks the motion as detected and draws a rectangle around the moving object.

### Display the Results

The processed frame is displayed, and if motion is detected, the current timestamp is printed.

### Exit the Program

The program exits when the user presses the 'q' key.

## Troubleshooting

- **Webcam Not Detected**: If the webcam is not detected, ensure that it is connected properly and that the correct index (0 for default) is used in `cv2.VideoCapture()`.
- **No Motion Detected**: If no motion is detected, try adjusting the `varThreshold` parameter in the MOG2 algorithm or ensure that there is significant movement in front of the camera.
- **High CPU Usage**: Real-time video processing can be CPU-intensive. To reduce CPU usage, consider lowering the resolution of the webcam feed or optimizing the code further.

## Possible Enhancements

Here are some suggestions for enhancing the motion detection system:

- **Recording Video on Motion Detection**: Automatically start recording a video when motion is detected and save it to the disk.
- **Email Notifications**: Send an email notification with an image attached when motion is detected.
- **Multiple Camera Support**: Extend the system to support multiple cameras for broader area coverage.
- **Face Detection Integration**: Combine the motion detection with face detection to identify people in the frame.

## Conclusion

This project provides a basic yet functional motion detection system using OpenCV. The MOG2 algorithm allows for effective background subtraction, enabling the detection of moving objects in real-time. With potential enhancements, this system could be adapted for various real-world applications, such as security systems, smart surveillance, and more.

## References

- [OpenCV Documentation](https://docs.opencv.org/)
- [NumPy Documentation](https://numpy.org/doc/)
- [Real-time Object Detection with Background Subtraction](https://www.pyimagesearch.com/2016/09/21/ball-tracking-with-opencv/)
