import cv2
import numpy as np


imagen = cv2.imread('Images/pruebita.png')
imagenHSV = cv2.cvtColor(imagen,cv2.COLOR_BGR2HSV);
gray = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
canny = cv2.Canny(gray, 10, 150)
canny = cv2.dilate(canny, None, iterations=1)
canny = cv2.erode(canny, None, iterations=1)

redBajo1 = np.array([0, 100, 20], np.uint8)
redAlto1 = np.array([8, 255, 255], np.uint8)
redBajo2=np.array([175, 100, 20], np.uint8)
redAlto2=np.array([179, 255, 255], np.uint8)
maskRed1 = cv2.inRange(imagenHSV, redBajo1, redAlto1)
maskRed2 = cv2.inRange(imagenHSV, redBajo2, redAlto2)
mask = cv2.add(maskRed1, maskRed2)

LimiteInferior = np.array([25,100,20],np.uint8)
LimiteSuperior = np.array([33,255,255],np.uint8)

maskY = cv2.inRange(imagenHSV, LimiteInferior, LimiteSuperior);

LimiteInferior = np.array([81,100,20],np.uint8)
LimiteSuperior = np.array([125,255,255],np.uint8)
maskB = cv2.inRange(imagenHSV, LimiteInferior, LimiteSuperior);

LimiteInferior = np.array([34,100,20],np.uint8)
LimiteSuperior = np.array([80,255,255],np.uint8)
maskG = cv2.inRange(imagenHSV, LimiteInferior, LimiteSuperior);



cv2.imshow('image',mask)
cv2.waitKey(0)

