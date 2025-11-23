import lmstudio as lms
from prompts import Gemma3NPC
from LLM import stream_response, save_chat, add_user_message, add_model_message, read_history
SERVER_API_HOST = "100.102.38.119:1235"

lms.configure_default_client(SERVER_API_HOST)

model = lms.llm("gemma3npc-it@q4_k_m")
history = {"messages" : []}

chat = lms.Chat.from_history(Gemma3NPC)
add_user_message(history, Gemma3NPC)

response = stream_response(model, chat)
add_model_message(history, response)

while True:
    try:
        user_input = input("You: ")
    except EOFError:
        print()
        break
    if user_input == "/exit":
        break
    if user_input == "/save":
        save_chat(history)
    if user_input == "/resume":
        chat = chat.from_history(read_history("history.json"))

    chat.add_user_message(user_input)
    add_user_message(history, user_input)
    response =  stream_response(model, chat)
    add_model_message(history, response)
