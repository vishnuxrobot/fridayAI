import pyttsx3
import datetime 

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
newVoiceRate = 150
engine.setProperty('rate', newVoiceRate)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak(date)
    speak(month) 
    speak(year)

def time():
    Time = datetime.datetime.now().strftime("%H:%M:")
    speak(Time)

def wishme():
    speak('Wlcome Back Vishnu!')
    speak("date is") 
    date()
    speak("time is") 
    time()
    speak("Friday at your service. How can i Help You?")


wishme() 
 