import cv2 as cv
import numpy as np
from pyzbar import pyzbar

CAM_ID = 0
CAM_WIDTH = 320
CAM_HEIGHT = 240

lower_blue = np.array([73, 131, 152])
upper_blue = np.array([121,255,255])

lower_red = np.array([19, 61, 119])
upper_red = np.array([179, 255, 255])

def open_cam(camera = CAM_ID):
    
    cap = cv.VideoCapture(camera)
    
    if cap.isOpened():
        cap.set(cv.CAP_PROP_FRAME_WIDTH, CAM_WIDTH)
        cap.set(cv.CAP_PROP_FRAME_HEIGHT, CAM_HEIGHT)
        cv.namedWindow('frame')
        return cap
    else:
        print("camera open failed \n")

def cam_streaming(cap):
    ret, frame = cap.read()
    
    if ret == True:
        return frame
    
    else:
        print("camera read error \n")
        
def image_filter(frame):
    hsv_blue = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    hsv_red = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    mask_blue = cv.inRange(hsv_blue, lower_blue, upper_blue)
    mask_red = cv.inRange(hsv_red, lower_red, upper_red)
    
    erode_blue_image = cv.erode(mask_blue, None, iterations = 2)
    dilate_blue_image = cv.dilate(mask_blue, None, iterations = 2)
    
    erode_red_image = cv.erode(mask_red, None, iterations = 2)
    dilate_red_image = cv.dilate(mask_red, None, iterations = 2)
    
    return dilate_blue_image, dilate_red_image 

def detect_goods(filter_blue_image, filter_red_image, frame):
    contours_blue = cv.findContours(filter_blue_image.copy(), cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)[-2]
    contours_red = cv.findContours(filter_red_image.copy(), cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)[-2]
    
    if len(contours_blue) > 0:
        c = max(contours_blue, key=cv.contourArea)
        signal = 'P'    
        
    elif len(contours_red) > 0:
        read_barcode
        c = max(contours_red, key=cv.contourArea)
        signal = 'F'
    
    else:
        print("no goods")
        return None
 
    ((x, y), radius) = cv.minEnclosingCircle(c) 
    M = cv.moments(c)
    center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
    
    if int(radius) > 10:
        data, frame = read_barcode(frame)
        cv2.circle(frame, (int(x), int(y)), int(radius), (0, 255, 255), 2)
        cv2.circle(frame, center, 5, (0, 0, 255), -1)
        cv2.putText(frame, str(x)+' , '+str(y), (x, y), cv.FONT_HERSHEY_PLAIN, 1.0, 255, 2)
        
    return frame, data, signal

def read_barcode(frame):
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    decoded = pyzbar.decode(gray)

    for d in decoded: 
        x, y, w, h = d.rect

    barcode_data = d.data.decode("utf-8")
    barcode_type = d.type

    cv.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
    return barcode_data, frame
    

cap = open_cam()

while(True):
    
    frame = cam_streaming(cap)
    
    frame = cv.GaussianBlur(frame, (5, 5), 0)
    
    (filter_blue_image, filter_red_image) = image_filter(frame)
    
    frame = detect_goods(filter_blue_image, filter_red_image, frame)
    
    cv.imshow('frame', frame)
    cv.imshow('filter_blue_mask', filter_blue_image)
    cv.imshow('filter_red_mask', filter_red_image)

    if cv.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv.destroyAllWindows()