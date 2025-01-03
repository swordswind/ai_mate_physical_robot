import cv2
from ultralytics import YOLO


def run_object_detection():
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    model = YOLO("data/model/YOLO/yolo11s.pt")
    class_dict = {
        "0": "个人", "1": "辆自行车", "2": "辆汽车", "3": "辆摩托车", "4": "架飞机", "5": "辆公共汽车", "6": "列火车",
        "7": "辆卡车", "8": "艘船", "9": "个交通灯", "10": "个消防栓", "11": "个停车标志", "12": "个停车计时器",
        "13": "张长椅", "14": "只鸟", "15": "只猫", "16": "只狗", "17": "匹马", "18": "只绵羊", "19": "头奶牛",
        "20": "头大象", "21": "只熊", "22": "只斑马", "23": "只长颈鹿", "24": "个背包", "25": "把伞", "26": "个手提包",
        "27": "条领带", "28": "个行李箱", "29": "个飞盘", "30": "副滑雪板", "31": "块滑雪板", "32": "个运动球",
        "33": "个风筝", "34": "根棒球棒", "35": "个棒球手套", "36": "块滑板", "37": "块冲浪板", "38": "个网球拍",
        "39": "个瓶子", "40": "个酒杯", "41": "个杯子", "42": "把叉子", "43": "把刀子", "44": "把勺子", "45": "个碗",
        "46": "根香蕉", "47": "个苹果", "48": "个三明治", "49": "个橙子", "50": "棵西兰花", "51": "根胡萝卜",
        "52": "个热狗", "53": "张比萨", "54": "个甜甜圈", "55": "块蛋糕", "56": "把椅子", "57": "张沙发",
        "58": "盆盆栽", "59": "张床", "60": "张餐桌", "61": "个厕所", "62": "台显示器", "63": "台笔记本电脑",
        "64": "个鼠标", "65": "个遥控器", "66": "个键盘", "67": "部手机", "68": "台微波炉", "69": "台烤箱",
        "70": "个烤面包机", "71": "个水槽", "72": "台冰箱", "73": "本书", "74": "个时钟", "75": "个花瓶",
        "76": "把剪刀", "77": "个泰迪熊", "78": "个吹风机", "79": "把牙刷"}
    while True:
        ret, frame = cap.read()
        if not ret:
            print("无法打开摄像机")
            break
        results = model(frame)[0]
        class_counts = {}
        for box in results.boxes:
            class_id = int(box.cls)
            class_name = str(class_id)
            if class_name in class_dict:
                if class_name in class_counts:
                    class_counts[class_name] += 1
                else:
                    class_counts[class_name] = 1
        output = []
        for class_name, count in class_counts.items():
            output.append(f"{count}{class_dict[class_name]}")
        output_str = ", ".join(output)
        if output_str:
            print(output_str)
        annotated_frame = results.plot()
        cv2.imshow("Object Detection - AI Mate Physical Robot", annotated_frame)
        if cv2.waitKey(50) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    run_object_detection()
