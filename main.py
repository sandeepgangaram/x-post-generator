import os
import requests
from dotenv import load_dotenv

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

def generate_x_post(user_input:str)->str:
    payload = {
        "model":"",
        "input":""
    }
    
    resonse = requests.post(
        "https://api.openai.com/v1/responses", 
        json=payload,
        headers={
            "Content-Type":"application/json",
            "Authorization":f"Bearer {OPENAI_API_KEY}"
        })

def main():
    user_input = input("What you want the post to be about?")
    x_post = generate_x_post(user_input)
    print(x_post)


if __name__ == "__main__":
    main()
