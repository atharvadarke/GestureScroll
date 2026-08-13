# import cv2
# import mediapipe as mp

# BaseOptions = mp.tasks.BaseOptions
# HandLandmarker = mp.tasks.vision.HandLandmarker
# HandLandmarkerOptions = mp.tasks.vision.HandLandmarkerOptions
# HandLandmarkerResult = mp.tasks.vision.HandLandmarkerResult
# VisionRunningMode = mp.tasks.vision.RunningMode


# def print_result(result: HandLandmarkerResult, output_image: mp.Image, timestamp_ms: int):

#     if result.hand_landmarks:

#         hand = result.hand_landmarks[0]

#         index_tip = hand[8]

#         print(
#             f"Index Finger: x={index_tip.x:.3f}, "
#             f"y={index_tip.y:.3f}, "
#             f"z={index_tip.z:.3f}"
#         )


# options = HandLandmarkerOptions(
#     base_options=BaseOptions(
#         model_asset_path=r"C:\Users\mahna\Downloads\hand_landmarker.task"
#     ),
#     running_mode=VisionRunningMode.LIVE_STREAM,
#     result_callback=print_result
# )

# cap = cv2.VideoCapture(0)

# timestamp = 0

# with HandLandmarker.create_from_options(options) as landmarker:

#     while True:

#         ret, frame = cap.read()

#         if not ret:
#             break

#         rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

#         mp_image = mp.Image(
#             image_format=mp.ImageFormat.SRGB,
#             data=rgb_frame
#         )

#         timestamp += 1

#         landmarker.detect_async(
#             mp_image,
#             timestamp
#         )

#         # cv2.imshow("window", frame)
#         if latest_result and latest_result.hand_landmarks:

#             h, w, _ = frame.shape

#             for hand in latest_result.hand_landmarks:

#                 for landmark in hand:

#                     x = int(landmark.x * w)
#                     y = int(landmark.y * h)

#                     cv2.circle(
#                         frame,
#                         (x, y),
#                         5,
#                         (0, 255, 0),
#                         -1
#                     )

#         cv2.imshow("window", frame)

#         if cv2.waitKey(10) & 0xFF == ord('q'):
#             break

# cap.release()
# cv2.destroyAllWindows()