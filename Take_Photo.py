# program to capture single image from webcam in python
from turtle import width
import cv2 as cv
from cv2 import resize

def TakePhoto():
    capture = cv.VideoCapture(0) # initialize the camera with value from cam-port
    capture.set(3,1920) # set camera resolution width
    capture.set(4,1080) # set camera resolution higth

    # reading the input using the camera
    isTrue, image = capture.read()

    # Function for image scaling if needed 
    def rescaleFrame(image):
        width=1920
        hight=1080
        dimentions= (width,hight)

        return cv.resize(image,dimentions,interpolation=cv.INTER_AREA)

    image = rescaleFrame(image) # scaling the image

    # If image detected without erro show resulte
    if isTrue:
        
        # cv.imshow("Work Place", image)              # Show resulte with frame name and image 
        cv.imwrite("Photos/workPlace.png",image)      #Save the image in local storege
        # cv.resizeWindow("Work Place", 1920,1080)

        # # Type 0 to destroy image and window 

        # cv.waitKey(0)
        # cv.destroyWindow("Work Place")
        print("Camera is online")
    # If capture image is corrupted show errow msg
    else:
        print("No image detected, Please try again")
    return image