Readme
-------------------------------
Image Search in Video
This Python script enables the search for a specific image within a video file using template matching with OpenCV.
Description
The script processes a video file frame by frame to find instances of a given template image. It uses OpenCV's template matching capabilities to locate the image within each frame and draws a rectangle around the found instances.
Prerequisites
Before running this script, you need to have Python installed on your system along with the OpenCV library. You can install OpenCV using pip:
```shell
pip install opencv-python
Usage
To use this script, you need to provide the path to the video file and the template image. Replace the placeholder paths in the script with the actual paths to your files.

Python
video_path = 'path_to_your_video.mp4'
template_path = 'path_to_your_template_image.png'

Run the script from the command line:
python image_search_in_video.py

How It Works
The script reads the video and template image into memory. It then converts each frame of the video to grayscale and performs template matching to find the template image. If a match is found with a confidence above the set threshold, it draws a green rectangle around the detected area.
Contributing
Contributions to this project are welcome. Please fork the repository and submit a pull request with your changes.

References:
https://docs.python.org/3/reference/index.html
https://pythonprinciples.com/reference/
https://www.w3schools.com/python/python_reference.asp

