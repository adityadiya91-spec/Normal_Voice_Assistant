## Voice Assistant (Python)
This project is a basic voice assistant written in Python.
It listens to voice commands through the microphone and responds using speech.
The assistant can tell the current time, search Wikipedia, play YouTube videos, tell jokes, and exit on command.


## Description
The voice assistant records audio from the microphone, converts speech to text using Google Speech Recognition, processes the command, and gives a spoken response using text-to-speech.
The program runs continuously and waits for user commands until the user says stop or exit.


## Functionalities
i.Listens to voice input
ii.Converts speech to text
iii.Speaks responses
iv.Tells the current time
v.Searches and reads Wikipedia summaries
vi.Plays songs or videos on YouTube
vii.Tells jokes
viii.Stops the assistant on command
## Libraries Used
1.speech_recognition
2.pyttsx3
3.datetime
4.wikipedia
5.pywhatkit
6.pyjokes
7.sounddevice
8.numpy


## How the Program Works
a)The assistant records audio from the microphone for a few seconds.
b)The recorded audio is converted into text.
c)The text is analyzed to identify keywords like:
    I.time
    II.wikipedia
    III.play
    IV.joke
    V.stop / exit
d)Based on the command, the assistant performs the required action.
e)The assistant responds using voice output.
f)The process repeats in a loop.

## Example Commands

Ex1: “What is the time”

Ex2: “Wikipedia Python programming”

Ex3: “Play Believer”

Ex4: “Tell me a joke”

Ex5: “Exit”

## Notes
1.Internet connection is required for speech recognition and Wikipedia search.
2.Clear speech and low background noise improve accuracy.
3.The assistant listens for 5 seconds for each command.

## Author
Adityakumar Pandey

## contact: adityadiya91@gmail.com
