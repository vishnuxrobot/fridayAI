import pyttsx3  # pip install pyttsx3
import datetime  # pip install datetime
# 1.pip install SpeechRecognition 2.pip install pipwin 3.pip install pyaudio
import speech_recognition as sr
import wikipedia  # pip install wikipedia
import smtplib  # dont want to install
import webbrowser as wb  # dont want to install
import os  # dont want to install
from playsound import playsound
import random
from transformers import BlenderbotTokenizer, BlenderbotForConditionalGeneration
from transformers import pipeline, AutoModelForSeq2SeqLM, AutoTokenizer
from bs4 import BeautifulSoup
import requests
import re

bb400m = "facebook/blenderbot-400M-distill"
chat_model = BlenderbotForConditionalGeneration.from_pretrained(bb400m)
chat_tokenizer = BlenderbotTokenizer.from_pretrained(bb400m)
model_name = "sshleifer/distilbart-cnn-12-6"
summarizer_model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
sum_tokenizer = AutoTokenizer.from_pretrained(model_name)
summarizer = pipeline("summarization", model=summarizer_model, tokenizer=sum_tokenizer)

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
newVoiceRate = 165
engine.setProperty('rate', newVoiceRate)

def replace_angle_brackets(input_text):
    pattern = re.compile(r'<.*?>')
    result_text = re.sub(pattern, '', input_text)
    return result_text

def speak(*words):
    print(" ".join(words))
    engine.say(" ".join(words))
    engine.runAndWait()

def randChat(sequence):
    try:
        inputs = chat_tokenizer([sequence], return_tensors="pt")
        reply_ids = chat_model.generate(**inputs)
        response = chat_tokenizer.batch_decode(reply_ids,skip_special_tokens=True)[0]
    except:
        return "Sorry pardon please!"
    return response

def qands(search):
    url = "https://www.google.com/search?q=" + search
    response = requests.get(url)
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        html_content = response.content
        soup = BeautifulSoup(html_content, 'html.parser')
        text_content = soup.get_text(separator=' ', strip=True)
        summary = summarizer(text_content, max_length=40, min_length=15, length_penalty=2.0, num_beams=4, early_stopping=True)
        return summary[0]['summary_text']
    else:
        return randChat(search)

def findAll(search,query):
    return all(item in query for item in search)

def findAny(search,query):
    return any(item in query for item in search)

def time():
    Time = datetime.datetime.now().strftime("%H:%M:")
    speak("yeha.....the time is ",Time)

def date():
    year = str(datetime.datetime.now().year)
    month = str(datetime.datetime.now().month)
    date = str(datetime.datetime.now().day)
    speak("today's date is",date,month,year)

def playMusic():
    mList = ['bullet','stay',"aromal","way maker","calm dowm","cheap thrills","oru dinam","taki taki","shape of you","thunder","senorita"]
    randMusic = random.choice(mList)
    print("Playing :",randMusic+".mp3")
    playsound('./music/'+randMusic+'.mp3')

def wishme():
    speak('Welcome Back phereena!')
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour <= 12:
        speak("Good Morning")
    elif hour >= 12 and hour <= 15:
        speak("Good Afternoon")
    elif hour >= 15 and hour <= 23:
        speak("Good Evening")
    else:
        speak("Good Night")
    speak("I am Friday, Your personal assistant. How can i help you?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing.......")
        query = r.recognize_google(audio, language="en-IN")
    except Exception as e:
        return "None"
    return query

if __name__ == "__main__":
    wishme()
    while True:
        query = takeCommand().lower()
        print(query)
        if "time" in query:
            time()
        elif "date" in query:
            date()
        elif ("name" in query) or findAll(["who","are","you"],query) :
            speak("Hi, i am friday, your personal assistant")
        elif findAll(["how","are","you"],query):
            speak("Yah, I am fine.")
        elif "friday" in query:
            speak("Hi phereena....How are you?")
        elif findAny(["fine","well"],query):
            speak("i am happy to here that")
        elif findAny(["quite","offline","shutdown"],query):
            speak("Ok.......fine.........Have a nice day")
            quit()
        elif findAll(['what','is'],query) or findAll(['who','is'],query) or findAll(['where','is'],query):
            speak("Oh... One second!")
            result = qands(" ".join(query))
            speak(result)
        elif "search" in query:
            speak("what should i search?")
            chromepath = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"
            search = takeCommand().lower()
            speak("here we go....")
            wb.get(chromepath).open_new_tab("https://www.google.com/search?q=" + search)
        elif "music" in query:
            speak("here we go....")
            playMusic()
        else:
            speak(randChat(query))
