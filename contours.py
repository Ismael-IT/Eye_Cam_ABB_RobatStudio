from cv2 import circle, threshold
from matplotlib.contour import ContourSet
import cv2 as cv

def ImageProcessing():
  # Reading Image
  font = cv.FONT_HERSHEY_COMPLEX
  image2 = cv.imread("Photos/workPlace.png",cv.IMREAD_COLOR)

  # Reading same image in another 
  # variable and converting to gray scale.
  image = cv.imread('Photos/workPlace.png', cv.IMREAD_GRAYSCALE)

  # Coverting image to binary image
  #(black and white only image)
  img_blur = cv.GaussianBlur(image, (3,3), 0) 
  _,Threshold = cv.threshold(image,110,255,cv.THRESH_BINARY)
  _,threshold2 = cv.threshold(img_blur,70,255,cv.THRESH_BINARY) # Removing grey 

  # Detecting contours in image
  countours,_ = cv.findContours(threshold2,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)

  # Going through every contours found in the image.
  Object=[]
  for cnt in countours:
      
      area = cv.contourArea(cnt) # Calculate small area and remove small elements
      approx = cv.approxPolyDP(cnt, 0.03 * cv.arcLength(cnt, True), True)

      # draw boundary of contours
      if area > 10000.0 and area < 1036800.0: # removing too smal areas and  large area since background of image is white max ara is halv of camera frame 
        cv.drawContours(image2,[cnt],0,(0,255,0),2)
        x,y,w,h =cv.boundingRect(cnt)
        #cv.rectangle(image2,(x,y),(x + w, y + h),(0,255,0),3)
        
        n = approx.ravel() 
        index = 0
        # calculate x,y coordinate of center
        M=cv.moments(cnt)
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])
        
        
        if len(approx) == 3:                                       # Test if the object have 3 cornes
          cv.putText(image2,"Triangle",(x,y-20),font,1.5,(255,0,0))
          cv.circle(image2, (cX, cY), 5, (255, 255, 255), -1)
          Object.append("Triangle"+" "+str(cX)+" "+str(cY))
        elif len(approx) == 4:                                    # Test if the object have 4 cornes
          cv.putText(image2,"Square",(x,y-20),font,1.5,(255,0,0))
          cv.circle(image2, (cX, cY), 5, (255, 255, 255), -1)
          Object.append("Square"+" "+str(cX)+" "+str(cY))
        elif len(approx) == 8:                                     # Test if the object have 8 cornes
          cv.circle(image2, (cX, cY), 5, (255, 255, 255), -1)
          cv.putText(image2,"Circle",(x,y-20),font,1.5,(255,0,0))
          Object.append("Circle"+" "+str(cX)+" "+str(cY))
    
      # Used to flatted the array containing
      # the co-ordinates of the vertices.
        n = approx.ravel() 
        i = 0
        for j in n:
          if(i % 2 == 0):
            x = n[i]
            y = n[i+1]

            #string containing the co-ordinate.
            string = str(x) + " " + str(y)

            if (i == 0):
            # Texte on topmost co-ordinates
              cv.putText(image2,"Pos"+" "+ string,(x,y),font,0.5,(255,0,0))
            else:
            #Text on remaining co-ordinate
              cv.putText(image2,string,(x,y),font,0.5,(0,255,0))
      
          i=i+1        
        index+=1
        


  return Object,image2

