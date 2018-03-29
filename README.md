# Handwritten-Number-Recognition-With-Image-Segmentation
## Info About this repository
This Repository is aimed at reading handwritten images of numbers and identifying the number written in it using Image Segmentation and Convolutional Neural Networks

## Image Segmentation
The image segmentation algorithm uses contour tracing algorithm to separate the characters from a handwritten number.
For Example :- 1567 should be separated as 1, 5, 6 and 7.

## Digit Recognition
The digit recognition part is done by using a trained  Convolutional Neural Network. Details about training and dataset can be found in my repository https://github.com/SparshaSaha/Neural-Nets/blob/master/Coursera%20Handwritten%20digits%20Recognition/Coursera_digit_recog_using_CNN.ipynb .
This trained network is used to predict each digit and then ultimately predict the number.

## Segmentation API for each number
Segmentation_utilities.py is the utility API for Image Segmentation

## Requirements
Python3

TensorFlow

TFlearn

PIL

Scipy

Numpy

Matplotlib

Jupyter-Notebook

## Running the project
The project can be run by using the CNN Classifier.ipnb file and providing the name of the image file which contains the image of the number to be classified.
