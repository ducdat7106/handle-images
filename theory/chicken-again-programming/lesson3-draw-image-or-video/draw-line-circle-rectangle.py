import cv2
import numpy as np__numpy_acronym

image_need_handle = cv2.VideoCapture(0)


# while loop
while True:
    # read image pass camera
    ret, frame = image_need_handle.read()

    # divide the frame into 4 parts

    width = int(image_need_handle.get(3))
    height = int(image_need_handle.get(4))

    #1 draw line
    img = cv2.line(frame, (0, 0), (width, height), (0, 0, 0), 10)
    img = cv2.line(frame, (0, height), (width, 0), (200, 0, 0), 10)
    img = cv2.line(frame, (width//2, 0), (width//2, height), (0, 200, 0), 10)
    img = cv2.line(frame, (0, height//2), (width, height//2), (0, 0, 200), 10)

    #2 draw cỉcle
        # thickness = -1 to fill color inside circle
    img = cv2.circle(frame, (200, 200), 100, (0, 0, 200), 3)
    img = cv2.circle(frame, (300, 400), 100, (0, 0, 50), -1)

    #3 paint rectangle
        # thickness = -1 to fill color inside rectangle
    img = cv2.rectangle(frame, (300, 300), (500, 400), (200, 200, 0), -1)

    img = cv2.rectangle(frame, (100, 100), (500, 400), (200, 100, 0), 3)
    
    #4 write text
    font = cv2.FONT_HERSHEY_COMPLEX
    img=cv2.putText(frame, 'duc dat 2000', (0, height-50), font, 1, (0,0,100), 4 )

    # Show captured images
    if ret == True:
        cv2.imshow('here is my image', img)
        print(ret)
    else:
        print('can not take a picture')
        print(ret)

    # exit white loop
    if cv2.waitKey(1) == ord('q'):  # q ~ quit
        break


# free memory variable 'image_need_handle'
image_need_handle.release()

cv2.destroyAllWindows()
