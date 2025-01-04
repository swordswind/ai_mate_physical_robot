import cv2
from deepface import DeepFace


def run_face_analysis():
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        try:
            results = DeepFace.analyze(frame, actions=['age', 'gender', 'race', 'emotion'])
            for face in results:
                age = face['age']
                gender_score = max(face['gender'].values())
                gender_label = max(face['gender'], key=face['gender'].get)
                race_score = max(face['race'].values())
                race_label = max(face['race'], key=face['race'].get)
                emotion_score = max(face['emotion'].values())
                emotion_label = max(face['emotion'], key=face['emotion'].get)
                x, y, w, h = face['region']['x'], face['region']['y'], face['region']['w'], face['region']['h']
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
                cv2.putText(frame, f"Age:{age}, Gender:{gender_label}, Race:{race_label}, Emotion:{emotion_label}",
                            (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)
                print(f"年龄:{age}, 性别:{gender_label}({gender_score:.1f}%), 种族:{race_label}({race_score:.1f}%), 表情:{emotion_label}({emotion_score:.1f}%)")
        except:
            print("未检测到人脸")
        cv2.imshow('Face Analysis - AI Mate Physical Robot', frame)
        if cv2.waitKey(50) & 0xFF == ord('q'):
            break


if __name__ == '__main__':
    run_face_analysis()
