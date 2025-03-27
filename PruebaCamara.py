import cv2

cap = cv2.VideoCapture(0)  # Abre la cámara en el índice correcto

while True:
    ret, frame = cap.read()  # Captura un frame
    if not ret:
        break  # Si no hay frame, salir del bucle

    cv2.imshow("Camara", frame)  # Muestra la imagen en una ventana

    # Espera 1ms por una tecla; si es 'q', cierra la ventana
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()  # Libera la cámara
cv2.destroyAllWindows()  # Cierra todas las ventanas abiertas