import cv2
import numpy as np

################################################
### DETECCIÓN COLOR ################
####################################




imagen = cv2.imread('Images/isa1.png'); #Cargo la imagen
LimiteInferior = np.array([100,100,20],np.uint8); #Limite H
LimiteSuperior = np.array([125,255,255],np.uint8); #Limite S
#Los limites que hacemos son un vector con los valores que asignamos, cada uno con los limites hsv de los colores que uqeremos reconocer

"""
frameHSV = cv2.cvtColor(imagen,cv2.COLOR_BGR2HSV) #Transformo la imagen en HSV
mask = cv2.inRange(frameHSV,LimiteInferior,LimiteSuperior) #Genero una mascara , umbralizando y colocando en 1 solo los pixeles dentro de los limites
cv2.imshow('Mascara',mask)
cv2.waitKey(0)
contornos, y = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) #Calculamos los contornos
 #Otras opciones para la recuperación de contornos - Investigar la diferencia
    #cv2.RETR_LIST
    # cv2.RETR_CCOMP
    # cv2.RETR_TREE
cv2.drawContours(imagen, contornos, -1, (0,0,255), 3) #Dibujamos los contornos
cv2.imshow('imagen',imagen)
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

