import cv2
import requests as rq
from base64 import b64encode


def run_chat_vision(question):
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    if not cap.isOpened():
        return "无法打开摄像头"
    ret, frame = cap.read()
    cap.release()
    _, buffer = cv2.imencode('.jpg', frame)
    base64_image = b64encode(buffer).decode('utf-8')
    data = {"image": f"data:image/jpeg;base64,{base64_image}", "msg": question}
    response = rq.post("http://127.0.0.1:8086/qwen_vl", json=data)
    return response.json()["answer"]


if __name__ == "__main__":
    while True:
        text = input("用户：")
        try:
            answer = run_chat_vision(text)
            print("AI：", answer)
        except:
            print("提示: 请先运行Qwen-VLM模型API服务器，再进行聊天。")
