# Blur Face Cam

This is a simple Python project that automatically blurs faces in real time using a webcam.  
It helps protect privacy — the face becomes unrecognizable in the video preview and saved photos.  
Everything runs locally on your computer (no internet or cloud processing).

## Setup

Make sure you have Python installed.  
Create and activate a virtual environment (optional but recommended),
then install the required libraries:

```bash
pip install -r requirements.txt

This installs:
mediapipe (face detection)
opencv-python (camera and image processing)
numpy (math operations)

To run it type this in terminal
python blur_cam_facemesh.py