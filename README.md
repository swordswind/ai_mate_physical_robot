# AI伙伴实体机器人

## 项目简介

欢迎来到**AI伙伴实体机器人**开源项目！本项目由MewCo-AI团队倾力打造，旨在通过先进的AI技术和机器人硬件，为用户提供沉浸式的全息陪伴体验。**Holo UGV**，是AI伙伴实体版的第一代产品，集成了多模态感知、自动驾驶、实时语音交互等强大功能，突破虚拟与现实的边界，开启全息陪伴的全新时代。本项目将逐渐开源。

## 项目亮点

### 1. **枫云AI仿生引擎（MAVE）**

**枫云AI仿生引擎（MewCo AI Virtual-Life Engine）**是AI伙伴实体版的核心软件系统，具备高度智能化的多模态交互能力。它通过三层架构设计，深度融合了当前最适合且先进的开源模型，实现了从感知到认知再到行为的全流程智能化。

   - **感知层**：
     - **多模态感知系统**：通过视觉、听觉、触觉等多模态传感器，实时捕捉环境信息。
       - **视觉感知**：基于**YOLO-World**的万物识别、**DeepFace**的人脸识别、**MediaPipe**的手势识别，能够精准识别物体、人脸和手势。
       - **听觉感知**：通过全向麦克风阵列，支持远距离语音识别**（SenseVoice）**和深度降噪，确保语音交互的准确性。
       - **空间感知**：结合TOF激光雷达和9轴惯性测量单元**（IMU）**，实现高精度的环境感知和导航。
     - **实时反馈**：感知层的数据实时传输到认知层，确保交互的即时性和流畅性。

   - **认知层**：
     - **大语言模型（Qwen2.5-7B）**：支持复杂的自然语言理解和生成，能够进行多轮对话、情感分析和上下文推理。
     - **视觉大模型（Qwen2-VL-7B）**：结合视觉感知数据，实现图像理解、场景分析和物体识别。
     - **长期记忆系统（MemGPT）**：能够存储和调用用户的长期交互历史，实现个性化的陪伴体验。
     - **知识图谱与向量知识库（LanceDB）**：通过结构化的知识存储和检索，支持智能问答、知识推理和角色扮演。
     - **思维链模型（Marco-o1）**：通过多步推理和决策，生成符合逻辑的行为和对话。

   - **行为层**：
     - **动作规划与运动控制**：基于强化学习和实时反馈，生成拟人化的动作和行为。
     - **多模态生成**：支持语音合成**（GPT-SoVITS）**、视觉生成和实时对话，提供流畅的交互体验。
     - **情绪与行为模拟**：通过情绪模型和拟人行为生成，AI伙伴能够表现出多变的情绪和自主行为，如主动发话、唱歌跳舞等。

   - **本地端侧运行**：所有AI计算均在本地端侧完成，无需依赖网络，确保用户隐私和数据安全。

### 2. **智能Agent功能**

   - **自动驾驶**：通过激光雷达和相机实现自主导航与避障，支持室内外高精度地图构建**（SLAM）**。
   - **自动寻物**：结合视觉感知、无线频谱感知和语音指令，帮助用户快速定位丢失物品。
   - **自动跟随**：通过声源定位和人脸识别，智能跟随用户移动。
   - **IoT联动**：与**Home Assistant**米家集成插件等智能家居系统无缝集成，支持智能家居的便捷控制。
   - **机器人蜂群网络**：支持多机协同与算力共享，适用于复杂场景下的多机协作。

## 项目目标

本项目的目标是通过开源的方式，推动AI与机器人技术的创新与发展，为开发者、研究者以及技术爱好者提供一个开放的平台，共同探索AI伙伴实体版的未来可能性。

## 项目地址

- **项目主页**: [https://swordswind.github.io/2025/01/01/holougv/](https://swordswind.github.io/2025/01/01/holougv/)
- **开源地址**: [https://github.com/swordswind/ai_mate_physical_robot](https://github.com/swordswind/ai_mate_physical_robot)

## 版权声明

本项目的硬件和软件引擎**严禁商用**，仅供技术创意交流展示。采用 **GPL-3.0 License** 开源协议，您可以在遵守该协议的前提下自由使用、修改和分发本项目。详情请参阅 [GPL-3.0 License](https://www.gnu.org/licenses/gpl-3.0.html)。

## 手势控制模块

本项目中的手势控制模块基于**MediaPipe**和**OpenCV**实现，能够通过摄像头实时捕捉用户的手势，并根据手势控制机器人的运动。以下是手势控制模块的主要功能：

- **手势识别**：通过MediaPipe的手势识别模型，实时检测用户的手势。
- **机器人控制**：根据识别到的手势，控制机器人的运动方向，包括前进、后退、左转、右转以及停止。
- **实时反馈**：在屏幕上实时显示当前识别到的手势及其对应的机器人动作。

1. **安装依赖**：

   ```bash
   pip install -r requirements.txt
   ```

2. **运行手势控制模块**：

   ```bash
   python gesture_control.py
   ```

3. **手势控制说明**：

   - **向前移动**：食指和中指向上，且食指高于拇指。
   - **向后移动**：食指和中指向下，且食指低于拇指。
   - **向左转**：食指向左，且食指与拇指的水平距离大于垂直距离。
   - **向右转**：食指向右，且食指与拇指的水平距离大于垂直距离。
   - **停止**：食指和中指向上，且食指和中指都低于拇指。

## 参与贡献

我们欢迎所有对AI和机器人技术感兴趣的开发者、研究者以及技术爱好者参与本项目。如果您有任何建议、问题或想要贡献代码，请通过以下方式联系我们：

- **提交Issue**: [https://github.com/swordswind/ai_mate_physical_robot/issues](https://github.com/swordswind/ai_mate_physical_robot/issues)
- **提交Pull Request**: [https://github.com/swordswind/ai_mate_physical_robot/pulls](https://github.com/swordswind/ai_mate_physical_robot/pulls)

## 特别鸣谢

本项目的诞生得益于众多开源项目的支持，特别感谢以下开源社区与开发者为AI伙伴实体版机器人项目做出的贡献：

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
