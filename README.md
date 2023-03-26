# Facial Recognition Project (Master)

This repository contains a Python script for performing facial recognition using OpenCV and face_recognition libraries. The script detects faces in a live video stream from a webcam or in images, encodes the faces, and compares them against a database of known faces to identify them.

## The code is divided into two files:

script.py: contains the main script for facial recognition using the webcam.
basic_test.py: contains a basic test of the face_recognition library with two images.

## Dependencies:
- Python 3.6+
- OpenCV 4.0+
- Numpy 1.16+
- face_recognition 1.3+

## Installation:

1. Clone this repository: git clone https://github.com/oskccy/facial-recognition.git.
2. Install the required dependencies using pip: pip install opencv-python numpy face_recognition.

## Usage:

To run the main script, navigate to the project directory and run the following command: python script.py.
The script will capture frames from the webcam and display them in a window. Any detected faces will be identified with a name label, if it matches any of the known faces in the "imagesAttendance" directory.

To test the face recognition functionality using two images, run python basic_test.py. The script will compare the faces in the two images and print out whether they match or not, along with a confidence score.
Contributing
If you would like to contribute to this project, please submit a pull request with your changes. I welcome all contributions, including bug fixes and feature enhancements.

## License:

- This project is licensed under the MIT License. See the LICENSE file for more details.



