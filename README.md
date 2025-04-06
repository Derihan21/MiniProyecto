# MiniProyecto


Este programa usa MediaPipe y OpenCV para detectar una mano a través de la cámara web. Cuando el usuario junta el índice y el pulgar, se interpreta como un gesto de "agarrar", y permite mover un objeto (un cuadrado azul) en la pantalla siguiendo la posición del dedo índice. Es como un sistema de drag and drop (arrastrar y soltar), pero usando solo gestos de la mano.

Librerias utilizadas:

cv2 (OpenCV): para capturar la imagen desde la cámara y mostrarla.

mediapipe: para detectar y seguir los puntos clave (landmarks) de la mano.

numpy: para calcular distancias entre puntos.
