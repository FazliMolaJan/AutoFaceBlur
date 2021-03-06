# Source https://pysource.com/2018/10/01/face-detection-using-haar-cascades-opencv-3-4-with-python-3-tutorial-37/

# Importa as bibliotecas do openCV e do Numpy
import cv2
import numpy as np

import time

# Captura a imagem da webcam
cap = cv2.VideoCapture(0)
# Importa o modelo xml do cascade de face frontal
frontal_face_cascade = cv2.CascadeClassifier("haarcascades/haarcascade_frontalface_default.xml")

# Abre uma janela
cv2.namedWindow("Frame", cv2.WINDOW_NORMAL)

while True:
    # Conta o tempo de inicio do ciclo
    tempo_inicio = time.time()
    # Le um frame da camera
    ret , frame = cap.read()
    # Transforma em escala de cinza (melhor para o reconheciento vai haar cascade)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Detecta as faces de frente
    front_faces = frontal_face_cascade.detectMultiScale(gray, 1.3, 3)
  
    # Desenha quadrados verdes sobre todas as faces frontais
    for rect in front_faces:
        (x, y, w, h) = rect
        frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Conta o tempo de fim do ciclo
    tempo_fim = time.time()
    # Calcula FPS (frames por segundo)
    fps = 1/(tempo_fim - tempo_inicio)

    # Coloca o FPS na tela
    cv2.putText(frame, str(fps) ,(10,30), cv2.FONT_HERSHEY_SIMPLEX, 0.5,(255,0,255),2,cv2.LINE_AA)
    # Mostra o frame com eventuais rostos detectados
    cv2.imshow("Frame", frame)
    # Se pressionar Esc ( = key 27), fecha a janela
    key = cv2.waitKey(1)
    if key == 27:
        break
    
# Libera a camera e fecha as janelas
cap.release()
cv2.destroyAllWindows()