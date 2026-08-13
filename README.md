# 🖐️ GestureScroll

**GestureScroll** is an intuitive, real-time computer vision application that allows you to control your computer's scrolling simply by using hand gestures. No more reaching for the mouse or trackpad—just pinch and move your hand to navigate the digital world!

---

## ✨ Features
- **Background Execution**: Runs silently in the background with a convenient System Tray icon to toggle features without keeping a terminal window open.
- **Pinch-to-Scroll Mechanism**: Highly responsive mechanism where you pinch your index finger and thumb together to "grab" the screen.
- **Multi-Directional Control**: Scroll up, down, left, or right effortlessly based on the direction of your hand movement.
- **Visual Feedback**: The app visually tracks your hand and highlights your pinch gesture with an on-screen indicator (can be toggled on/off).
- **Lightweight & Fast**: Powered by Google's MediaPipe for fast, efficient, and accurate hand tracking, ensuring a smooth experience without input lag.

## 🛠️ Technology Stack
- **Python**: Core programming language.
- **OpenCV**: Captures real-time video feed from your webcam.
- **MediaPipe**: State-of-the-art ML models for high-fidelity hand landmark detection.
- **PyAutoGUI**: Cross-platform module used to programmatically control the mouse and perform scrolling actions.
- **Pystray & Pillow**: Used to create the background taskbar notification icon.

---

## 🚀 Getting Started

### Prerequisites
Make sure you have Python installed on your system. You will also need a working webcam.

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/atharvadarke/GestureScroll.git
   cd GestureScroll
   ```

2. **Set up a virtual environment (Recommended):**
   ```bash
   python -m venv venv
   
   # Activate the virtual environment
   # Windows:
   .\venv\Scripts\activate
   # macOS/Linux:
   source venv/bin/activate
   ```

3. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

---

## 🎮 How to Use

1. Run the main application:
   ```bash
   python main.py
   ```
2. The application will immediately go to the background. Look for the **GestureScroll icon** in your system tray (bottom right corner, next to the clock).
3. **Right-click the icon** to access the control menu:
   - **Toggle Gestures (On/Off)**: Pause or resume gesture reading.
   - **Show/Hide Camera**: Open a visual debugging window to see the tracking skeleton overlay.
   - **Quit**: Safely exit the application.
4. **Scrolling**: While gestures are enabled, **pinch** your thumb and index finger together. Move your hand up/down or left/right to scroll the page.

---

## ⚙️ Configuration
You can easily adjust the sensitivity of the scrolling and the gesture threshold inside `main.py`:
- `SCROLL_SENSITIVITY`: Increase this value for faster scrolling (Default is `1500`).
- `PINCH_THRESHOLD`: Adjusts how close your fingers need to be to trigger a pinch (Default is `0.05`).

---

*Made with ❤️ and Python.*