Project overview

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
