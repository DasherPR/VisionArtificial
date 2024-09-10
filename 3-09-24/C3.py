import cv2
import numpy as np

imagen = cv2.imread('Images/img1.jpg') 



### CONVERSIÓN A ESCALA DE GRISES ###########
gris= cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)


#######   Umbralización
val, binarizada1 = cv2.threshold(gris,130,255,cv2.THRESH_BINARY) #Cuando el pixel sea mayor a 130 se asignará 255
print("el umbral empleado fue:",val)
#En la anterior linea use una funcion donde 130 es el nivel umbral y 255 es el valor de pixel a asignar
#La funcion tambien me devuelve el valor del umbral utilizado

cv2.imshow('Binarizada',binarizada1)
cv2.waitKey(0)
cv2.destroyAllWindows()

#############################################
val, binarizada2 = cv2.threshold(gris,2,255,cv2.THRESH_OTSU) #asigna automáticamente el umbral
print("el umbral empleado POR otsu fue:",val)
#Este metodo eligen automaticamente el umbral cuando se utiliza el metodo de otsu, el 2 que coloque en la funcion no interesa pero hay que colocarlo.
#Aqui si nos interesa ver el umbral que utilizo

cv2.imshow('Binarizada_Otsu',binarizada2)
cv2.waitKey(0)
cv2.destroyAllWindows()



val, binarizada = cv2.threshold(gris,122,255,cv2.THRESH_BINARY) #Cuando el pixel sea mayor a 130 se asignará 255

print("el umbral empleado fue:",val)
cv2.imshow('Binarizada',binarizada)
cv2.waitKey(0)
cv2.destroyAllWindows()

######################## MORFOLOGÍA ##################
# La morfologia hace referencia a firltros morofologicos sirve para aplicarse a imagenes binarizadas 
# Ampliar las secciones blancas se conoce como dilatacion y ampliar las secciones negras se conoce como erosion (o reducir las secciones blancas)
# Esto se hace con objetivo de mejorar la imagen para momentos posteriores
kernel = cv2.getStructuringElement(cv2.MORPH_CROSS,(3, 3)) #Este es el "pincel" que se utiliza para la dilatacion y erosion, estamos seleccionando un rectangulo de 3x3
#A la vairable se le suele llamar Kernel

#Otras opciones:
#cv2.MORPH_RECT,(5,5)
#cv2.MORPH_ELLIPSE,(5,5)
#cv2.MORPH_CROSS,(5,5)

eroded = cv2.erode(binarizada,kernel) #aqui aplicamos erosion en la imagen binarizada con el kernel
cv2.imshow("Eroded Image",eroded)
cv2.waitKey(0)


dilated = cv2.dilate(binarizada,kernel) #aqui dilatamos en la imagen binarizada con el kernel
cv2.imshow("Dilated Image",dilated)
cv2.waitKey(0)


#Es comun que se nos binarice de forma incorrecta, por lo que podemos invertirla con la siguiente función
invertida=cv2.bitwise_not(eroded)
cv2.imshow("Invertida",invertida)
cv2.waitKey(0)


#El proceso de aperturación y cierre son operaciones morfológicas que se utilizan para mejorar la imagen y eliminar ruido
#Apertura hace une erosion y luego una diltacion
opening = cv2.morphologyEx(binarizada, cv2.MORPH_OPEN, kernel) 
cv2.imshow("opening",invertida)
cv2.waitKey(0)
#Cierre hace una diltación y luego una erosión
closing = cv2.morphologyEx(binarizada, cv2.MORPH_CLOSE, kernel)
cv2.imshow("closing",invertida)
cv2.waitKey(0)
#Estos procesos suelen ayudar a eliminar ruido y distorsiones en la imagen ya binarizada, por ejemplo es comun en los OCR


cv2.destroyAllWindows()
cv2.destroyAllWindows()



##################################
############ contornos ###########
##################################


#Cuando voy a dibujar contornos en una imagen lo que busco es encontrar contornos, primero necesito encontrar las coordenadas que son el contorno de un objeto.
contornos,hierarchy1 = cv2.findContours(invertida, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE) #.RETR_EXTERNAL solo nos muestra los contornos externos,.CHAIN_APPROX_SIMPLE simplifica los contornos a puntos simples
# un contorno es una lista de puntos que forman el contorno, tambien es por ello que necesitamos que el fondo sea negro y el objeto sea blanco
cv2.drawContours(imagen, contornos, -1, (0,255,0), 3) #Luego hay que dibujar los contornos en la imagen original, con -1 dibuja todos los contornos
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(imagen,"Contornos",(400,400),font,0.75, (255,0,0),2,cv2.LINE_AA)
cv2.imshow('imagen',imagen)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite("imagen2.png",imagen)  #Guardamos la imagen en disco




### Video:

captura = cv2.VideoCapture(0)  #El cero es el número de la cámara conectada al equipo
while (captura.isOpened()):
  ret, imagen = captura.read()
  if ret == True:  ## Cuando si se está capturando video
    cv2.imshow('video', imagen)
    if cv2.waitKey(1) & 0xFF == ord('s'):
      break
  else: break
captura.release()
cv2.destroyAllWindows()


