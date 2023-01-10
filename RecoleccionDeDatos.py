import imutils
import cv2 as cv
import os

nombrePersona = "CHIMUELO"
nombrePersona = nombrePersona.upper()
ruta = 'rostros' +'/' + nombrePersona
if not os.path.exists(ruta):
    os.mkdir(ruta)
    print("Carpeta", ruta, "creada")

haarcascades = 'haarcascade_frontalface_default.xml'
faceClassif = cv.CascadeClassifier(cv.data.haarcascades + haarcascades)

carpestas = os.listdir(ruta)

archivos = os.listdir(ruta) #cambiar aqui por algo mejor
si = []
for archivo in archivos:
    si.append(int(archivo.split('_')[1].split('.')[0]))
if len(si) == 0:
    maximo = 0
else:
    maximo = max(si)
    

cont = maximo + 1
cap = cv.VideoCapture(1)

while True:
    ret, frame = cap.read()
    
    if not ret:
        break
    
    frame = imutils.resize(frame, width=512)
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    auxFrame = frame.copy()
    
    faces = faceClassif.detectMultiScale(gray,1.3,5)
    
    for (x, y, w, h) in faces:
        cv.rectangle(frame, (x, y), (x+w, y+h), (0,255,0), 2)
        rostro = auxFrame[y:y + h, x:x + w]
        rostro = cv.resize(rostro, (150, 150), interpolation=cv.INTER_CUBIC)
        cv.imwrite(ruta + '/Imagen_{}.jpg'.format(cont), rostro)
        cont += 1
    cv.imshow("frame", frame)
    k = cv.waitKey(1)
    if k == 27 or cont  >= 300 + maximo:
        cap.release()
        cv.destroyAllWindows()

cap.release()
cv.destroyAllWindows()