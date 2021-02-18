import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import pyjokes

name = input('Choose a name\n')

listener = sr.Recognizer()
engine = pyttsx3.init()


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            if name in command:
                command = command.replace(name, '')
                print(command)
    except:
        pass
    return command


def run_AI():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%H:%M')
        print(time)
        talk('Current time is ' + time)
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk('Please say the command again.')


while True:
    run_AI()
