import cv2

## read image
img = cv2.imread('girl1.png', 1)

## change size image
    ## (x, y) - (width, height)
# img = cv2.resize(img, (400, 400))

## change ratio image
    ## fx = 0.1 ~ 10%
img = cv2.resize(img, (0,0), fx=0.3, fy=0.3)

## save image new
cv2.imwrite('image-new1.png', img)

## rotate image
img = cv2.rotate(img, cv2.ROTATE_180)

## show image
cv2.imshow('girl beautiful ', img)

## wait press any key to exit
k = cv2.waitKey()
print(k)



