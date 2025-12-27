import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import pywhatkit
import pyjokes
import sounddevice as sd
import numpy as np

engine = pyttsx3.init()
engine.setProperty('rate', 170)

recognizer = sr.Recognizer()

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        print("Listening... (speak)")
        duration = 5        
        sample_rate = 16000

        audio = sd.rec(
            int(duration * sample_rate),
            samplerate=sample_rate,
            channels=1,
            dtype='int16'
        )
        sd.wait()

        audio_data = sr.AudioData(
            audio.tobytes(),
            sample_rate,
            2 
        )

        command = recognizer.recognize_google(audio_data)
        command = command.lower()
        print("You said:", command)
        return command

    except sr.UnknownValueError:
        return ""

    except sr.RequestError:
        talk("Internet connection problem")
        return ""

    except Exception as e:
        print("Error:", e)
        return ""

def run_assistant():
    command = take_command()

    if command == "":
        return

    if 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk("Current time is " + time)

    elif 'wikipedia' in command:
        talk("Searching Wikipedia")
        command = command.replace("wikipedia", "")
        try:
            info = wikipedia.summary(command, sentences=2)
            talk(info)
        except:
            talk("Sorry, I couldn't find that")

    elif 'play' in command:
        song = command.replace('play', '')
        talk("Playing " + song)
        pywhatkit.playonyt(song)

    elif 'joke' in command:
        talk(pyjokes.get_joke())

    elif 'stop' in command or 'exit' in command:
        talk("Goodbye")
        exit()

    else:
        talk("Sorry, I did not understand")

talk("Voice assistant started")

while True:
    run_assistant()
