import os
import gradio as gr
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

def chat_with_Deepseek(user_input):
    client = OpenAI(
        api_key=os.getenv('DEEPSEEK_API_KEY'),
        base_url="https://api.deepseek.com")

    response = client.chat.completions.create(
        model="deepseek-v4-flash-vision-exp",
        messages=[
            {"role": "system", "content": "You are a helpful assistant"},
            {"role": "user", "content": user_input},
        ]
    )

    return response.choices[0].message.content


demo = gr.Interface(
    fn=chat_with_Deepseek,
    inputs=["text"],
    outputs=["text"]
)

if __name__ == "__main__":
    demo.launch()
