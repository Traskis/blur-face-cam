English — project overview

Automatic Real-Time Face Blurring

This project implements a Python-based tool
that automatically blurs a person’s face while
taking photos or recording video in real time.
The goal is to protect privacy by making faces
unrecognizable both during live preview and in saved images.

Technologies used:
Python, OpenCV, MediaPipe FaceMesh, NumPy.

The application continuously reads frames from the camera,
detects faces, builds a face contour, and applies a strong blur
only to that region, leaving the rest of the image intact.
Pressing c saves the blurred image, while q closes the program.
All processing happens locally on the computer, so no images
are sent to external servers.

------------------------------------------------------------------------

###  Install dependencies using requirements.txt

This project includes a file called **requirements.txt**.  
It contains a list of Python libraries that the project needs.

You do NOT install them one by one.  
You install everything with one command.

First make sure your virtual environment(venv) is active, then run:

```bash
pip install -r requirements.txt