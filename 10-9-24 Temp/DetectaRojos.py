import cv2
import numpy as np


imagen = cv2.imread('Imagenes/Colores.jpg') 
cv2.imshow('Imagen Cargada',imagen)
cv2.waitKey(0)
cv2.destroyAllWindows()

#LimiteInferior = np.array([0.581*180,0.505*255,0.492*255],np.uint8)
#LimiteSuperior = np.array([0.638*180,0.947*255,1*255],np.uint8)

#LimiteInferior = np.array([0.981*180,0.952*255,0.654*255],np.uint8)
#LimiteSuperior = np.array([0.033*180,1*255,0.840*255],np.uint8)

redBajo1 = np.array([0, 100, 20], np.uint8)
redAlto1 = np.array([8, 255, 255], np.uint8)
redBajo2=np.array([175, 100, 20], np.uint8)
redAlto2=np.array([179, 255, 255], np.uint8)

gris= cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
ImagenHSV = cv2.cvtColor(imagen,cv2.COLOR_BGR2HSV)
#mask = cv2.inRange(ImagenHSV,LimiteInferior,LimiteSuperior)
maskRed1 = cv2.inRange(ImagenHSV, redBajo1, redAlto1)
maskRed2 = cv2.inRange(ImagenHSV, redBajo2, redAlto2)
mask = cv2.add(maskRed1, maskRed2)
contornos, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(gris, contornos, -1, (0,255,0), 3)
    
cv2.imshow('maskAzul',mask)
cv2.imshow('frame',gris)
cv2.waitKey(0)
cv2.destroyAllWindows()