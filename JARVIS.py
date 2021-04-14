# imports
import speech_recognition as speech
import webbrowser
import pyttsx3
from time import sleep
from datetime import datetime

# instance of Recognizer class
r = speech.Recognizer()

# confs for pyttsx3
IronMan_Jarvis = pyttsx3.init()
IronMan_Jarvis.setProperty('rate', 200)
IronMan_Jarvis.setProperty('volume', 1.0)

# function to speak 
def speak(text):
  IronMan_Jarvis.say(text)
  IronMan_Jarvis.runAndWait()

# function to translate our voice into a text_version of the recording
def recognize_voice():
  text = ' '
  # create an instance of the Microphone class
  with speech.Microphone() as source:
    # adjust for ambient noise
    r.adjust_for_ambient_noise(source)
    # Records a single phrase from source
    voice_recording = r.listen(source)

    try:
      # speech recognition using the Google Speech Recognition API
      text = r.recognize_google(voice_recording)
    except speech.RequestError:
      # handles errors with recognize_google function
      speak("My apologies, failed to access Google API")
    except speech.UnknownValueError:
      # handles errors with unknown voice_recording values
      speak("My apologies, could not understand what you said")
  return text.lower()

# Jarvis's replies including: 
# 'name', 'how are you', 'time', 'search', and 'age'
def reply(text):
  if "name" in text:
    speak("My name is Jarvis short for Just A Rather Very Intelligent System sir")
  
  if "how are you" in text:
    speak("Online and ready sir ")

  if "date" in text:
    date = datetime.now().strftime("%-d %B %Y")
    speak("As you wish sir")
    speak(date)

  if "time" in text:
    time = datetime.now().time().strftime("%H %M")
    speak("The time is " + time)

  if "age" in text:
    speak("Well, that is a diffcult question, I could not give you an answer")
  
  if "search" in text:
    speak("What would you like me to look up?")
    keyword = recognize_voice()
    if keyword != '':
      url = "https://google.com/search?q=" + keyword
      speak("Here are the search results for " + keyword)
      webbrowser.open(url)
      sleep(1)
  
  # quit program
  if "quit" in text:
    speak("As you wish, powering off now")
    exit()
  # exit program
  if "exit" in text: 
    speak("As you wish, powering off now")
    exit()

# allow recognize_voice to finish
sleep(1)

# run until quit or exit is spoken
while True:
  speak("At your service sir...")
  text_version = recognize_voice()
  reply(text_version)