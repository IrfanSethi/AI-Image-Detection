# Image Detecting Robot - Project 1

## Introduction
This project is an introductory exploration into image detection using Google Cloud Vision API. The goal is to detect and localize objects within images, providing bounding box coordinates and confidence scores for each detected object. This project serves as a foundation for understanding how machine learning APIs can be integrated into Python applications for computer vision tasks.

## Features
- Object localization in images
- Confidence scoring for detected objects
- Bounding box extraction for each object
- Console output of detected objects and their properties

## Screenshot
![Screenshot](Screenshot%202025-08-10%20142203.png)

## Installation
1. Clone this repository to your local machine.
2. Install the required Python packages:
   ```bash
   pip install google-cloud-vision
   ```
3. Obtain Google Cloud Vision API credentials and place the JSON file in the project directory.
4. Update the image and credentials path in `week1.py` if necessary.

## Usage
1. Place your test image in the appropriate directory (default: project root).
2. Run the script:
   ```bash
   python week1.py
   ```
3. View the console output for detected objects and their bounding boxes.

## Technologies
- Python 3
- Google Cloud Vision API
- Google Auth

## Why This Project?
This project was created to test the waters of image detection and to gain hands-on experience with cloud-based computer vision APIs. It provides a simple yet effective way to understand the basics of object detection and how to integrate external machine learning services into Python workflows.
