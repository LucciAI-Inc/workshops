import json
import requests
import os
from dotenv import load_dotenv
from termcolor import colored

load_dotenv()  # This loads the variables from .env

GPT_MODEL = "gpt-3.5-turbo-0613"
# GPT_MODEL = "gpt-3.5-turbo-0301"

def chat_completion_request(messages, model=GPT_MODEL):
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + os.getenv('OPENAI_API_KEY'),
    }
    json_data = {
        "model": model, 
        "messages": messages, 
        "max_tokens": 500, 
        "temperature": 0,
        "n" : 1
        }
    try:
        response = requests.post(
            "https://api.openai.com/v1/chat/completions",
            headers=headers,
            json=json_data,
        )
        return response
    except Exception as e:
        print("Unable to generate ChatCompletion response")
        print(f"Exception: {e}")
        return e
    


def model_list_request():
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + os.getenv('OPENAI_API_KEY')
    }

    try:
        response = requests.get(
            "https://api.openai.com/v1/models",
            headers=headers
        )
        return response
    except Exception as e:
        print("Unable to retrieve model list")
        print(f"Exception: {e}")
        return e


def pretty_print_conversation(messages):
    role_to_color = {
        "system": "red",
        "user": "green",
        "assistant": "blue"
    }
    
    for message in messages:
        if message["role"] == "system":
            print(colored(f"system: {message['content']}\n", role_to_color[message["role"]]))
        elif message["role"] == "user":
            print(colored(f"user: {message['content']}\n", role_to_color[message["role"]]))
        elif message["role"] == "assistant":
            print(colored(f"assistant: {message['content']}\n", role_to_color[message["role"]]))

# Chat
messages = []
messages.append({"role": "system", "content": "Eres un asistente muy útil y conciso"})
messages.append({"role": "user", "content": "Puedes contar hasta 10?"})

chat_response = chat_completion_request(messages)

json_res = json.dumps(chat_response.json(), indent=4)
print(json_res)

assistant_message = chat_response.json()["choices"][0]["message"]
messages.append(assistant_message)

#pretty_print_conversation(messages)
print(messages)

# Model listing
# model_list = model_list_request()
# json_res = json.dumps(model_list.json(), indent=4)
# print(json_res)