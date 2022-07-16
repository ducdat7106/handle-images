import cv2
import face_recognition
import os  # using for load library iamge

################################### part 1: ####################################################

# ################### step 1: load image from archives image ########################################
path = "pic2"
images = []  # [] is list empty
classNames = []

# check all name file inside folder 'path'(or pic2)
myList = os.listdir(path)
# ['Donal Trump.jpg', 'elon musk .jpg', 'Joker.jpg', 'tokuda.jpg']
print(myList)

for index in myList:
    print(index)
    # after reading, will push to the matrix
    currentImage = cv2.imread(f"{path}/{index}")  # pic2/Donal Trump.jpg

    # save matrix point image
    images.append(currentImage)

    # break end path image --> get image name
    classNames.append(os.path.splitext(index)[0])

# lenght list
print(len(images))
print(classNames)


########################## step 2: encoding image###################################
# def ~ define
def encoding_image(images):
    # encoding each picture
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList


encodeListKnow = encoding_image(images)
print('encode successful')
print(len(encodeListKnow))
print('finish encoding')


# start up webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    frame_resize = cv2.resize(frame, (0, 0), None, fx=0.5, fy=0.5)
    frame_resize = cv2.cvtColor(frame_resize, cv2.COLOR_BGR2RGB)
    
    # define face location and encoding it
    face_current_frame = face_recognition.face_locations(frame_resize) # define face at frame any
    encode_current_frame = face_recognition.face_encodings(frame_resize)
    
    
    for encodeFace, faceLoc in zip(encode_current_frame, face_current_frame)
            
