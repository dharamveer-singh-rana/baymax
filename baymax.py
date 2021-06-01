import pyttsx3
import speech_recognition as sr
from datetime import datetime as dt
import os
import random
from requests import get
import wikipedia
import webbrowser

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
voice_id_Brian22 = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\IVONA 2 Voice Brian22"
engine.setProperty('voice', voice_id_Brian22)


def speak(audio):
    engine.say(audio)
    print("Baymax : " + audio)
    engine.runAndWait()


def command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening....")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=None, phrase_time_limit=2.5)
    try:
        print("Recognising.....")
        print("You : " + r.recognize_google(audio, language='en-in'))
        return (r.recognize_google(audio)).lower()
    except sr.UnknownValueError:
        speak("Unable to catch! Why not give it one more shot?")
        return 'None'


def greeting():
    hour = dt.now().hour
    day = dt.today().strftime("%A")
    year = dt.today().year
    time = dt.now().time().strftime("%I:%M %p")
    if hour >= 0 and hour <= 12:
        wish = "Good Morning sir! Looks like a fresh start today!Everyday is a new beginning. Take a deep breath, smile and start again."
    elif hour > 12 and hour <= 18:
        wish = "Good Evening! How was you day sir!"
    else:
        wish = "Good Night Sir! I know you are exhausted but it’s a long night. So, you’ll have plenty of time to sleep and to dream. Good night my friend. Have a sound sleep!"
    speak(wish + "It's " + day + " today." + " And current time is " + time)


if __name__ == "__main__":
    # speak("Hi, I am BAY MAX")
    # speak("It's 12:10 a.m. in the morning and weather will be humid or rainy as per the forecast. Also you're connected to satellite 1o9 6. Current Battery status is 82 percent.")
    # command()
    greeting()
    speech = command().lower()
    if speech != 'None':
        if "play music" in speech:
            dir = "F:\\Soothing Songs"
            songs = os.listdir(dir)
            rd = random.choice(songs)
            os.startfile(os.path.join(dir, rd))
            # os.system('TASKKILL /F /IM vlc.exe')

        elif "ip address" in speech:
            ip = get("https://api.ipify.org").text
            speak("Sir your IP address is " + ip)

        elif ("who is" in speech) or ("wikipedia" in speech)  or ("what is" in speech) or ("who are" in speech) or ("what are" in speech) or ("search" in speech):
            speak("Let me dig the Internet for you, sir")
            speech = speech.replace("wikipedia","")
            search_result = wikipedia.summary(speech, sentences=3)
            speak("Here what I hunt down for you in web forest!")
            speak(search_result)

        elif "open youtube" in speech:
            webbrowser.open("www.youtube.com")

        elif "open google" in speech or "google" in speech:
            speak('Ok,what would you like to search on Google sir!')
            query = command()
            url = "https://www.google.com.tr/search?q={}".format(query)
            webbrowser.get('C:/Program Files/Google/Chrome/Application/chrome.exe %s').open(url)

        elif "open mail" in speech:
            webbrowser.open("https://outlook.office.com/mail/inbox")

