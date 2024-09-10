import cv2
import numpy as np


def imageprocess(mask):
  #Proceso de erosion:

    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
    eroded = cv2.erode(mask,kernel,iterations=2)
    filtrada= cv2.medianBlur(eroded, 5) #filtro mediana
    kernel2 = cv2.getStructuringElement(cv2.MORPH_RECT,(15,5))

    dilated = cv2.dilate(filtrada,kernel2,iterations=2)

    return dilated
    


LimiteInferior = np.array([100,100,20],np.uint8)
LimiteSuperior = np.array([125,255,255],np.uint8)


captura = cv2.VideoCapture(0)  #El cero es el número de la cámara conectada al equipo
while (captura.isOpened()):
  ret, frame = captura.read()
  if ret==True:
    frameHSV = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(frameHSV,LimiteInferior,LimiteSuperior)
    procesada = imageprocess(mask)
    contornos, y = cv2.findContours(procesada, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for c in contornos:
       area = cv2.contourArea(c)
       if area>10000:
        x,y,w,h = cv2.boundingRect(c) 
        cv2.rectangle(frame, (x, y), (x+w, y+h),(0,0,255), 2) 
        #cv2.drawContours(frame, contornos, -1, (0,0,255), 3)
        cv2.circle(frame, (int(x+w/2), int(y+h/2)), 2,(0,255,255), 3)
        cv2.imshow('video', frame)  
    if cv2.waitKey(1) & 0xFF == ord('s'):
      break
  else: break 
captura.release()
cv2.destroyAllWindows()






