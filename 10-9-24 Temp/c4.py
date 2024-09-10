import cv2
import numpy as np

################################################
### DETECCIÓN COLOR ################
####################################




#imagen = cv2.imread('Images/imagen.jpg')
LimiteInferior = np.array([30,50,0],np.uint8)
LimiteSuperior = np.array([90,255,180],np.uint8)


#frameHSV = cv2.cvtColor(imagen,cv2.COLOR_BGR2HSV)
#mask = cv2.inRange(frameHSV,LimiteInferior,LimiteSuperior)
#contornos, y = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
 #Otras opciones para la recuperación de contornos - Investigar la diferencia
    #cv2.RETR_LIST
    # cv2.RETR_CCOMP*
    # cv2.RETR_TREE

"""
cv2.drawContours(imagen, contornos, -1, (0,0,255), 3)
cv2.imshow('Imagen',imagen)
cv2.waitKey(0)
"""

cap = cv2.VideoCapture(0)
while True:
  ret,frame = cap.read()
  if ret==True:
    frameHSV = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(frameHSV,LimiteInferior,LimiteSuperior) ## crea una mascara en la que los pixeles que están en los límites se vuelven blancos y los demás negros 
    contornos, y = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    cv2.drawContours(frame, contornos, -1, (0,0,255), 3)

    cv2.imshow('maskAzul',mask)
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('s'): #Si se presiona la letra s
      break
cap.release()
cv2.destroyAllWindows()

