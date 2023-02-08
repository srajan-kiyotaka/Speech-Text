from gtts import gTTS
import os

def text_to_speech(text, filename):
    tts = gTTS(text=text, lang='en')
    tts.save(filename)
    os.system(f"start {filename}")

text = "Hello, Myself srajan chourasia, third year btech student at IIT Goa, I am the current General Secretary of Technical Affairs. I am in the Computer Science branch, I mostly work in the field of AI and Machine Learning specially in the field of Deep Learning. I recently won the Goa Police Hackathon. Thanks for listening this sample audio!"
filename = "Srajan.mp3"

text_to_speech(text, filename)
