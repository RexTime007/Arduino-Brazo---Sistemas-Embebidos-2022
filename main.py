from lib2to3.pgen2.token import RPAR
from logging import root
from time import sleep
from tkinter import *
from tkinter import filedialog
from PIL import Image
from PIL import ImageTk
import cv2 as cv
import os
import imutils
import concurrent.futures
import threading
import serial, time


sleep(1)

r1 = [3,3,7,7,7,7,3,8,3,8]
rG = [0,143,90,125,90,125,0,0,143,31]
rP = [0,119,90,125,90,125,0,0,119,31]
rV = [0,87,90,125,90,125,0,0,87,31]
rM = [0,61,90,125,90,125,0,0,61,31]
ser = serial.Serial('COM4', 9600)
face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('MoneloLBPHF.yaml')
faceClassif = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')
global peopleList
global QUIEN
global HILOSTOP
global YAMANDO
HILOSTOP = True
QUIEN = ""
YAMANDO = True
m3 = 0
m4 = 0
m5 = 0
m6 = 0
m7 = 0
m8 = 0
peopleList = os.listdir('rostros/')



def reconocimiento(frame):
    global HILOSTOP
    global YAMANDO
    if HILOSTOP:
        #HILOSTOP = False
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        auxFrame = gray.copy()
        faces = faceClassif.detectMultiScale(gray,1.3,5)
        global QUIEN
        for (x,y,w,h) in faces:
            rostro = auxFrame[y:y+h,x:x+w]
            rostro = cv.resize(rostro,(150,150),interpolation= cv.INTER_CUBIC)
            result = face_recognizer.predict(rostro)
            #print(result)

            #cv.putText(frame,'{}'.format(result),(x,y-5),1,1.3,(255,255,0),1,cv.LINE_AA)
            # LBPHFace
            if result[1] < 60:
                #frame = cv.putText(frame,'{}'.format(peopleList[result[0]]),(x,y-25),2,1.1,(0,255,0),1,cv.LINE_AA)
                #frame = cv.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)
                QUIEN = peopleList[result[0]]
                print(QUIEN)
                if QUIEN != 'Desconocido' or QUIEN != "" or QUIEN != "Camara Apagada" or QUIEN != "Buscando" or QUIEN != "Camara Encendida":
                    HILOSTOP = False
                    if QUIEN == "VICTOR" and YAMANDO:
                        YAMANDO = False
                        
                    elif QUIEN == "MENDOZA" and YAMANDO:
                        YAMANDO = False
                       
                    elif QUIEN == "PEDRO" and YAMANDO:
                        YAMANDO = False
                        

                    elif QUIEN == "GREANS" and YAMANDO:
                        YAMANDO = False
                        

                        
                        
            else:
                #frame = cv.putText(frame,'Desconocido',(x,y-20),2,0.8,(0,0,255),1,cv.LINE_AA)
                #frame = cv.rectangle(frame, (x,y),(x+w,y+h),(0,0,255),2)
                QUIEN = 'Desconocido'
                HILOSTOP = True
        print(QUIEN)
        #HILOSTOP = True

def closeOpenCV():
    global QUIEN
    global YAMANDO
    YAMANDO = True
    lblVideo.image = ""
    cap.release()
    QUIEN="Camara Apagada"
    lblQuien.configure(text=QUIEN)
    btnOpenCV['state'] = 'normal'
    #print(threading.active_count())

def otro():
    global HILOSTOP
    global QUIEN
    global YAMANDO
    YAMANDO = True
    QUIEN = "Buscando"
    lblQuien.configure(text=QUIEN)
    HILOSTOP = True



def vision():
    global cap
    global QUIEN
    ret, frame = cap.read()
    if ret:
        frame = imutils.resize(frame, width=500)
        thr = threading.Thread(target=reconocimiento, args=(frame,))
        thr.start()
        #print(threading.active_count())
        frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
        im = Image.fromarray(frame)
        img = ImageTk.PhotoImage(image=im)
        
        lblVideo.configure(image=img)
        lblVideo.image = img
        lblQuien.configure(text=QUIEN)
        lblVideo.after(10, vision)
    else:
        lblVideo.image = ""
        cap.release()
def opencv():
    global cap
    global QUIEN
    QUIEN = "Camara Encendida"
    lblQuien.configure(text=QUIEN)
    cap = cv.VideoCapture(1, cv.CAP_DSHOW)
    btnOpenCV['state'] = 'disable'
    vision()

def moverBrazo1():
   ser.write(str("3,"+str(motor1.get())).encode())
   pass
