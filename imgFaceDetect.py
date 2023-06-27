import os
import cv2 

# File Paths
script_path = os.path.dirname(os.path.abspath(__file__))
classifier_file = r'\classifier\haarcascade_frontalface_default.xml'
img_dir = r'\img\resized'
img_file = r'\image1.jpg'
full_img_path = script_path + img_dir + img_file

# Define Classifier and Convert Image to Greyscale
face_cascade = cv2.CascadeClassifier(script_path+classifier_file)
img = cv2.imread(full_img_path)
gray  = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray,1.1,4)

# Draw Rectangles on Detected Faces
for (x,y,w,h) in faces:
    cv2.rectangle(img, (x,y), (x+w,y+h), (30,155,40), 3)
cv2.imshow('Facial Recognition',img)
cv2.waitKey()