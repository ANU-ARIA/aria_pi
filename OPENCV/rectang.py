import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)

lower_blue = np.array([73, 131, 152])
upper_blue = np.array([121, 255, 255])

#lower_red = np.array([32, 18, 0])
#upper_red = np.array([179, 255, 255])

print('width: {0}, height: {1}'.format(cap.get(3),cap.get(4)))  
cap.set(3,320)   
cap.set(4,240)

while(True):
    ret, frame = cap.read()

    frame = cv.GaussianBlur(frame, (5, 5), 0)
    hsv_blue = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    hsv_red = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    mask_blue = cv.inRange(hsv_blue, lower_blue, upper_blue)
    mask_red = cv.inRange(hsv_red, lower_red, upper_red)

    contours_blue = cv.findContours(mask_blue.copy(), cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)[-2]
    contours_red = cv.findContours(mask_red.copy(), cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)[-2]

    if len(contours_blue) > 0:
        c = max(contours_blue, key=cv.contourArea)
        signal = 'P'    
        
    elif len(contours_red) > 0:
        c = max(contours_red, key=cv.contourArea)
        signal = 'F' 
    
    else:
        continue

    x, y, w, h = cv.boundingRect(c)    
    cv.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 2)
    cv.circle(frame, (x + int(w/2), y + int(h/2)), 3, (0, 0, 255), -1)
    cv.putText(frame, "( " + str(x + int(w/2)) + ", " + str(y + int(h/2)) + " )", (x + int(w/2), y + int(h/2)), cv.FONT_HERSHEY_SIMPLEX, 0.3, (255, 0, 0), 2)

    cv.imshow('frame', frame)
    #cv.imshow('res', res)
    cv.imshow('blue_mask', mask_blue)
    #cv.imshow('red_mask', mask_red)

    if cv.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv.destroyAllWindows()