import cv2
import numpy as np

'''
This program is my first hands-on experimenting with openCV. It takes an image and can draw an outline around objects of a chosen colour.

Used as guide https://medium.com/@sasasulakshi/opencv-object-masking-b3143e310d03

Future changes: Error handling
- check if image pathway exists
- check if colour input is valid colour/string

'''

def main():
    print("Welcome to object detection!\Make sure your image in the same folder as this code.")
    path = str(input("What is the filename + extension of your image?\n"))
    print("Your object can be red, orange, yellow, green, blue or purple")
    colour = input("What colour is your object?\n").lower()

    detectObject(path, colour)


def detectObject(path, colour):

    #setting upper and lower bound for hsv scale to 0 by default
    ub = 0
    lb = 0 

    #setting upper and lower bound for hsv for colour selected range - may need to be tweaked
    match colour:
        case "red":
            ub = 20
            lb = -30 
        case "orange":
            ub = 40
            lb = 0
        case "yellow":
            ub = 70
            lb = 40
        case "green": #green doesn't seem to work well 
            ub = 150
            lb = 70
        case "blue": #Blue doesn't seem to work well
            ub = 270
            lb = 150
        case "purple": #purple doesn't seem to work well
            ub = 300
            lb = 270

    #read image 
    img = cv2.imread(path)

    #converting to hsv image
    hsv_img = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

    #Setting colour upper and lower bounds for image mask
    colour_ub = np.array([ub,255,255])
    colour_lb = np.array([lb,25,25]) 

    mask = cv2.inRange(hsv_img,colour_lb,colour_ub)

    #Find contours within masked image
    contours, new = cv2.findContours(mask.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    contourMask = img.copy()

    #Change outline to different colour if object colour is green or yellow to stand out better
    if colour == "green" or colour == "yellow":
        cv2.drawContours(contourMask, contours, -1, (0, 0, 255), 3)
    else:
        cv2.drawContours(contourMask, contours, -1, (0, 255, 0), 3)

    #creating cv window
    cv2.namedWindow("HSV Red Masked", cv2.WINDOW_NORMAL)
    cv2.imshow("contourMask", contourMask)
    #cv2.imshow("HSV Red Masked",mask)

    cv2.waitKey(0) & 0xFF 
    cv2.destroyAllWindows()


main()