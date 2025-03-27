import cv2
import mediapipe as mp
import numpy as np

# Inicializar MediaPipe Hands
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

def distancia(p1, p2):
    return np.linalg.norm(np.array(p1) - np.array(p2))

with mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7) as hands:
    agarrando = False
    objeto_x, objeto_y = 300, 200  # Posición inicial del objeto

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.flip(frame, 1)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(rgb_frame)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                # Obtener las coordenadas del índice y el pulgar
                idx_x = int(hand_landmarks.landmark[8].x * frame.shape[1])
                idx_y = int(hand_landmarks.landmark[8].y * frame.shape[0])
                thumb_x = int(hand_landmarks.landmark[4].x * frame.shape[1])
                thumb_y = int(hand_landmarks.landmark[4].y * frame.shape[0])

                # Dibujar un círculo en el índice y el pulgar
                cv2.circle(frame, (idx_x, idx_y), 10, (0, 255, 0), -1)
                cv2.circle(frame, (thumb_x, thumb_y), 10, (0, 255, 0), -1)

                # Detectar si los dedos están juntos (agarre)
                if distancia((idx_x, idx_y), (thumb_x, thumb_y)) < 50:
                    agarrando = True
                else:
                    agarrando = False

                # Mover el objeto si se está agarrando
                if agarrando:
                    objeto_x, objeto_y = idx_x, idx_y

        # Dibujar el objeto virtual
        cv2.rectangle(frame, (objeto_x - 20, objeto_y - 20), (objeto_x + 20, objeto_y + 20), (255, 0, 0), -1)

        cv2.imshow("Drag & Drop con seguimiento de manos", frame)

        if cv2.waitKey(1) & 0xFF == 27:
            break

cap.release()
cv2.destroyAllWindows()


