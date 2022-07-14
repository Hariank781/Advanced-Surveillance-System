import os
import time
from tkinter.messagebox import askyesno, showinfo
from tkinter import Tk, simpledialog

import face_recognition
import numpy as np
import cv2
from cv2 import *
from send_mail import send



path = 'total_images'
images = []
id = 0
classnames = []
mylist = os.listdir(path)
print(mylist)

for cl in mylist:
    curimg= cv2.imread(f'{path}/{cl}')
    images.append(curimg)
    classnames.append(os.path.splitext(cl)[0])
print(classnames)


def findencodings(images):
    encodelist = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodelist.append(encode)
    return encodelist


encodelistknown = findencodings(images)
print('Encoding Complete')

#cap = cv2.VideoCapture('http://192.168.78.7:8080/video')
cap = cv2.VideoCapture(0)
while True:
    success, img = cap.read()
    imgs = cv2.resize(img, (0, 0), None, 1.04, 1.04)
    imgs = cv2.cvtColor(imgs, cv2.COLOR_BGR2RGB)

    facescurframe = face_recognition.face_locations(imgs)
    encodescurframe = face_recognition.face_encodings(img, facescurframe)

    for encodeface, faceLoc in zip(encodescurframe, facescurframe):
        matches = face_recognition.compare_faces(encodelistknown, encodeface)
        faceDis = face_recognition.face_distance(encodelistknown, encodeface)
        print(faceDis)
        matchIndex = np.argmin(faceDis)
        k = cv2.waitKey(1)
        if k % 256 == 27:
            print('escaping')
            break

        if matches[matchIndex]:
            name = classnames[matchIndex].upper()
            print(name)
            y1, x2, y2, x1 = faceLoc
            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
            cv2.putText(img, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255), int(0.7))

        else:
            #     thresh = 1000
            #     foog = cv2.createBackgroundSubtractorMOG2( detectShadows = True, varThreshold = 50, history = 2800)
            #     fgmask = foog.apply(img)
            #     # Get rid of the shadows
            #     ret, fgmask = cv2.threshold(fgmask, 250, 255, cv2.THRESH_BINARY)
            #     contours, hierarchy = cv2.findContours(fgmask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[-2:]
            #     cnt = max(contours, default=0)

            # # make sure the contour area is somewhat hihger than some threshold to make sure its a person and not some noise.
            #     # if cv2.contourArea(cnt) > thresh:

            #     # Draw a bounding box around the person and label it as person detected
            #     x,y,w,h = cv2.boundingRect(cnt)
            #     cv2.rectangle(img,(x ,y),(x+w,y+h),(0,0,255),2)
            #     cv2.putText(img,'Person Detected',(x,y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.3, (0,255,0), 1, cv2.LINE_AA)
            y1, x2, y2, x1 = faceLoc
            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
            # cv2.putText(img,(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255),int(0.7))
            ret, frame = cap.read()  # return a single frame in variable `frame`

            # while(True):
            # cv2.imshow('img1',frame) #display the captured image
            # if cv2.waitKey(1) & 0xFF == ord('y'): #save on pressing 'y'
            cv2.imwrite('Unrecognised' + str(1) + '.jpg', frame)
            # cv2.destroyAllWindows()
            # break
            send()
            # time.sleep(10)
            response = askyesno(message='An unrecognised image has been discovered. Would you like to add the image to the dataset?', title='Add Image')
            if response:
                print('oui')
                application_window = Tk()
                name = simpledialog.askstring("Input", "What is your name?", parent=application_window)
                os.rename('Unrecognised1.jpg', 'total_images/%s.jpg' % (str(name)))
                showinfo(title='Image Added', message='The image has been added to the dataset.')
                id += 1
            else:
                os.remove('Unrecognised1.jpg')
                cap.release()
            # cap.release()

    cv2.imshow('webcam', img)
    cv2.waitKey(1)

# faceLock = face_recognition.face_locations(imgelon)[0]
# encodeElon = face_recognition.face_encodings(imgelon)[0]
# cv2.rectangle(imgelon,(faceLock[3],faceLock[0]),(faceLock[1],faceLock[2]),(255,0,255),2)

# faceLockTest = face_recognition.face_locations(imgelon)[0]
# encodeTest = face_recognition.face_encodings(imgtest)[0]
# cv2.rectangle(imgtest,(faceLockTest[3],faceLockTest[0]),(faceLockTest[1],faceLockTest[2]),(255,0,255),2)

# results = face_recognition.compare_faces([encodeElon], encodeTest)
# faceDis = face_recognition.face_distance([encodeElon], encodeTest)
# __main__.py
