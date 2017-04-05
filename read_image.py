from tkinter import *
import cv2
import numpy as np
face_cascade = cv2.CascadeClassifier('C:\\opencv\\opencv\\build\\etc\\haarcascades\\haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('C:\\opencv\\opencv\\build\\etc\\haarcascades\\haarcascade_eye.xml')


root2 = Tk()
root2.minsize(300, 100)
root2.configure(bg="#bababa")
root2.title("Find Frame")



def extrac_image():
    val = int(input1.get())
    val = val*10.0
    cap = cv2.VideoCapture('D:\semesters\semester 06\HCI\FaceDetectionApplication in python/output.avi')


    cap.set(1, val);  # Where frame_no is the frame you want
    ret, frame = cap.read()  # Read the frame
    cv2.imwrite("frame.jpg", frame)  # save frame as JPEG file

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = frame[y:y + h, x:x + w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
    cv2.imshow('window_name', frame)  # show frame on window
    cv2.imwrite("detected_frame.jpg", frame)  # save frame as JPEG file
    while True:
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    return


Label(root2, text="Press 'q' to be able to load another frame (press while image is showing)").grid(row=0,padx=0,pady=10)
Label(root2, text="Enter Time in Seconds").grid(row=1,padx=0,pady=10)
input1 = Entry(root2, width=20)
input1.grid(row=2, column=0,padx=20,pady=5)
button1 = Button(root2, text="Find Frame", width=20,command = extrac_image)
button1.grid(row=3, column=0,padx=20,pady=5)
root2.mainloop()

