## OPEN CV ##
import cv2 #! Es la segunda versión porque la anterior dejo de estar usada !#
import numpy as np

#*Cargamos la imagen*#

imagenbgr = cv2.imread('images/img1.jpg'); #Cargamos la imagen en RGB#

#* Para mostrar la imagen necesitamos dos argumentos, e, lprimero es el nombre de la ventana y la segunda es la imagen*#
cv2.imshow('Imagen BGR', imagenbgr);
cv2.waitKey(0); #Esperamos a que se presione una tecla para continuar. 0 significa que espera indefinidamente#

#*Convertimos a escala de grises*#
gray = cv2.cvtColor(imagenbgr, cv2.COLOR_BGR2GRAY); # El primer argumento es la imagen en BGR, el segundo es la conversion a escala de grises en este caso#
cv2.imshow('Imagen grises', gray); #Mostramos la imagen en escala de grises#  #
cv2.waitKey(0);

##Informacion de la imagen
#Vamos a mostrar ancho, alto y canales
print("tamaño: {} bytes".format(imagenbgr.size));
print("alto: {} pixels".format(imagenbgr.shape[0]));
print("ancho: {} pixels".format(imagenbgr.shape[1]));
print("canales: {}".format(imagenbgr.shape[2]));

#Mostremos el tamaño de la imagen en gris en bytes
print("tamaño de la imagen en gris: {} bytes".format(gray.size));

#Para separar por canales de color la imagen#
blue = imagenbgr[:,:,0];
green = imagenbgr[:,:,1];
red = imagenbgr[:,:,2];

#Ahora vamos a mostrar cada canal individualmente
cv2.imshow('Canal azul', blue);
cv2.waitKey(0);
cv2.imshow('Canal verde', green);
cv2.waitKey(0);
cv2.imshow('Canal rojo', red);
cv2.waitKey(0);
cv2.destroyAllWindows(); #Cerramos todas las ventanas después de usarlas#

#Si quisieramos mostrar la matriz en la consola hariamos: #
print("Roja {}, Verde{}, Azul{}".format(red,green,blue));

### OPERACIONES CON IMAGENES ###
suma = imagenbgr + 100;

#Mostramos la imagen en la pantalla

cv2.imshow('Imagen suma', suma);
cv2.waitKey(0);

resta = imagenbgr - 100;

cv2.imshow('Imagen resta', resta);
cv2.waitKey(0);

##Ahora podemos modificar cada color por separado y reconstruir la imagen##

bluemod = blue+2;
greenmod = green-5;
redmod = red*0.5;

Modificada =imagenbgr.copy();
Modificada[:,:,0]=bluemod;
Modificada[:,:,1]=greenmod;
Modificada[:,:,2]=redmod;
cv2.imshow('Imagen modificada', Modificada);
cv2.waitKey(0);


#Filtros derivativos

laplacianFilt = cv2.Laplacian(gray, cv2.CV_8U);
cv2.imshow('Filtro Laplaciano', laplacianFilt);
cv2.waitKey(0);

sobelFilt = cv2.Sobel(gray, ddepth=cv2.CV_8U, dx=1, dy=1, ksize=3);
cv2.imshow('Filtro Sobel', sobelFilt);
cv2.waitKey(0);

CannyFilt = cv2.Canny(gray, 100, 200);
cv2.imshow('Filtro Canny', CannyFilt);
cv2.waitKey(0);
