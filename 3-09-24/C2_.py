
import cv2


#Instrucción para cargar una imagen
imagen = cv2.imread('Images/img1.jpg');
imagen2 = imagen.copy(); # Se usa .copy para crear una copia de la imagen original y que esta no se vea afectada por los cambios en al copia

#Mostramos la imagen
cv2.imshow('Imagen Cargada',imagen);


## Mediante las funciones de Open Cv es posible hacer algunos dibujos básicos
# sobre las imágenes, esto será util en aplicaciones posteriores:

alto, ancho, _ = imagen.shape #se calculan las dimensiones de la imagen, la linea de la tercera 
                            #posicion significa que no nos importa el canal de color o si lo usaramos en otro programa esa variable.
color = [0, 255, 255]; # Si queremos dar color a algo se lo solemos entregar como una lista de tres valores BGR (Blue, Green, Red), por lo que aqui es el color rojo.
grosor = 2;


#la sintaxis es la siguiente:
#imagen = cv2.line(imagen, puntoInicial, puntoFinal, color, grosor) #Se dibuja una linea en la imagen con este codigo

imagen = cv2.line(imagen, (0, 0), (ancho, alto), color, grosor); # aqui aplicamos el codigo para dibujar una linea horizontal en la parte superior de la imagen
cv2.imshow('Linea', imagen); #tengo que mostrar la imagen con la linea dibujada
cv2.waitKey(0);


cuadricula = 80 #Ahora podemos hacer una cuadricula en la imagen

for x in range(0, ancho, cuadricula):
    imagen = cv2.line(imagen, (x, 0), (x, alto), color, grosor) #Dibujamos lineas verticales
for y in range(0, alto, cuadricula):
    imagen = cv2.line(imagen, (0, y), (ancho, y), color, grosor) #dibujamos lineas horizontales

cv2.imshow('cuadricula', imagen)
cv2.waitKey(0)


cv2.arrowedLine(imagen, (200, 100), (300, 150), (255,0,0), grosor) #Creamos una flecha en la imagen
cv2.imshow('cuadricula', imagen)
cv2.waitKey(0)

## RECTÁNGULOS

color = (0, 0, 255) #Vuelvo a definir un color rojo
grosor = 4
RectanguloXInicial, RectanguloXFinal = 300, 550 #Defino los puntos de inicio y fin del rectangulo.
RectanguloYInicial, RectanguloYFinal = 20, 220


cv2.rectangle(imagen2, (RectanguloXInicial, RectanguloYInicial), (RectanguloXFinal, RectanguloYFinal),color, grosor) #Dibujamos el rectangulo en la imagen2

cv2.imshow('cuadro', imagen2)
cv2.waitKey(0)

## CIRCULOS Y ELIPSES

#SINTAXIS

# cv2.circle(imagen, (centro_x, centro_y), radio,color, grosor) #!Con este codigo se dibuja una linea en el codigo para dibujar un circulo en la imagen



imagen = cv2.imread('Images/img1.jpg') 

alto, ancho, canales = imagen.shape
color = (40, 0, 255)
incremento_radio = 40
grosor = 10

centro_x = int(ancho/2) #calculamos el centro en x de la imagen
centro_y = int(alto/2) #calculamos el centro en y de la imagen
#Ambos son convertidos a enteros para que la operacion sea exacta, no sera exactamente la mitad pero no es demasiado importante para este caso.


for radio in range(0, int(alto/2), incremento_radio):
    cv2.circle(imagen, (centro_x, centro_y), radio,color, grosor)

cv2.imshow('Circulos', imagen)
cv2.waitKey(0)

## TEXTOS
# cv2.putText(img, "Texto", posicionDeInicio, fuente, escala, color, grosor)
# Se puede escribir en varias fuentes. 

color = (0, 255, 0)
grosor = 4
fuente = cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
escala = 2


cv2.putText(imagen, "Prohibido herir a los gatos", (80, 60), fuente, escala, (255,0,0), grosor)

cv2.imshow('Texto', imagen)
cv2.waitKey(0)