def moverBrazo2():
    ser.write(str("4,"+str(motor2.get())).encode())
    pass
def moverBrazo3():
    ser.write(str("5,"+str(motor3.get())).encode())
    pass
def moverBrazo4():
    ser.write(str("6,"+str(motor4.get())).encode())
    pass
def moverBrazo5():
    ser.write(str("7,"+str(motor5.get())).encode())
    pass
def moverBrazo6():
    ser.write(str("8,"+str(motor6.get())).encode())
    pass
def default1():
    ser.write(str(str("3")+","+str("90")).encode())
    sleep(4)
    ser.write(str(str("4")+","+str("40")).encode())
    sleep(3)
    ser.write(str(str("5")+","+str("30")).encode())
    sleep(3)
    ser.write(str(str("6")+","+str("90")).encode())
    sleep(3)
    ser.write(str(str("7")+","+str("115")).encode())
    sleep(3)
    ser.write(str(str("8")+","+str("30")).encode())
    

cap = None
root = Tk()
root.title("Reconocimiento de Rostros")
root.geometry("1009x500")
lblInfo = Label(root, text="Vision pal brazo", font=("Helvetica", 20))
lblInfo.pack()
lblQuien = Label(root, text="¿Quien sos?, identifícate", font=("Helvetica", 20))
lblQuien.place(x=150, y=450)
lblVideo = Label(root)
lblVideo.place(x=15, y=45)
btnOpenCV = Button(root, text="Abrir Camara", command=opencv)
btnOpenCV.place(x=550, y=115)
btnCloseCV = Button(root, text="Cerrar Camara", command=closeOpenCV)
btnCloseCV.place(x=550, y=160)
btnVolver = Button(root, text="Volver a detectar", command=otro)
btnVolver.place(x=550, y=200)
btnVolver = Button(root, text="Default", command=default1)
btnVolver.place(x=550, y=240)


#Motor 1
motor1 = Scale(root, from_=0, to=180, orient=HORIZONTAL)
motor1.place(x=750, y=110)
lblMotor1 = Label(root, text="Motor 1", font=("Helvetica", 12))
lblMotor1.place(x=680, y=110)
#Motor 2
motor2 = Scale(root, from_=0, to=140, orient=HORIZONTAL)
motor2.place(x=750, y=170)
lblMotor2 = Label(root, text="Motor 2", font=("Helvetica", 12))
lblMotor2.place(x=680, y=170)
#Motor 3
motor3 = Scale(root, from_=0, to=180, orient=HORIZONTAL)
motor3.place(x=750, y=240)
lblMotor3 = Label(root, text="Motor 3", font=("Helvetica", 12))
lblMotor3.place(x=680, y=240)
#Motor 4|
motor4 = Scale(root, from_=0, to=180, orient=HORIZONTAL)
motor4.place(x=750, y=310)
lblMotor4 = Label(root, text="Motor 4", font=("Helvetica", 12))
lblMotor4.place(x=680, y=310)
btnMoverBrazo1 = Button(root, text="Mover Brazo 1", command=moverBrazo1)
btnMoverBrazo1.place(x=880, y=110)
btnMoverBrazo2 = Button(root, text="Mover Brazo 2", command=moverBrazo2)
btnMoverBrazo2.place(x=880, y=170)
btnMoverBrazo3 = Button(root, text="Mover Brazo 3", command=moverBrazo3)
btnMoverBrazo3.place(x=880, y=240)
btnMoverBrazo4 = Button(root, text="Mover Brazo 4", command=moverBrazo4)
btnMoverBrazo4.place(x=880, y=310)
btnMoverBrazo5 = Button(root, text="Mover Brazo 5", command=moverBrazo5)
btnMoverBrazo5.place(x=880, y=380)
btnMoverBrazo6 = Button(root, text="Mover Brazo 6", command=moverBrazo6)
btnMoverBrazo6.place(x=880, y=450)
#Motor 5
motor5 = Scale(root, from_=0, to=180, orient=HORIZONTAL)
motor5.place(x=750, y=380)
lblMotor5 = Label(root, text="Motor 5", font=("Helvetica", 12))
lblMotor5.place(x=680, y=380)
#Motor 6
motor6 = Scale(root, from_=0, to=100, orient=HORIZONTAL)
print(motor6.get())
motor6.place(x=750, y=450)
motor1.set(90)
motor2.set(40)
motor3.set(30)
motor4.set(90)
motor5.set(115)
motor6.set(30)
lblMotor6 = Label(root, text="Motor 6", font=("Helvetica", 12))
lblMotor6.place(x=680, y=450)
root.mainloop()