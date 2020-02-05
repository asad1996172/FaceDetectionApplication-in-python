from tkinter import *
import cv2
import numpy as np
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye.xml")


root = Tk()
root.minsize(400, 100)
root.configure(bg="#bababa")
root.title("Record Video")


def start_recording():
    cap = cv2.VideoCapture(0)
    # Define the codec and create VideoWriter object
    # Define the codec and create VideoWriter object

    fourcc = cv2.VideoWriter_fourcc(*'MJPG')

    out = cv2.VideoWriter('output.avi', fourcc, 10.0, (640, 480))


    while (cap.isOpened()):
        ret, frame = cap.read()
        print('Recording!!!')
        if ret == True:
            # frame = cv2.flip(frame, 0)
            out.write(frame)

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, 1.3, 5)
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
                roi_gray = gray[y:y + h, x:x + w]
                roi_color = frame[y:y + h, x:x + w]
                eyes = eye_cascade.detectMultiScale(roi_gray)
                for (ex, ey, ew, eh) in eyes:
                    cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)


            cv2.imshow('frame', frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break
    cap.release()
    out.release()
    cv2.destroyAllWindows()
    return


def stop_recording():
    cv2.waitKey = 113
    return



button1 = Button(root, text="Start", width=10, command=start_recording,bg="blue")
button2 = Label(root, text="To Stop and save video press 'q'", width=40)
button1.grid(row=0, column=0, padx=70, pady=50)
button2.grid(row=0, column=1, padx=8, pady=50)
# imageFrame = tk.Frame(window, width=600, height=500)
# imageFrame.grid(row=0, column=0, padx=10, pady=2)

root.mainloop()

