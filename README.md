# AI伙伴实体机器人

## 项目简介

**AI伙伴实体机器人**是MewCo-AI团队打造的开源项目，旨在通过AI技术和机器人硬件提供沉浸式全息陪伴体验。**Holo UGV**是第一代产品，集成了多模态感知、自动驾驶、实时语音交互等功能，突破虚拟与现实的边界。本项目将逐步开源。

## 项目亮点

### 1. **枫云AI仿生引擎（MAVE）**

**枫云AI仿生引擎**是AI伙伴的核心软件系统，具备高度智能化的多模态交互能力，通过三层架构设计实现全流程智能化。

   - **感知层**：
     - **多模态感知系统**：通过视觉、听觉、触觉等传感器实时捕捉环境信息。
       - **视觉感知**：基于**YOLO-World**、**DeepFace**、**MediaPipe**，精准识别物体、人脸和手势。
       - **听觉感知**：支持远距离语音识别（**SenseVoice**）和深度降噪。
       - **空间感知**：结合TOF激光雷达和9轴IMU，实现高精度环境感知和导航。
     - **实时反馈**：感知层数据实时传输到认知层，确保交互即时性。

   - **认知层**：
     - **大语言模型（Qwen2.5-7B）**：支持复杂自然语言理解和生成。
     - **视觉大模型（Qwen2-VL-7B）**：结合视觉感知数据，实现图像理解和场景分析。
     - **长期记忆系统（MemGPT）**：存储和调用用户交互历史，实现个性化陪伴。
     - **知识图谱与向量知识库（LanceDB）**：支持智能问答、知识推理和角色扮演。
     - **思维链模型（Marco-o1）**：通过多步推理和决策，生成符合逻辑的行为和对话。

   - **行为层**：
     - **动作规划与运动控制**：基于强化学习和实时反馈，生成拟人化动作。
     - **多模态生成**：支持语音合成（**GPT-SoVITS**）、视觉生成和实时对话。
     - **情绪与行为模拟**：通过情绪模型和拟人行为生成，表现多变情绪和自主行为。

   - **本地端侧运行**：所有AI计算在本地完成，确保用户隐私和数据安全。

### 2. **智能Agent功能**

   - **自动驾驶**：通过激光雷达和相机实现自主导航与避障。
   - **自动寻物**：结合视觉感知和语音指令，帮助用户定位丢失物品。
   - **自动跟随**：通过声源定位和人脸识别，智能跟随用户移动。
   - **IoT联动**：与**Home Assistant**等智能家居系统无缝集成。
   - **机器人蜂群网络**：支持多机协同与算力共享。

## 项目目标

通过开源推动AI与机器人技术的创新与发展，为开发者、研究者提供开放平台，探索AI伙伴实体版的未来可能性。

## 项目地址

