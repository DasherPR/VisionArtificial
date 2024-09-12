import cv2
import numpy as np



def imageprocess(mask):
  #Proceso de erosion:

    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
    eroded = cv2.erode(mask,kernel,iterations=2)
    filtrada= cv2.medianBlur(eroded, 5) #filtro mediana
    kernel2 = cv2.getStructuringElement(cv2.MORPH_RECT,(15,5))

    dilated = cv2.dilate(filtrada,kernel2,iterations=2)

    return dilated
def calcula_extremos(frame,x,y,w,h):

  frameHSV = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
  procesada = imageprocess(mask)
  sumax=0
  sumay=0
  contador=0
  limiteH=int(x+w/10)
  limiteV=y+h
  for i in range(x,limiteH): #Este for sirve para buscar el sitio en el que hay partes del objeto que se quiere reconocer.
    for j in range (y,limiteV):
      if procesada[j,i]==255:
        sumax+=i
        sumay+=j
        contador+=1
  if (contador!=0):  
     
    xpromIzq=int(sumax/contador) #Una vez encontrado todos los pixeles buscamos una coordenadas promedio para dibujar el circulo.
    ypromIzq=int(sumay/contador)
    cv2.circle(frame, (xpromIzq, ypromIzq), 2,(0,255,255), 5)
  sumax=0
  sumay=0
  contador=0
  limiteH=int(x+w*0.9)
  limiteV=y+h
  for i in range(limiteH,x+w): #Repetimos el proceso pero desde el 90% del rectangulo.
    for j in range (y,limiteV):
      if procesada[j,i]==255:
        sumax+=i
        sumay+=j
        contador+=1
  if (contador!=0):      
    xpromDer=int(sumax/contador)
    ypromDer=int(sumay/contador)
    cv2.circle(frame, (xpromDer, ypromDer), 2,(0,0,255), 5)

  difx= xpromDer - xpromIzq # Aqui calculamos las diferencas para poder calcular el angulo.
  dify= ypromDer - ypromIzq
  angulo = np.arctan(dify/difx) #Calculamos el angulo en base a los dos catetos que ya tenemos. 
  angulo = angulo*180/np.pi
  print("angulo", angulo)
  frame = cv2.line(frame, (xpromIzq, ypromIzq), (xpromDer, ypromDer), (0,255,255), 5) 

# Ahora vamos a hacer un codigo que permita escoger al usuario el color del elemento que usara.

print("Hola, Bienvenido al programa para controlar un motor.");

while True:
  colAsk = input("Por favor escriba R para usar un objeto rojo, escriba A para usar un objeto azul y escriba AM para usar un objeto amarillo \n");
  colAsk = colAsk.upper()
  if colAsk == "A" or colAsk == "R" or colAsk == "AM":
    break
  else:
    print("Esa opcion no es valida")

if colAsk == "A":
  LimiteInferior = np.array([100,100,20],np.uint8)
  LimiteSuperior = np.array([125,255,255],np.uint8)
elif colAsk == "AM":
  LimiteInferior = np.array([25,100,20],np.uint8)
  LimiteSuperior = np.array([35,255,255],np.uint8)









captura = cv2.VideoCapture(0)  #El cero es el número de la cámara conectada al equipo
while (captura.isOpened()):
  ret, frame = captura.read()
  if ret==True:
    if colAsk == "A" or colAsk == "AM":
      frameHSV = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
      mask = cv2.inRange(frameHSV,LimiteInferior,LimiteSuperior)
      procesada = imageprocess(mask)
      contornos, y = cv2.findContours(procesada, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    elif colAsk == "R":
      redBajo1 = np.array([0, 100, 20], np.uint8)
      redAlto1 = np.array([8, 255, 255], np.uint8)
      redBajo2=np.array([175, 100, 20], np.uint8)
      redAlto2=np.array([179, 255, 255], np.uint8)
      frameHSV = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
      maskRed1 = cv2.inRange(frameHSV, redBajo1, redAlto1)
      maskRed2 = cv2.inRange(frameHSV, redBajo2, redAlto2)
      maskRedFinal = cv2.add(maskRed1, maskRed2)
      procesada = imageprocess(maskRedFinal)
      contornos, y = cv2.findContours(procesada, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
      mask = maskRedFinal
    for c in contornos:
      area = cv2.contourArea(c)
      if(area>10000):  
        #cv2.drawContours(frame, contornos, -1, (0,0,255), 3)
        x, y, w, h = cv2.boundingRect(c) ## Nueva
        cv2.rectangle(frame, (x, y), (x+w, y+h),(0,255,0), 3)
        cv2.circle(frame, (int(x+w/2), int(y+h/2)), 2,(0,0,255), 5)
        calcula_extremos(frame,x,y,w,h)

      cv2.imshow('video', frame)  
    if cv2.waitKey(1) & 0xFF == ord('s'):
      break
  else: break 
captura.release()
cv2.destroyAllWindows()




