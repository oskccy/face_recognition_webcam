import cv2
import numpy as np
import face_recognition

oscar = face_recognition.load_image_file('imagesBasic/oscarNew.jpg')
oscar = cv2.cvtColor(oscar,cv2.COLOR_BGR2RGB)
##oscar = cv2.rotate(oscar,cv2.ROTATE_90_CLOCKWISE)

testImage = face_recognition.load_image_file('imagesBasic/oscarTest.jpg')
testImage = cv2.cvtColor(testImage,cv2.COLOR_BGR2RGB)
##testImage = cv2.rotate(testImage,cv2.ROTATE_90_CLOCKWISE)

location = face_recognition.face_locations(oscar)[0]
encodeOscar = face_recognition.face_encodings(oscar)[0]
cv2.rectangle(oscar,(location[3],location[0]),(location[1],location[2]),(255,0,255), 5)

locationTestImage = face_recognition.face_locations(testImage)[0]
encodetestImage = face_recognition.face_encodings(testImage)[0]
cv2.rectangle(testImage,(locationTestImage[3],locationTestImage[0]),(locationTestImage[1],locationTestImage[2]),(255,0,255), 5)

results = face_recognition.compare_faces([encodeOscar],encodetestImage)
faceDis = face_recognition.face_distance([encodeOscar],encodetestImage)
print(results, faceDis)

#cv2.imshow('oscar', oscar)
#cv2.imshow('testImage', testImage)
#cv2.waitKey(0)





 
