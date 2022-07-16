import cv2
import face_recognition
import os  # using for load library iamge
import  numpy as np

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

# while True:
#     ret, frame = cap.read()
#     frame_resize = cv2.resize(frame, (0, 0), None, fx=0.5, fy=0.5)
#     frame_resize = cv2.cvtColor(frame_resize, cv2.COLOR_BGR2RGB)
    
#     # define face location and encoding it
#     face_current_frame = face_recognition.face_locations(frame_resize) # define face at frame any
#     encode_current_frame = face_recognition.face_encodings(frame_resize)
    
    
#     # get each face and location current to pairs
#     for encodeFace, faceLocation in zip(encode_current_frame, face_current_frame):
#          matches = face_recognition.compare_faces(encodeListKnow,encodeFace)
#         faceDis = face_recognition.face_distance(encodeListKnow,encodeFace)
#         print(faceDis)
#         matchIndex = np.argmin(faceDis) #đẩy về index của faceDis nhỏ nhất


#         if faceDis[matchIndex] <0.50 :
#             name = classNames[matchIndex].upper()
#         else:
#             name = "Unknow"

#         #print tên lên frame
#         y1, x2, y2, x1 = faceLoc
#         y1, x2, y2, x1 = y1*2, x2*2, y2*2, x1*2
#         cv2.rectangle(frame,(x1,y1), (x2,y2),(0,255,0),2)
#         cv2.putText(frame,name,(x2,y2),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)


#     cv2.imshow('Ga Lai Lap Trinh', frame)
#     if cv2.waitKey(1) == ord("q"):  # độ trễ 1/1000s , nếu bấm q sẽ thoát
#         break
    
# cap.release()  # giải phóng camera
# cv2.destroyAllWindows()  # thoát tất cả các cửa sổ

while True:
    ret, frame= cap.read()
    framS = cv2.resize(frame,(0,0),None,fx=0.5,fy=0.5)
    framS = cv2.cvtColor(framS, cv2.COLOR_BGR2RGB)

    # xác định vị trí khuôn mặt trên cam và encode hình ảnh trên cam
    facecurFrame = face_recognition.face_locations(framS) # lấy từng khuôn mặt và vị trí khuôn mặt hiện tại
    encodecurFrame = face_recognition.face_encodings(framS)

    for encodeFace, faceLoc in zip(encodecurFrame,facecurFrame): # lấy từng khuôn mặt và vị trí khuôn mặt hiện tại theo cặp
        matches = face_recognition.compare_faces(encodeListKnow,encodeFace)
        faceDis = face_recognition.face_distance(encodeListKnow,encodeFace)
        print(faceDis)
        matchIndex = np.argmin(faceDis) #đẩy về index của faceDis nhỏ nhất


        if faceDis[matchIndex] <0.50 :
            name = classNames[matchIndex].upper()
        else:
            name = "Unknow"

        #print tên lên frame
        y1, x2, y2, x1 = faceLoc
        y1, x2, y2, x1 = y1*2, x2*2, y2*2, x1*2
        cv2.rectangle(frame,(x1,y1), (x2,y2),(0,255,0),2)
        cv2.putText(frame,name,(x2,y2),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)


    cv2.imshow('Ga Lai Lap Trinh', frame)
    if cv2.waitKey(1) == ord("q"):  # độ trễ 1/1000s , nếu bấm q sẽ thoát
        break
cap.release()  # giải phóng camera
cv2.destroyAllWindows()  # thoát tất cả các cửa sổ
