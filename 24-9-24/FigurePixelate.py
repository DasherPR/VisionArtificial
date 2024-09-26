import cv2
import numpy as np

def pixelate_image(image, pixel_size):
    # Obtener las dimensiones de la imagen
    height, width = image.shape[:2]

    # Dividir la imagen en bloques de tamaño 'pixel_size'
    for y in range(0, height, pixel_size):
        for x in range(0, width, pixel_size):
            # Obtener el bloque en el área actual
            block = image[y:y + pixel_size, x:x + pixel_size]

            # Calcular el color promedio en el bloque
            average_color = block.mean(axis=(0, 1))

            # Asignar el color promedio a todo el bloque
            image[y:y + pixel_size, x:x + pixel_size] = average_color

    return image


def pixelate_image_roi(image, pixel_size,roi):
        
    color = np.copy(image)
    image = pixelate_image(image, pixel_size)
    color[roi[1]:roi[1] + roi[3], roi[0]:roi[0] + roi[2]] = image[roi[1]:roi[1] + roi[3], roi[0]:roi[0] + roi[2]]
    
    return color


imagen = cv2.imread('Images/pruebita.png')
imagenHSV = cv2.cvtColor(imagen,cv2.COLOR_BGR2HSV);
gray = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
canny = cv2.Canny(gray, 10, 150)
canny = cv2.dilate(canny, None, iterations=1)
canny = cv2.erode(canny, None, iterations=1)

contornos,_ = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

roi = (0,0,0,0);

for c in contornos:
    length = cv2.arcLength(c,True) #arcLength = perimeter
    epsilon = 0.01*length
    approx = cv2.approxPolyDP(c,epsilon,True) #  algoritmo de Douglas-Peucker - https://en.wikipedia.org/wiki/Ramer%E2%80%93Douglas%E2%80%93Peucker_algorithm
    if len(approx)>10:
        print(len(approx))
        x,y,w,h = cv2.boundingRect(approx)
        roi = (x,y,w,h);
        copia = np.copy(imagen)
        result = pixelate_image_roi(copia, 8,roi)
        imagen = result;


cv2.imshow('resultado',result)
cv2.waitKey(0)