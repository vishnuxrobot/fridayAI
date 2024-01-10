import pyttsx3
import datetime
import speech_recognition as sr # 1.pip pip install SpeechRecognition 2.pip install pipwin 3.pipwin install pyaudio

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
newVoiceRate = 150
engine.setProperty('rate', newVoiceRate)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()



def time():
    Time = datetime.datetime.now().strftime("%H:%M:")
    speak("hi boss the time is")
    speak(Time)

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("hi boss the date is")
    speak(date)
    speak(month)
    speak(year)

def wishme():
    speak('Welcome Back Vishnu!')

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
        print("Recoganinsing.......")
        query = r.recognize_google(audio, language ="en-US")
        print(query)
    except Exception as e:
        print(e)
        speak("Say that again....")

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
        elif "offline" in query:
            speak("Ok Bye have a nice day")
            quit()    



 