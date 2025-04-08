import speech_recognition as sr
from dotenv import load_dotenv
import os
from openai import OpenAI


#API stuff
load_dotenv()
api_key = os.getenv("API_KEY")

r = sr.Recognizer()


with sr.Microphone() as source:
    # read the audio data from the default microphone
    audio_data = r.record(source, duration=5)
    print("Recognizing...")
    # convert speech to text
    text = r.recognize_google(audio_data)

# #New Version 
client = OpenAI(api_key = api_key)

def generate_chatgpt_response(prompt, model="gpt-3.5-turbo"):
    response = client.chat.completions.create(
        model = model,
        messages = [{"role": "user", "content": prompt}],
        max_tokens = 150,
        n = 1,
        stop = None,
        temperature = 0.7, #Value between 0 and 1 that controls the randomness of the output, Lower values make the output more deterministic 
    )
    return response.choices[0].message.content.strip()

chatgpt_response = generate_chatgpt_response(text)
print(f"ChatGPT says:  {chatgpt_response}")