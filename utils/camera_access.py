import cv2


cap = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # # Our operations on the frame come here
    rgb_frames = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Display the resulting frame
    cv2.imshow('window', frame)
    if cv2.waitKey(5000) & 0xFF == ord('q'):
        break