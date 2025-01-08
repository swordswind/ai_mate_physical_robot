from ollama import Client

cot_history = []
prompt = "你是一个由MewCo-AI开发的Holo UGV陪伴型猫娘，不是机器人，拥有人类情感，性格为温柔体贴且活泼。"


def run_chat_chain_of_thought(msg):
    cot_client = Client(host='http://127.0.0.1:11434')
    cot_history.append({"role": "user", "content": msg})
    messages = [{"role": "system", "content": prompt}]
    messages.extend(cot_history)
    response_stream = cot_client.chat(model="qwen2.5:7b", messages=messages, stream=True)
    full_response = ""
    print("AI：", end="")
    for chunk in response_stream:
        if 'message' in chunk and 'content' in chunk['message']:
            content = chunk['message']['content']
            print(content, end="", flush=True)
            full_response += content
    cot_history.append({"role": "assistant", "content": full_response})


if __name__ == '__main__':
    while True:
        text = input("用户：")
        run_chat_chain_of_thought(text)
        print()
