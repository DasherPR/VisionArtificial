import cv2
import numpy as np

#C:\Users\Usuario\AppData\Local\Programs\Python\Python38\Lib\site-packages\cv2\data
#faceClassif = cv2.CascadeClassifier('Data/haarcascade_frontalface_default.xml')

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

roi = (0,0,0,0);

faceClassif = cv2.CascadeClassifier (cv2.data.haarcascades + 'haarcascade_frontalface_default.xml' )
image = cv2.imread('Images/hp2.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

faces = faceClassif.detectMultiScale(gray,
  scaleFactor=1.18,
  minNeighbors=5,
  minSize=(20,20),
  maxSize=(300,300))

for (x,y,w,h) in faces:
  cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)
  roi = (x,y,w,h);
  copia = np.copy(image)
  result = pixelate_image_roi(copia, 8,roi)
  image = result;


cv2.imshow('image',image)
cv2.waitKey(0)
cv2.destroyAllWindows()