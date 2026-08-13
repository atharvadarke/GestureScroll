import cv2
import mediapipe as mp

BaseOptions = mp.tasks.BaseOptions
HandLandmarker = mp.tasks.vision.HandLandmarker
HandLandmarkerOptions = mp.tasks.vision.HandLandmarkerOptions
HandLandmarkerResults = mp.tasks.vision.HandLandmarkerResult
VisionRunningMode = mp.tasks.vision.RunningMode

# Create a hand landmarker instance with the live stream mode:
def print_result(result: HandLandmarkerResults, output_image: mp.Image, timestamp_ms: int):
    print('hand landmarker result: {}'.format(result))

options = HandLandmarkerOptions(
    base_options=BaseOptions(model_asset_path= "C:\\Users\\mahna\\Downloads\\hand_landmarker.task"),
    running_mode=VisionRunningMode.LIVE_STREAM,
    result_callback=print_result)


cap = cv2.VideoCapture(0)
with HandLandmarker.create_from_options(options) as landmarker:
        mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=frame)
        detection_results = landmarker.detect_async(mp_image, 10000)

        while True:
            # Capture frame-by-frame
            ret, frame = cap.read()
            
            # # Our operations on the frame come here
            rgb_frames = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # Display the resulting frame
            
            cv2.imshow('window', frame)
            if cv2.waitKey(10) & 0xFF == ord('q'):
                break