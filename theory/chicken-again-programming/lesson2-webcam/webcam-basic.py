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

    small_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)  # 1/4 frame output

    # create block black for all frame output
    image = np__numpy_acronym.zeros(frame.shape, np__numpy_acronym.uint8)

    # :height//2 ~ 0 --> height/2
    # height//2: ~ height/2 --> height
    image[:height//2, :width//2] = small_frame  # 2nd quadrant
    image[:height//2, width//2:] = small_frame  # 1st quadrant
    image[height//2:, :width//2] = small_frame  # 3rd quadrant
    image[height//2:, width//2:] = small_frame  # 4th quadrant

    image[height // 2:, width // 2:] = cv2.rotate(small_frame, cv2.ROTATE_180)

    # Show captured images
    if ret == True:
        cv2.imshow('here is my image', image)
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
