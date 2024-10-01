import cv2;
import numpy as np;



#Funciones para usar abajo:

def pixelarImg(image, pixel_size):
    # Obtengo las dimensiones de la imagen
    height, width = image.shape[:2]

    # Se divide toda la imagen en bloques que tengan el tamaño que determiné
    for y in range(0, height, pixel_size):
        for x in range(0, width, pixel_size):
            # Obtengo el bloque correspondiente al area.
            block = image[y:y + pixel_size, x:x + pixel_size]

            # Se calcula el color promedio del bloque para luego asignarlo
            average_color = block.mean(axis=(0, 1))
            image[y:y + pixel_size, x:x + pixel_size] = average_color

    return image

def pixelarImg_roi(image, pixel_size,roi):
        
    color = np.copy(image)
    image = pixelarImg(image, pixel_size)
    color[roi[1]:roi[1] + roi[3], roi[0]:roi[0] + roi[2]] = image[roi[1]:roi[1] + roi[3], roi[0]:roi[0] + roi[2]]
    
    return color


#Primero leo la imagen pasandola a HSV y escala de grises
img = cv2.imread("Images/imgp2.png");
imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV);
filtGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY);
filtCanny = cv2.Canny(filtGray, 10, 150);
filtCanny = cv2.dilate(filtCanny, None, iterations=1);
filtCanny = cv2.erode(filtCanny, None, iterations=1);

imagen = np.copy(img)

#Para detectar el color rojo: 
redBajo1 = np.array([0, 100, 20], np.uint8)
redAlto1 = np.array([8, 255, 255], np.uint8)
redBajo2=np.array([175, 100, 20], np.uint8)
redAlto2=np.array([179, 255, 255], np.uint8)
maskRed1 = cv2.inRange(imgHSV, redBajo1, redAlto1)
maskRed2 = cv2.inRange(imgHSV, redBajo2, redAlto2)
maskR = cv2.add(maskRed1, maskRed2)

#Para detectar el color Verde
LimiteInferior = np.array([34,100,20],np.uint8)
LimiteSuperior = np.array([80,255,255],np.uint8)
maskG = cv2.inRange(imgHSV, LimiteInferior, LimiteSuperior);

#Para detectar el color azul:

LimiteInferior = np.array([81,100,20],np.uint8)
LimiteSuperior = np.array([125,255,255],np.uint8)
maskB = cv2.inRange(imgHSV, LimiteInferior, LimiteSuperior);

#Para separar los contornos segun el color de la imagen:


contornosB,_ = cv2.findContours(maskB, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE);
contornosG,_ = cv2.findContours(maskG, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE);
contornosR,_ = cv2.findContours(maskR, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE);

#Para contar las figuras rojas:

RTriang = 0;
RCirc = 0;
RRect = 0;

for c in contornosR:
    length = cv2.arcLength(c,True) 
    epsilon = 0.01*length
    approx = cv2.approxPolyDP(c,epsilon,True) 
    x,y,w,h = cv2.boundingRect(approx)
    if len(approx)==3:
      cv2.putText(img,'Triangulo', (x,y-5),1,1.5,(0,255,0),2)
      RTriang += 1;
    if len(approx)==4:
        cv2.putText(img,'Rectangulo', (x,y-5),1,1.5,(0,255,0),2)
        RRect += 1;
    if len(approx)>10:
      cv2.putText(img,'Circulo', (x,y-5),1,1.5,(0,255,0),2)
      RCirc += 1;
    cv2.drawContours(img, [approx], 0, (0,255,0),2)
    cv2.imshow('image',img)
    cv2.waitKey(0)

print("El numero de Circulos Rojos es: " + str(RCirc));
print("El numero de Rectangulos o cuadrados rojos es: " + str(RRect));
print ("El numero de Triangulos rojos es: " + str(RTriang));

#Para pixelar las figuras verdes:

roi = (0,0,0,0);

for c in contornosG:
    length = cv2.arcLength(c,True)
    epsilon = 0.01*length
    approx = cv2.approxPolyDP(c,epsilon,True) 
    x,y,w,h = cv2.boundingRect(approx)
    roi = (x,y,w,h);
    copia = np.copy(imagen)
    result = pixelarImg_roi(copia, 8,roi)
    imagen = result;


cv2.imshow('resultado',result)
cv2.waitKey(0)

# Para contar las imagenes azules que superen un determinado umbral de Area:

TotalFigB = 0;

for c in contornosB:
    area = cv2.contourArea(c)
    if area>10000:
        TotalFigB += 1;
    
print("El numero total de figuras azules con area mayor a 10000px es de: " + str(TotalFigB));




