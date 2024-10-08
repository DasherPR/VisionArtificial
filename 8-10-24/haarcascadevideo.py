import cv2
#C:\Users\Usuario\AppData\Local\Programs\Python\Python38\Lib\site-packages\cv2\data
#faceClassif = cv2.CascadeClassifier('Data/haarcascade_frontalface_default.xml')
faceClassif = cv2.CascadeClassifier (cv2.data.haarcascades + 'haarcascade_frontalface_default.xml' )
image = cv2.imread('Images/Luna.png')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)





captura = cv2.VideoCapture(0)  #El cero es el número de la cámara conectada al equipo
while (captura.isOpened()):
  ret, frame = captura.read()
  gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  faces = faceClassif.detectMultiScale(gray,
  scaleFactor=1.1,
  minNeighbors=6,
  minSize=(10,10),
  maxSize=(300,300))
  
  if ret==True:
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)

    cv2.imshow('video', frame)  
    if cv2.waitKey(1) & 0xFF == ord('s'):
      break
  else: break 
captura.release()
cv2.destroyAllWindows()