contornos,_ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contornosY,_ = cv2.findContours(maskY, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contornosB,_ = cv2.findContours(maskB, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contornosG,_ = cv2.findContours(maskG, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
circ= [0,0,0,0];
tria = [0,0,0,0];
rect = [0,0,0,0];
cuad = [0,0,0,0];
pent = [0,0,0,0];
hex = [0,0,0,0];

for c in contornos:
    length = cv2.arcLength(c,True) #arcLength = perimeter
    epsilon = 0.01*length
    approx = cv2.approxPolyDP(c,epsilon,True) #  algoritmo de Douglas-Peucker - https://en.wikipedia.org/wiki/Ramer%E2%80%93Douglas%E2%80%93Peucker_algorithm
    print(len(approx))
    x,y,w,h = cv2.boundingRect(approx)
    if len(approx)==3:
      cv2.putText(imagen,'Triangulo', (x,y-5),1,1.5,(0,255,0),2)
      tria[2] += 1;
    if len(approx)==4:
      relacionAspecto = float(w)/h
      print('aspect_ratio= ', relacionAspecto)
      if relacionAspecto == 1:
        cv2.putText(imagen,'Cuadrado', (x,y-5),1,1.5,(0,255,0),2)
        cuad[2] += 1;
      else:
        cv2.putText(imagen,'Rectangulo', (x,y-5),1,1.5,(0,255,0),2)
        rect[2] += 1;
    if len(approx)==5:
      cv2.putText(imagen,'Pentagono', (x,y-5),1,1.5,(0,255,0),2)
      pent[2] +=1;
    if len(approx)==6:
      cv2.putText(imagen,'Hexagono', (x,y-5),1,1.5,(0,255,0),2)
      hex[2] += 1;
    if len(approx)>10:
      cv2.putText(imagen,'Circulo', (x,y-5),1,1.5,(0,255,0),2)
      circ[2] += 1;
    cv2.drawContours(imagen, [approx], 0, (0,255,0),2)
    cv2.imshow('image',imagen)
    cv2.waitKey(0)


for c in contornosY:
    length = cv2.arcLength(c,True) #arcLength = perimeter
    epsilon = 0.01*length
    approx = cv2.approxPolyDP(c,epsilon,True) #  algoritmo de Douglas-Peucker - https://en.wikipedia.org/wiki/Ramer%E2%80%93Douglas%E2%80%93Peucker_algorithm
    print(len(approx))
    x,y,w,h = cv2.boundingRect(approx)
    if len(approx)==3:
      cv2.putText(imagen,'Triangulo', (x,y-5),1,1.5,(0,255,0),2)
      tria[3] += 1;
    if len(approx)==4:
      relacionAspecto = float(w)/h
      print('aspect_ratio= ', relacionAspecto)
      if relacionAspecto == 1:
        cv2.putText(imagen,'Cuadrado', (x,y-5),1,1.5,(0,255,0),2)
        cuad[3] += 1;
      else:
        cv2.putText(imagen,'Rectangulo', (x,y-5),1,1.5,(0,255,0),2)
        rect[3] += 1;
    if len(approx)==5:
      cv2.putText(imagen,'Pentagono', (x,y-5),1,1.5,(0,255,0),2)
      pent[3] +=1;
    if len(approx)==6:
      cv2.putText(imagen,'Hexagono', (x,y-5),1,1.5,(0,255,0),2)
      hex[3] += 1;
    if len(approx)>10:
      cv2.putText(imagen,'Circulo', (x,y-5),1,1.5,(0,255,0),2)
      circ[3] += 1;
    cv2.drawContours(imagen, [approx], 0, (0,255,0),2)
    cv2.imshow('image',imagen)
    cv2.waitKey(0)

for c in contornosB:
    length = cv2.arcLength(c,True) #arcLength = perimeter
    epsilon = 0.01*length
    approx = cv2.approxPolyDP(c,epsilon,True) #  algoritmo de Douglas-Peucker - https://en.wikipedia.org/wiki/Ramer%E2%80%93Douglas%E2%80%93Peucker_algorithm
    print(len(approx))
    x,y,w,h = cv2.boundingRect(approx)
    if len(approx)==3:
      cv2.putText(imagen,'Triangulo', (x,y-5),1,1.5,(0,255,0),2)
      tria[0] += 1;
    if len(approx)==4:
      relacionAspecto = float(w)/h
      print('aspect_ratio= ', relacionAspecto)
      if relacionAspecto == 1:
        cv2.putText(imagen,'Cuadrado', (x,y-5),1,1.5,(0,255,0),2)
        cuad[0] += 1;
      else:
        cv2.putText(imagen,'Rectangulo', (x,y-5),1,1.5,(0,255,0),2)
        rect[0] += 1;
    if len(approx)==5:
      cv2.putText(imagen,'Pentagono', (x,y-5),1,1.5,(0,255,0),2)
      pent[0] +=1;
    if len(approx)==6:
      cv2.putText(imagen,'Hexagono', (x,y-5),1,1.5,(0,255,0),2)
      hex[0] += 1;
    if len(approx)>10:
      cv2.putText(imagen,'Circulo', (x,y-5),1,1.5,(0,255,0),2)
      circ[0] += 1;
    cv2.drawContours(imagen, [approx], 0, (0,255,0),2)
    cv2.imshow('image',imagen)
    cv2.waitKey(0)

for c in contornosG:
    length = cv2.arcLength(c,True) #arcLength = perimeter
    epsilon = 0.01*length
    approx = cv2.approxPolyDP(c,epsilon,True) #  algoritmo de Douglas-Peucker - https://en.wikipedia.org/wiki/Ramer%E2%80%93Douglas%E2%80%93Peucker_algorithm
    print(len(approx))
    x,y,w,h = cv2.boundingRect(approx)
    if len(approx)==3:
      cv2.putText(imagen,'Triangulo', (x,y-5),1,1.5,(0,255,0),2)
      tria[1] += 1;
    if len(approx)==4:
      relacionAspecto = float(w)/h
      print('aspect_ratio= ', relacionAspecto)
      if relacionAspecto == 1:
        cv2.putText(imagen,'Cuadrado', (x,y-5),1,1.5,(0,255,0),2)
        cuad[1] += 1;
      else:
        cv2.putText(imagen,'Rectangulo', (x,y-5),1,1.5,(0,255,0),2)
        rect[1] += 1;
    if len(approx)==5:
      cv2.putText(imagen,'Pentagono', (x,y-5),1,1.5,(0,255,0),2)
      pent[1] +=1;
    if len(approx)==6:
      cv2.putText(imagen,'Hexagono', (x,y-5),1,1.5,(0,255,0),2)
      hex[1] += 1;
    if len(approx)>10:
      cv2.putText(imagen,'Circulo', (x,y-5),1,1.5,(0,255,0),2)
      circ[1] += 1;
    cv2.drawContours(imagen, [approx], 0, (0,255,0),2)
    cv2.imshow('image',imagen)
    cv2.waitKey(0)



cv2.putText(imagen,'Triangulos: '+str(tria), (0,20),1,1.5,(0,0,0),2);
cv2.putText(imagen,'Cuadrados: '+str(cuad), (0,40),1,1.5,(0,0,0),2);
cv2.putText(imagen,'Rectangulos: '+str(rect), (0,60),1,1.5,(0,0,0),2);
cv2.putText(imagen,'Pentagonos: '+str(pent), (0,80),1,1.5,(0,0,0),2);
cv2.putText(imagen,'Hexagonos: '+str(hex), (0,100),1,1.5,(0,0,0),2);
cv2.putText(imagen,'Circulos: '+str(circ), (0,120),1,1.5,(0,0,0),2);
cv2.imshow('image',imagen)
cv2.waitKey(0)
