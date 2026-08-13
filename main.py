import cv2
import mediapipe as mp
import pyautogui
import math
import time

def main():
    # Disable pyautogui failsafe (optional, but prevents crashes if mouse goes to corner)
    pyautogui.FAILSAFE = False
    
    mp_hands = mp.solutions.hands
    mp_drawing = mp.solutions.drawing_utils

    hands = mp_hands.Hands(
        static_image_mode=False,
        max_num_hands=1,
        min_detection_confidence=0.7,
        min_tracking_confidence=0.7
    )

    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return

    # To track the previous position for delta calculation
    prev_y = None
    prev_x = None

    # Threshold for pinch detection (distance between thumb and index tip)
    PINCH_THRESHOLD = 0.05
    
    # Sensitivity for scrolling (adjust based on preference)
    # Higher value = faster scroll
    SCROLL_SENSITIVITY = 1500
    
    print("Starting Gesture Scroll Application...")
    print("Instructions: Pinch your thumb and index finger together and move your hand to scroll.")
    print("Press 'q' in the video window to quit.")

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame")
            break
        
        # Flip frame horizontally for intuitive "selfie" mirror view
        frame = cv2.flip(frame, 1) 
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        # Process the frame and find hands
        results = hands.process(rgb_frame)
        
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                # Draw hand landmarks
                mp_drawing.draw_landmarks(
                    frame, 
                    hand_landmarks, 
                    mp_hands.HAND_CONNECTIONS
                )
                
                # Get coordinates for index tip and thumb tip
                index_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
                thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
                
                # Calculate euclidean distance between thumb and index tip
                dist = math.hypot(index_tip.x - thumb_tip.x, index_tip.y - thumb_tip.y)
                
                # Check if gesture is a "pinch"
                if dist < PINCH_THRESHOLD:
                    # Visual feedback for pinch (draw a circle around the pinch point)
                    h, w, _ = frame.shape
                    cx, cy = int(index_tip.x * w), int(index_tip.y * h)
                    cv2.circle(frame, (cx, cy), 15, (0, 255, 0), cv2.FILLED)
                    
                    curr_y = index_tip.y
                    curr_x = index_tip.x
                    
                    if prev_y is not None and prev_x is not None:
                        # Calculate movement delta
                        dy = curr_y - prev_y
                        dx = curr_x - prev_x
                        
                        # Apply scrolling if movement is beyond a tiny noise threshold
                        if abs(dy) > 0.005:
                            # In pyautogui, positive scroll is up, negative is down
                            scroll_amount_y = int(-dy * SCROLL_SENSITIVITY)
                            pyautogui.scroll(scroll_amount_y)
                            prev_y = curr_y # update reference point
                            
                        if abs(dx) > 0.005:
                            # Horizontal scrolling
                            scroll_amount_x = int(dx * SCROLL_SENSITIVITY)
                            # Only uncomment if your environment supports horizontal scrolling well
                            pyautogui.hscroll(scroll_amount_x)
                            prev_x = curr_x
                    else:
                        # First frame of the pinch, set origin
                        prev_y = curr_y
                        prev_x = curr_x
                else:
                    # Reset origin when pinch is released
                    prev_y = None
                    prev_x = None
                    
        else:
            # Reset origin if no hands detected
            prev_y = None
            prev_x = None
            
        cv2.imshow('Gesture Scroll (Pinch & Move)', frame)
        
        # Exit on 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
            
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
