import cv2
import face_recognition


########## Part 1: Start iamge recognition############
# load image need check
# convert image from BGR to RGB
imgElon = face_recognition.load_image_file('picture/luu-diec-phi-hair-long.png')
imgElon = cv2.cvtColor(imgElon, cv2.COLOR_BGR2RGB)

# define face location
faceLocation = face_recognition.face_locations(imgElon)[0]

# print face position
# type (y1, x2, y2, x1)
print(faceLocation)

# image encoding
encodeElon = face_recognition.face_encodings(imgElon)[0]

# draw a rectangle on top of the image
cv2.rectangle(imgElon, (faceLocation[3], faceLocation[0]),
              (faceLocation[1], faceLocation[2]), (200, 0, 0), 2)


# ######################## Stop image recognition ###########################


# ###################### Part 2: Start image check ################################

###### do similar image at part recognition  ######
imgCheck = face_recognition.load_image_file('picture/luu-diec-phi-pro.png')
imgCheck = cv2.cvtColor(imgCheck, cv2.COLOR_BGR2RGB)

faceCheck = face_recognition.face_locations(imgCheck)[0]
print(faceCheck)

encodeCheck = face_recognition.face_encodings(imgCheck)[0]

cv2.rectangle(imgCheck, (faceCheck[3], faceCheck[0]),
              (faceCheck[1], faceCheck[2]), (0, 200, 0), 2)

######################## Stop image check ################################


####################### Part 3: Check image #####################################
results = face_recognition.compare_faces([encodeElon], encodeCheck)
# print(results)

##########################################################################


# open width
# case have many image to compare --> need know distance (error) image
faceDistance = face_recognition.face_distance([encodeElon], encodeCheck)
print(results, faceDistance)

# check type of variable
# print(type(faceDistance))

# write text next to photo
cv2.putText(imgCheck, f"{results}{ round(faceDistance[0], 2) }", (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,200), 2)

imgCheck = cv2.resize(imgCheck,(0,0), fx=0.5, fy=0.5)

# show image
cv2.imshow('Elon Musk', imgElon)
cv2.imshow('Elon Check', imgCheck)

cv2.waitKey()
cv2.destroyAllWindows()
