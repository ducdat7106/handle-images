import cv2
import face_recognition 
import os  # using for load all a library image
import  numpy as np

################################### part 1: ####################################################

# ################### step 1: load image from archives image ########################################
path = "picture2"
images = []  # [] is list empty
classNames = []

# check all name file inside folder 'path'(or pic2)
myList = os.listdir(path) # ['Donal Trump.jpg', 'elon musk .jpg', 'Joker.jpg', 'tokuda.jpg']

print(myList)

for cl in myList:
    print(cl)
    
    # after reading, will push to the matrix
    currentImage = cv2.imread(f"{path}/{cl}")  # pic2/Donal Trump.jpg <-- name image

    # save matrix point image
    images.append(currentImage)

    # break end path image --> get image name --> cut name 
    # 0 --> name
    # 1 --> type of image (.jpg)
    classNames.append(os.path.splitext(cl)[0])

# lenght list
print(len(images))
print(classNames)


########################## step 2: determine location and encoding image ###################################

def encoding_image(images):    # def ~ define
    # encoding each picture
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode) # save các encode
    return encodeList


encodeListKnow = encoding_image(images)
print('encode successful')
print(len(encodeListKnow))
print('finish encoding')


# start up webcam
# cap = cv2.VideoCapture(0)
cap = cv2.VideoCapture("video-test.mp4")


while True:
    ret, frame = cap.read()
    frameS = cv2.resize(frame, (0, 0), None, fx=0.5, fy=0.5) # frameS ~ frame resize
    frameS = cv2.cvtColor(frameS, cv2.COLOR_BGR2RGB) # convert RGB
    
    # define face location and encoding it
    face_current_frame = face_recognition.face_locations(frameS) # define face at frame any current
    encode_current_frame = face_recognition.face_encodings(frameS)
    
    
   
    for encodeFace, faceLoc in zip(encode_current_frame, face_current_frame):  # get each face and location current to pairs
        matches = face_recognition.compare_faces(encodeListKnow,encodeFace)
        faceDis = face_recognition.face_distance(encodeListKnow,encodeFace)
        print(faceDis)
        matchIndex = np.argmin(faceDis) # đẩy về index của faceDis nhỏ nhất
        # print(matchIndex)  --> giống chỉ số của mảng


        if faceDis[matchIndex] < 0.50 :
            name = classNames[matchIndex].upper()
        else:
            name = "Unknow"

        #print tên lên frame
        y1, x2, y2, x1 = faceLoc # toạ độ khuôn mặt
        y1, x2, y2, x1 = y1*2, x2*2, y2*2, x1*2
        cv2.rectangle(frame,(x1,y1), (x2,y2),(0,200,0),2)
        cv2.putText(frame,name,(x2,y2),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2) #đặt text bên cạnh


    cv2.imshow('show image', frame)
    if cv2.waitKey(1) == ord("q"):  # độ trễ 1/1000s , nếu bấm q sẽ thoát
        break
    
cap.release()  # giải phóng camera
cv2.destroyAllWindows()  # thoát tất cả các cửa sổ

    
    

