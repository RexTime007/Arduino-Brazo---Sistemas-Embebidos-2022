import os
import cv2 as cv
import numpy as np
dataPath = 'rostros/'
nombres = os.listdir(dataPath)
print("Nombres: ", nombres)

labels = []
faceData = []
label = 0

for n in nombres:
    personalPath = dataPath + n
    print("PersonalPath: ", personalPath)
    for file in os.listdir(personalPath):
        print("Rostro: ", file)
        labels.append(label)
        faceData.append(cv.imread(personalPath + '/' + file, 0))
    label += 1
face_recognizer = cv.face.LBPHFaceRecognizer_create()
#entrenamiento 
print("Entrenando...")
face_recognizer.train(faceData, np.array(labels))
#almacenar el modelo
face_recognizer.save('MoneloLBPHF.yaml')
print("Entrenamiento terminado")   