import os
import cv2 

def detectFace(img,face_cascade):
    # Greyscale Image and Detect Faces
    gray  = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,1.1,4)

    # Draw Rectangles on Detected Faces
    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w,y+h), (30,155,40), 3)
    cv2.imshow('Facial Recognition',img)

def camFaceDetect(face_cascade):
    cap = cv2.VideoCapture(0)
    while True:
        _, img = cap.read()
        detectFace(img,face_cascade)
        k = cv2.waitKey(30) & 0xff  
        if k==27: # Pressing Esc Will Exit While Loop
            break

def imgFaceDetect(face_cascade,full_img_path):
    img = cv2.imread(full_img_path)
    detectFace(img,face_cascade)
    cv2.waitKey()

# File Paths
script_path = os.path.dirname(os.path.abspath(__file__))
classifier_file = r'\classifier\haarcascade_frontalface_default.xml'
img_dir = r'\img\resized'
img_file = r'\image1.jpg'
full_img_path = script_path + img_dir + img_file

# Define Classifier 
face_cascade = cv2.CascadeClassifier(script_path+classifier_file)

# Choose Face Detection Mode - Still Image or Video Capture Mode
mode = 0
while mode < 1 or mode > 2 or type(mode)!=int:
    mode = int(input(f"Choose Mode (Enter Number): \n  1. Live Video Capture \n  2. Image Detection \n"))
    if mode < 1 or mode > 2 or type(mode)!=int:
        print('Enter The Listed Integer Value To Select Mode')
if mode == 1:
    camFaceDetect(face_cascade)
elif mode == 2:
    imgFaceDetect(face_cascade,full_img_path)