- **项目主页**: [https://swordswind.github.io/2025/01/01/holougv/](https://swordswind.github.io/2025/01/01/holougv/)
- **开源地址**: [https://github.com/swordswind/ai_mate_physical_robot](https://github.com/swordswind/ai_mate_physical_robot)

## 版权声明

本项目采用 **GPL-3.0 License** 开源协议，严禁商用。详情请参阅 [GPL-3.0 License](https://www.gnu.org/licenses/gpl-3.0.html)。

## 安装依赖

运行前请确保已安装所需依赖：

```bash
pip install -r requirements.txt
```

## 人脸分析模块

本项目的人脸分析模块基于**DeepFace**和**OpenCV**实现，能够通过摄像头实时分析人脸属性，包括年龄、性别、种族和表情。以下是模块的主要功能：

- **人脸检测**：通过DeepFace实时检测摄像头画面中的人脸。
- **属性分析**：分析人脸的年龄、性别、种族和表情。
- **实时反馈**：在屏幕上实时显示分析结果，并绘制人脸框。

1. **运行人脸分析模块**：

   ```bash
   python face_analysis.py
   ```

2. **人脸分析说明**：

   - **检测属性**：支持年龄、性别、种族和表情的实时分析。
   - **输出格式**：分析结果以文本形式输出，例如“年龄:25, 性别:男, 种族:亚洲, 表情:高兴”。
   - **退出程序**：按下键盘上的`q`键即可退出程序。

## 手势控制模块

本项目的手势控制模块基于**MediaPipe**和**OpenCV**实现，能够通过摄像头实时捕捉用户手势，并根据手势控制机器人运动。以下是模块的主要功能：

- **手势识别**：通过MediaPipe实时检测用户手势。
- **机器人控制**：根据手势控制机器人运动方向。
- **实时反馈**：在屏幕上实时显示手势及其对应的机器人动作。

1. **运行手势控制模块**：

   ```bash
   python gesture_control.py
   ```

2. **手势控制说明**：

   - **向前移动**：食指和中指向上，且食指高于拇指。
   - **向后移动**：食指和中指向下，且食指低于拇指。
   - **向左转**：食指向左，且食指与拇指的水平距离大于垂直距离。
   - **向右转**：食指向右，且食指与拇指的水平距离大于垂直距离。
   - **停止**：食指和中指向上，且食指和中指都低于拇指。

## 物体检测模块

本项目的物体检测模块基于**YOLO**模型实现，能够通过摄像头实时检测环境中的物体，并统计各类物体的数量。以下是模块的主要功能：

- **物体检测**：通过YOLO模型实时检测摄像头画面中的物体。
- **物体统计**：统计画面中各类物体的数量，并输出结果。
- **实时反馈**：在屏幕上实时显示检测到的物体及其数量。

1. **运行物体检测模块**：

   ```bash
   python object_detection.py
   ```

2. **物体检测说明**：

   - **检测类别**：支持80种常见物体的检测。
   - **输出格式**：检测结果以文本形式输出，例如“1个人，2辆汽车”。
   - **退出程序**：按下键盘上的`q`键即可退出程序。

## 参与贡献

欢迎所有对AI和机器人技术感兴趣的开发者、研究者参与本项目。如有建议、问题或想贡献代码，请通过以下方式联系我们：

- **提交Issue**: [https://github.com/swordswind/ai_mate_physical_robot/issues](https://github.com/swordswind/ai_mate_physical_robot/issues)
- **提交Pull Request**: [https://github.com/swordswind/ai_mate_physical_robot/pulls](https://github.com/swordswind/ai_mate_physical_robot/pulls)

## 特别鸣谢

感谢以下开源社区与开发者为AI伙伴实体版机器人项目做出的贡献：

- **GPT-SoVITS**: [https://github.com/RVC-Boss/GPT-SoVITS](https://github.com/RVC-Boss/GPT-SoVITS)
- **OpenCV**: [https://github.com/opencv/opencv-python](https://github.com/opencv/opencv-python)
- **FunAudioLLM**: [https://github.com/FunAudioLLM](https://github.com/FunAudioLLM)
- **Qwen2.5**: [https://github.com/QwenLM/Qwen2.5](https://github.com/QwenLM/Qwen2.5)
- **Qwen2-VL**: [https://github.com/QwenLM/Qwen2-VL](https://github.com/QwenLM/Qwen2-VL)
- **Marco-o1**: [https://github.com/AIDC-AI/Marco-o1](https://github.com/AIDC-AI/Marco-o1)
- **MemGPT**: [https://github.com/letta-ai/letta](https://github.com/letta-ai/letta)
- **Live2D**: [https://github.com/nladuo/live2d-chatbot-demo](https://github.com/nladuo/live2d-chatbot-demo)
- **YOLO-World**: [https://github.com/AILab-CVC/YOLO-World](https://github.com/AILab-CVC/YOLO-World)
- **DeepFace**: [https://github.com/serengil/deepface](https://github.com/serengil/deepface)
- **MediaPipe**: [https://github.com/google-ai-edge/mediapipe](https://github.com/google-ai-edge/mediapipe)