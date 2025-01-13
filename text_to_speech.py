import pygame as pg
import requests as rq

voice_path = "data/cache.wav"


def run_text_to_speech(text):
    url = f'http://127.0.0.1:9880/?text={text}&text_language=zh'
    try:
        response = rq.get(url)
        print("语音合成成功！")
        wav_data = response.content
        with open(voice_path, 'wb') as f:
            f.write(wav_data)
        pg.init()
        try:
            pg.mixer.music.load(voice_path)
            pg.mixer.music.play()
            while pg.mixer.music.get_busy():
                pg.time.Clock().tick(1)
            pg.mixer.music.stop()
        except:
            pass
        pg.quit()
    except Exception as e:
        print(f"本地GPT-SoVITS整合包API服务器未开启，错误详情：{e}")


if __name__ == '__main__':
    while True:
        msg = input("请输入要想合成语音的文本：")
        print("正在合成语音，请稍等...")
        run_text_to_speech(msg)
