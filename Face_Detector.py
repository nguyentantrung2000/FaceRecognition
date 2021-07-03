
import cv2
from random import randrange
#train computure know what is face 
train_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#Choose an image to detect faces in
# img = cv2.imread('manyfaces.jpeg')

#dectect face webcam
webcam = cv2.VideoCapture(0)

while True:
    successful_frame_read , frame = webcam.read()

#gratscale your img & frame
    grayscaled_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face_detect = train_face_data.detectMultiScale(grayscaled_img)
    
    for (x,y,w,h) in face_detect:
        cv2.rectangle(frame, (x,y), (x+w,y+h)     , (randrange(255),randrange(255),randrange(255))             ,5)
    
    cv2.imshow("Bo Programmer Face Detector", frame)
    Key = cv2.waitKey(1)
    #press Q to close Program
    if Key==81 or Key==113:
        break
### release the videocapture object
webcam.release()

# #detect face by function detectMultiScale
# face_detect = train_face_data.detectMultiScale(grayscaled_img)
# #                  top left   bottom right   color rectangle   thick rectangle
# for (x,y,w,h) in face_detect:
#     cv2.rectangle(img, (x,y), (x+w,y+h)     , (0,255,0)             ,5)
# #print(face_detect)


# cv2.imshow('Bo Programmer Face Detector', img)

# #when IDE show up img you can back with any key you want
# cv2.waitKey()

# print("code done hahah")