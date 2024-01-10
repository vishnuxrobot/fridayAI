import pyttsx3 # pip install pyttsx3
import datetime # pip install datetime
import speech_recognition as sr # 1.pip pip install SpeechRecognition 2.pip install pipwin 3.pipwin install pyaudio
import wikipedia # pip install wikipedia
import webbrowser as wb # dont want to install 

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
newVoiceRate = 160
engine.setProperty('rate', newVoiceRate)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()



def time():
    Time = datetime.datetime.now().strftime("%H:%M:")
    speak("yeha..the time is")
    speak(Time)

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("today's date is")
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
    speak("i am your Fryday. How can i Help You?")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recoganinsing.......")
        query = r.recognize_google(audio, language ="en-IN")
        print(query)
    except Exception as e:
        print(e)
        speak("i didn't get you...........Say that again....")

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
        elif "friday" in query:
            speak("Hi vishnu....How are you?")
        elif "fine" in query:
            speak("i am happy to here that")
        elif "offline" in query:
            speak("Ok.......fine.........Have a nice day")
            quit()
                
        elif "wikipedia" in query:
            speak("Searching.....")
            query = query.replace("wikipedia", "")
            speak("i got something")
            result = wikipedia.summary(query, sentences = 2)
            speak(result)

        elif "search" in query:
            speak("what should i search?")
            chromepath = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
            search = takeCommand().lower()
            wb.get(chromepath).open_new_tab(search + ".com")

        
 