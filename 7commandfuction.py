import pyttsx3
import datetime
import speech_recognition as sr # 1.pip pip install SpeechRecognition 2.pip install pipwin 3.pipwin install pyaudio

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
newVoiceRate = 170
engine.setProperty('rate', newVoiceRate)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()



def time():
    Time = datetime.datetime.now().strftime("%H:%M:")
    speak(Time)

def wishme():
    speak('Welcome Back Vishnu!')
    speak("The current time is") 
    time()
    hour = datetime.datetime.now().hour

    if hour >= 6 and hour <= 12:
        speak("good Morning")
    elif hour >= 12 and hour <= 15:
        speak("Good afternoon")
    elif hour >=15 and hour <=23:
        speak("Good Evening") 
    else:
        speak("Good Night")        
    speak(" Ralph at your service. How can i Help You?")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        speak("Say something!")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Yaa Got it! i am putting Forward")
        speak("Yaa Got it! i am putting Forward")
        query = r.recognize_google(audio, language ="en-US")
        print(query)
    except Exception as e:
        print(e)
        speak("Say that again....")

        return "None"

    return query

wishme()
takeCommand()

 