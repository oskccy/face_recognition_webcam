import cv2
import numpy as np
import face_recognition
import os
print('Test 1: huge w, imports in')

images = []
classNames = []
path = 'imagesAttendance'

for img in os.listdir(path):
    curImg = cv2.imread(f'{path}/{img}')
    images.append(curImg)
    classNames.append(os.path.splitext(img)[0])

print('Test 2: fucking array additions')

def findEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    
    return encodeList

encodeListKnownFaces =  findEncodings(images)
print('Test 3: Encoding Complete')

cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    imgTinier = cv2.resize(img,(0,0), None, 0.25, 0.25)
    imgTinier = cv2.cvtColor(imgTinier,cv2.COLOR_BGR2RGB)

    facesInFrame = face_recognition.face_locations(imgTinier)
    encodeCurrentFrame = face_recognition.face_encodings(imgTinier, facesInFrame)

    for enc, loc, in zip(encodeCurrentFrame, facesInFrame):
        matches = face_recognition.compare_faces(encodeListKnownFaces, enc)
        faceDist = face_recognition.face_distance(encodeListKnownFaces, enc)
        #print(faceDist)
        matchIndex = np.argmin(faceDist)

        if matches[matchIndex]:
            name = classNames[matchIndex].upper()
            #print(name)
            y1,x2,y2,x1 = loc
            y1,x2,y2,x1 = y1*4,x2*4,y2*4,x1*4
            cv2.rectangle(img,(x1,y1), (x2,y2), (0,255,0), 5)
            cv2.rectangle(img, (x1,y2-35), (x2,y2), (0,255,0), cv2.FILLED)
            cv2.putText(img, name,(x1+6, y2-6), cv2.FONT_HERSHEY_COMPLEX, 0.75, (0,0,0), 2)      
        else:
            y1,x2,y2,x1 = loc
            y1,x2,y2,x1 = y1*4,x2*4,y2*4,x1*4
            cv2.rectangle(img,(x1,y1), (x2,y2), (0,255,0), 5)

            
    
    cv2.imshow('Webcam', img)
    cv2.waitKey(1)