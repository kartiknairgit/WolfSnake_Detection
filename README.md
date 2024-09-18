# Motion Detection Using OpenCV and Background Subtraction

## Overview

This project demonstrates an advanced motion detection system using OpenCV's background subtraction method. The system captures video feed from a webcam, processes each frame to detect motion, and highlights areas where motion is detected. It also includes a visual alert overlay that activates when continuous motion is detected for a certain period.

## Requirements

- Python 3.x
- OpenCV
- NumPy

Install the required packages using the provided `requirements.txt` file:

```
numpy==2.1.0
opencv-python==4.10.0.84
opencv-python-headless==4.10.0.84
```

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/motion-detection-opencv.git
   cd motion-detection-opencv
   ```

2. (Optional) Set up a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the script:

```bash
python motion_detection.py
```

- The webcam feed will open in a new window. 
- Motion will be highlighted with green rectangles. 
- If continuous motion is detected for more than 4 seconds, an alert overlay will appear.
- Press 'q' to exit the program.

## How It Works

1. Capture video feed from the webcam.
2. Apply background subtraction using MOG2 algorithm.
3. Threshold the result to create a binary mask.
4. Find contours in the binary mask.
5. Analyze contours to detect significant motion.
6. If motion is detected continuously, activate the alert overlay.
7. Display the processed frame with motion highlights and alert overlay (if active).

## Troubleshooting

- **Webcam Not Detected**: Ensure the webcam is properly connected and the correct index is used in `cv2.VideoCapture()`.
- **No Motion Detected**: Adjust the `varThreshold` parameter in the MOG2 algorithm or ensure significant movement in front of the camera.
- **High CPU Usage**: Consider lowering the webcam feed resolution or optimizing the code further.

## Possible Enhancements

- Recording Video on Alert
- Remote Notifications
- Multiple Camera Support
- AI-powered Object Recognition

## Conclusion

This project provides an advanced motion detection system using OpenCV, featuring real-time processing, visual motion highlighting, and an alert overlay for continuous motion detection. It serves as a solid foundation for various applications in security, surveillance, and home automation.

## References

- [OpenCV Documentation](https://docs.opencv.org/)
- [NumPy Documentation](https://numpy.org/doc/)
- [Python datetime Documentation](https://docs.python.org/3/library/datetime.html)
