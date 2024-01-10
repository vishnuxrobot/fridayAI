import pyttsx3 # pip install pyttsx3
import datetime # pip install datetime
import speech_recognition as sr # 1.pip pip install SpeechRecognition 2.pip install pipwin 3.pipwin install pyaudio
import os # dont want to install 

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
  
        if "songs" in query:
            songs_dir = "D:/music/car"
            songs = os.listdir(songs_dir)
            os.startfile(os.path.join(songs_dir, songs[0]))
 