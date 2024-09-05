import cv2


imagen = cv2.imread('Images/Moneda.png')

grises = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
HSVimage = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)


cv2.imshow("Gris",grises)
cv2.waitKey(0)


H=HSVimage[:,:,0]

cv2.imshow("H",H)
cv2.waitKey(0)

S=HSVimage[:,:,1]
cv2.imshow("S",S)
cv2.waitKey(0)

V=HSVimage[:,:,2]
cv2.imshow("V",V)
cv2.waitKey(0)


_,binarizada =  cv2.threshold(S, 140, 255, cv2.THRESH_OTSU)

cv2.imshow('binarizada', binarizada)
cv2.waitKey(0)

kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(3, 3))
dilated = cv2.dilate(binarizada,kernel)


cv2.imshow('dilated', dilated)
cv2.waitKey(0)

filtrada= cv2.medianBlur(dilated, 3) 
cv2.imshow('filtrada', filtrada)
cv2.waitKey(0)

contornos,_ = cv2.findContours(filtrada, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) 
font = cv2.FONT_HERSHEY_SIMPLEX

mensaje = 'Numero de Objetos:' + str(len(contornos))
cv2.putText(imagen,mensaje,(10,50),font,0.75,
    (255,0,0),2,cv2.LINE_AA)
for c in contornos:
  cv2.drawContours(imagen, [c], 0, (255,0,0),2)
  cv2.imshow('Imagen', imagen)
  cv2.waitKey(0)
    
cv2.destroyAllWindows()


