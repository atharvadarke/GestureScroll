import cv2
import mediapipe as mp

cap = cv2.VideoCapture(0)
mp_hands = mp.solutions.hands
hands = mp.Hands()

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # # Our operations on the frame come here
    rgb_frames = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Display the resulting frame
    cv2.imshow('window', frame)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break