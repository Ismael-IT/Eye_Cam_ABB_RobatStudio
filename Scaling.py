from numpy import square
from contours import ImageProcessing

def Scaling(Object):
     
   # Object,_=ImageProcessing()
    Triangle=""
    Circle=""
    Square=""
    Home="GoHome 0 0"            # Here GoHome is add to make robot go Home after finnshing there task. NB! Data format is essential here but not coordinates since Home is define is Rapid code 

    # The scaling factor is found by measuring the work are(The area camera can see width=730mm hight=410) and scal it with the cameara res width=1920 hight=1080 
    for Data in Object:
        # scaling the objects from frames to mm
        if "Triangle" in Data:
            Triangle=Data.split()
            x=round(float(Triangle[1])/2.63,2)
            y=round(float(Triangle[2])/2.63,2)
            Triangle="Triangle"+" "+str(x)+" "+str(y)      
            
        elif "Circle" in Data:
            Circle=Data.split()
            x=round(float(Circle[1])/2.63,2)
            y=round(float(Circle[2])/2.63,2)
            Circle="Circle"+" "+str(x)+" "+str(y)  
            
        elif "Square" in Data:       
            Square=Data.split()
            x=round(float(Square[1])/2.63,2)
            y=round(float(Square[2])/2.63,2)
            Square="Square"+" "+str(x)+" "+str(y) 
    
    if Triangle or Circle or Square:         # Checking if there is Data in any of three object and add Home if any Data exists 
       Data=[Triangle,Circle,Square,Home]
    else:
        Data=[Triangle,Circle,Square]
    Data=list(filter(None,Data))            # Removing empy object(elemets) on data list
    return Data
