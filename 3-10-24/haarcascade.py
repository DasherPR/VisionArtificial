import cv2
#C:\Users\Usuario\AppData\Local\Programs\Python\Python38\Lib\site-packages\cv2\data
#faceClassif = cv2.CascadeClassifier('Data/haarcascade_frontalface_default.xml')
faceClassif = cv2.CascadeClassifier (cv2.data.haarcascades + 'haarcascade_frontalface_default.xml' )
image = cv2.imread('Images/hp2.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

faces = faceClassif.detectMultiScale(gray,
  scaleFactor=1.18,
  minNeighbors=8,
  minSize=(10,10),
  maxSize=(300,300))

for (x,y,w,h) in faces:
  cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)

cv2.imshow('image',image)
cv2.waitKey(0)
cv2.destroyAllWindows()