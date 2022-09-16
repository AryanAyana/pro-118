import cv2
# Initiate video capture for video file
cap = cv2.VideoCapture('walking.avi')


# Create our body classifier
body_classifier = cv2.CascadeClassifier('harrcascade_fullbody.xml')


# Loop once video is successfully loaded
while(True):
       ret,frame = cap.read()
       gray= cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
       bodies = body_classifier.detectMultiScale(gray)
       print(bodies)

       for (x,y,w,h) in bodies:
         cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        
         cv2.imshow('frame',frame)
    # Read first frame
    

    #Convert Each Frame into Grayscale
    
    # Pass frame to our body classifier
    
    
    # Extract bounding boxes for any bodies identified
    
#32 is the Space Key
       if cv2.waitKey(25)==32:
         break          

cap.release()
cv2.destroyAllWindows()        
