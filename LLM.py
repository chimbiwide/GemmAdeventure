import lmstudio as lms
import json

def stream_response(model, chat):
    prediction_stream = model.respond_stream(
        chat,
        on_message=chat.append,
        config={
            "temperature": 1.0,
            "maxTokens": 512,
        }
    )
    print("Mysterious Magician: ", end="", flush=True)
    response_text = ""
    for fragment in prediction_stream:
        print(fragment.content, end="", flush=True)
        response_text += fragment.content
    print()
    return response_text

def save_chat(history):
    with open("history.json", "w", encoding='utf-8') as f:
        json.dump(history, f, indent=4)

def add_user_message(history, txt):
    history["messages"].append({
        "role": "user",
        "content": txt
    })

def add_model_message(history, txt):
    history["messages"].append({
        "role": "assistant",
        "content": txt
    })

def read_history(file:str):
    chat = {}
    with open(file, "r", encoding='utf-8') as f:
        chat = json.load(f)
    return chat
