import cv2
import numpy as np
from mtcnn import MTCNN
#from scipy.spatial.distance import cosine
from scipy.spatial.distance import euclidean

# Cargar En la que se quiere buscar
image = cv2.imread("Images/twoPeople.jpeg")
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # Convertir la imagen a RGB (MTCNN requiere imágenes en RGB)

# Crear una instancia del detector MTCNN
detector = MTCNN()

# Detectar rostros en la imagen
faces = detector.detect_faces(image_rgb)

# Cargar la imagen del rostro que se quiere reconocer

reference_face = cv2.imread("Images/false_img2.jpg")
reference_face_rgb = cv2.cvtColor(reference_face, cv2.COLOR_BGR2RGB)
faces2 = detector.detect_faces(reference_face_rgb)

# Extraer características del rostro de referencia
reference_face_features = detector.detect_faces(reference_face_rgb)[0]['keypoints']

threshold = 0;

# Extraer características de los rostros detectados y comparar con el rostro de referencia
for face in faces:
    face_keypoints = face['keypoints']
    
    # Convierte los valores en arrays numpy, aplana y asegura que sean flotantes
    face_keypoints_values = np.array(list(face_keypoints.values()), dtype=np.float64).flatten()
    reference_face_features_values = np.array(list(reference_face_features.values()), dtype=np.float64).flatten()

    # Reescalar los vectores antes de la normalización
    face_keypoints_values = face_keypoints_values / np.max(np.abs(face_keypoints_values))
    reference_face_features_values = reference_face_features_values / np.max(np.abs(reference_face_features_values))

    # Normaliza los vectores
    face_keypoints_values /= np.linalg.norm(face_keypoints_values)
    reference_face_features_values /= np.linalg.norm(reference_face_features_values)

    distance = euclidean(np.array(list(face_keypoints.values())).flatten(), np.array(list(reference_face_features.values())).flatten())
    print(distance)
    
    # Definir un umbral para determinar si los rostros son similares
    threshold = 300
    
    # Si la distancia es menor que el umbral, se considera que los rostros son similares
    if distance < threshold:
        x, y, w, h = face['box']  # Obtener las coordenadas y dimensiones del rectángulo del rostro
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)  # Dibujar el rectángulo

    for face in faces2:
        if distance < threshold:
            x, y, w, h = face['box']  # Obtener las coordenadas y dimensiones del rectángulo del rostro
            cv2.rectangle(reference_face, (x, y), (x+w, y+h), (0, 255, 0), 2)  # Dibujar el rectángulo

# Mostrar la imagen con los rostros detectados
cv2.imshow('Detected Faces', image)
cv2.waitKey(0)
cv2.imshow('Detected Faces', reference_face)
cv2.waitKey(0)
cv2.destroyAllWindows()