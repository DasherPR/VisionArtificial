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

img = cv2.imread('Images/isa1.png')
cv2.imshow("img",img)
cv2.waitKey(0)
copia = np.copy(img)

roi=(200,100,350,250)

result = pixelate_image_roi(copia, 15,roi)

cv2.imshow("pixelada",result)
cv2.waitKey(0)
cv2.imshow("img",img)
cv2.waitKey(0)