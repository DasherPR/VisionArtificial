import cv2
import numpy as np
import time




faceClassif = cv2.CascadeClassifier (cv2.data.haarcascades + 'haarcascade_frontalface_default.xml' )

# Intervalo de tiempo para guardar las imágenes (5 segundos)
intervalo = 30

# Contador de imágenes guardadas
count = 0

start_time = time.time() #Iniciamos el temporizador

video = cv2.VideoCapture(0)
i = 0
while True:
  ret, cap = video.read()
  if ret == False: break
  gray = cv2.cvtColor(cap, cv2.COLOR_BGR2GRAY)
  faces = faceClassif.detectMultiScale(gray,
  scaleFactor=1.12,
  minNeighbors=5,
  minSize=(10,10),
  maxSize=(300,300))
  if i == 25:
    bgGray = gray
  if i > 25:
    dif = cv2.absdiff(gray, bgGray)
    _, th = cv2.threshold(dif, 40, 255, cv2.THRESH_BINARY)
    
    contornos, _ = cv2.findContours(th, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    #cv2.drawContours(frame, cnts, -1, (0,0,255),2)        
    
    for c in contornos:
      area = cv2.contourArea(c)
      if area > 9000:
        for (x,y,w,h) in faces:
            cv2.rectangle(cap, (x,y), (x+w,y+h),(0,255,0),2)
            current_time = time.time() #Pregunta cuanto tiempo ha pasado desde el tiempo inicial
            if current_time - start_time >= intervalo: #Aquí preguntamos al programa si el tiempo actual menos el tiempo inicial cumple el intervalo
                # Crear un nombre de archivo único para la imagen
                filename = f"Cara_{count}.jpg"
                cv2.imwrite(filename, cap)
                print(f"Imagen guardada: {filename}")

                # Reiniciar el temporizador
                start_time = current_time
                count += 1
  cv2.imshow('Frame',cap)
  i = i+1
  if cv2.waitKey(30) & 0xFF == ord ('q'):
    break
video.release()