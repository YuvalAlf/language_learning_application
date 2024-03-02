from gtts import gTTS
import os

from gtts.tts import Speed


def speak_english(text):
    tts = gTTS(text=text, lang='fr')
    tts.speed = Speed.NORMAL
    tts.save("output.mp3")
    os.system("output.mp3")  # Use mpg321 for Linux or macOS, use mpg123 for Windows

text = "Bonjour, comment ca va? je m'apelle Yuval."
speak_english(text)
