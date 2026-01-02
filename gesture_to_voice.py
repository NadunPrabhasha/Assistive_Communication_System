import cv2
import mediapipe as mp
import pyttsx3

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)
spoken = False  # prevent repeating speech

while True:
    success, img = cap.read()
    if not success:
        break

    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    result = hands.process(img_rgb)

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            mp_draw.draw_landmarks(
                img,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS
            )

            # Count fingers (simple logic)
            landmarks = hand_landmarks.landmark
            fingers = 0

            tips = [4, 8, 12, 16, 20]
            for tip in tips:
                if landmarks[tip].y < landmarks[tip - 2].y:
                    fingers += 1

            if fingers >= 4 and not spoken:
                speak("Please help me")
                spoken = True

    cv2.imshow("Gesture to Voice - Assistive Communication System", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
