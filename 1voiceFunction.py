import pyttsx3
import datetime 

engine = pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

speak('hey vishnu')