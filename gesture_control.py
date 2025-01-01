import cv2
import mediapipe as mp


def run_gesture_control():
    def get_finger_direction():
        finger_tips = [mp_hands.HandLandmark.THUMB_TIP, mp_hands.HandLandmark.INDEX_FINGER_TIP,
                       mp_hands.HandLandmark.MIDDLE_FINGER_TIP, mp_hands.HandLandmark.RING_FINGER_TIP,
                       mp_hands.HandLandmark.PINKY_TIP]
        if hand_landmarks:
            thumb_tip = hand_landmarks.landmark[finger_tips[0]]
            index_tip = hand_landmarks.landmark[finger_tips[1]]
            middle_tip = hand_landmarks.landmark[finger_tips[2]]
            thumb_tip_x, thumb_tip_y = thumb_tip.x, thumb_tip.y
            index_tip_x, index_tip_y = index_tip.x, index_tip.y
            middle_tip_x, middle_tip_y = middle_tip.x, middle_tip.y
            if index_tip_y < thumb_tip_y and middle_tip_y < thumb_tip_y:
                return "Robot Stop", "机器人停止运动"
            else:
                if abs(index_tip_x - thumb_tip_x) > abs(index_tip_y - thumb_tip_y):
                    if index_tip_x > thumb_tip_x:
                        return "Robot Turn Right", "机器人向右转"
                    else:
                        return "Robot Turn Left", "机器人向左转"
                else:
                    if index_tip_y > thumb_tip_y:
                        return "Robot Move Backward", "机器人向后退"
                    else:
                        return "Robot Move Forward", "机器人向前走"
        return "No Gesture Detected", "未检测到手势"
    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands(static_image_mode=False, max_num_hands=1, min_detection_confidence=0.7,
                           min_tracking_confidence=0.5)
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(rgb_frame)
        status_en = "No Gesture Detected"
        status_cn = "未检测到手势"
        if results and results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                status_en, status_cn = get_finger_direction()
                mp.solutions.drawing_utils.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
        cv2.putText(frame, status_en, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
        print(status_cn)
        cv2.imshow('Gesture Control - AI Mate Physical Robot', frame)
        if cv2.waitKey(50) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    run_gesture_control()
