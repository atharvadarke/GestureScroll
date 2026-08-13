import cv2
import mediapipe as mp
import pyautogui
import math
import threading
import pystray
from pystray import MenuItem as item
from PIL import Image, ImageDraw

# Global control flags
is_running = True
is_enabled = True
show_camera = False

def create_image(width, height, color1, color2):
    """Generate an image for the system tray icon."""
    image = Image.new('RGB', (width, height), color1)
    dc = ImageDraw.Draw(image)
    dc.rectangle(
        (width // 4, height // 4, width * 3 // 4, height * 3 // 4),
        fill=color2)
    return image

def gesture_loop():
    """Background thread function that handles webcam and gesture processing."""
    global is_running, is_enabled, show_camera
    
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
        is_running = False
        return

    prev_y = None
    prev_x = None
    PINCH_THRESHOLD = 0.05
    SCROLL_SENSITIVITY = 1500

    while is_running:
        ret, frame = cap.read()
        if not ret:
            continue
            
        if not is_enabled:
            # If disabled, just read frames to keep buffer clear
            if show_camera:
                cv2.imshow('Gesture Scroll (Disabled)', frame)
                cv2.waitKey(1)
            else:
                try:
                    cv2.destroyWindow('Gesture Scroll (Disabled)')
                    cv2.destroyWindow('Gesture Scroll (Pinch & Move)')
                except:
                    pass
            continue

        # Processing logic when enabled
        frame = cv2.flip(frame, 1) 
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(rgb_frame)
        
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                if show_camera:
                    mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
                
                index_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
                thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
                
                dist = math.hypot(index_tip.x - thumb_tip.x, index_tip.y - thumb_tip.y)
                
                if dist < PINCH_THRESHOLD:
                    if show_camera:
                        h, w, _ = frame.shape
                        cx, cy = int(index_tip.x * w), int(index_tip.y * h)
                        cv2.circle(frame, (cx, cy), 15, (0, 255, 0), cv2.FILLED)
                        
                    curr_y = index_tip.y
                    curr_x = index_tip.x
                    
                    if prev_y is not None and prev_x is not None:
                        dy = curr_y - prev_y
                        dx = curr_x - prev_x
                        
                        if abs(dy) > 0.005:
                            scroll_amount_y = int(-dy * SCROLL_SENSITIVITY)
                            pyautogui.scroll(scroll_amount_y)
                            prev_y = curr_y
                            
                        if abs(dx) > 0.005:
                            scroll_amount_x = int(dx * SCROLL_SENSITIVITY)
                            pyautogui.hscroll(scroll_amount_x)
                            prev_x = curr_x
                    else:
                        prev_y = curr_y
                        prev_x = curr_x
                else:
                    prev_y = None
                    prev_x = None
        else:
            prev_y = None
            prev_x = None
            
        if show_camera:
            try:
                cv2.destroyWindow('Gesture Scroll (Disabled)')
            except:
                pass
            cv2.imshow('Gesture Scroll (Pinch & Move)', frame)
            cv2.waitKey(1)
        else:
            try:
                cv2.destroyWindow('Gesture Scroll (Pinch & Move)')
                cv2.destroyWindow('Gesture Scroll (Disabled)')
            except:
                pass

    cap.release()
    cv2.destroyAllWindows()

def toggle_enable(icon, item):
    global is_enabled
    is_enabled = not is_enabled
    # Update icon color based on state (Green = On, Red = Off)
    if is_enabled:
        icon.icon = create_image(64, 64, 'black', 'green')
    else:
        icon.icon = create_image(64, 64, 'black', 'red')

def toggle_camera(icon, item):
    global show_camera
    show_camera = not show_camera

def quit_app(icon, item):
    global is_running
    is_running = False
    icon.stop()

def main():
    # Start the gesture tracking loop in a background thread
    gesture_thread = threading.Thread(target=gesture_loop, daemon=True)
    gesture_thread.start()
    
    # Create the system tray icon
    icon_image = create_image(64, 64, 'black', 'green')
    
    menu = pystray.Menu(
        item('Toggle Gestures (On/Off)', toggle_enable, checked=lambda item: is_enabled),
        item('Show/Hide Camera', toggle_camera, checked=lambda item: show_camera),
        pystray.Menu.SEPARATOR,
        item('Quit', quit_app)
    )
    
    icon = pystray.Icon("GestureScroll", icon_image, "Gesture Scroll", menu)
    
    print("GestureScroll is now running in the background.")
    print("Look for the icon in your system tray (bottom right corner).")
    
    # Run the icon event loop (blocks the main thread)
    icon.run()

if __name__ == "__main__":
    main()
