# 🖐️ GestureScroll

**GestureScroll** is an intuitive, real-time computer vision application that allows you to control your computer's scrolling simply by using hand gestures. No more reaching for the mouse or trackpad—just pinch and move your hand to navigate the digital world!

---

## ✨ Features
- **Pinch-to-Scroll Mechanism**: Highly responsive mechanism where you pinch your index finger and thumb together to "grab" the screen.
- **Multi-Directional Control**: Scroll up, down, left, or right effortlessly based on the direction of your hand movement.
- **Visual Feedback**: The app visually tracks your hand and highlights your pinch gesture with an on-screen indicator.
- **Lightweight & Fast**: Powered by Google's MediaPipe for fast, efficient, and accurate hand tracking, ensuring a smooth experience without input lag.

## 🛠️ Technology Stack
- **Python**: Core programming language.
- **OpenCV**: Captures real-time video feed from your webcam.
- **MediaPipe**: State-of-the-art ML models for high-fidelity hand landmark detection.
- **PyAutoGUI**: Cross-platform module used to programmatically control the mouse and perform scrolling actions.

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
   *(Note: Ensure `pyautogui`, `opencv-python`, and `mediapipe` are correctly installed).*

---

## 🎮 How to Use

1. Run the main application:
   ```bash
   python main.py
   ```
2. A window will open displaying your webcam feed.
3. Bring your hand into the frame. You will see a skeleton overlay tracking your hand movements.
4. **Pinch** your thumb and index finger together. A **green circle** will appear indicating the gesture is registered.
5. While holding the pinch, **move your hand** up/down or left/right to scroll the page.
6. Press the **`q`** key while the video window is focused to quit the application.

---

## ⚙️ Configuration
You can easily adjust the sensitivity of the scrolling and the gesture threshold inside `main.py`:
- `SCROLL_SENSITIVITY`: Increase this value for faster scrolling (Default is `1500`).
- `PINCH_THRESHOLD`: Adjusts how close your fingers need to be to trigger a pinch (Default is `0.05`).

---

*Made with ❤️ and Python.*