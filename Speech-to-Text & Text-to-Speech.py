import pyttsx3
import speech_recognition

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
engine.setProperty("rate", 200)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 600
        try:
            audio = r.listen(source, timeout=4)
            print("Understanding...")
            query = r.recognize_google(audio, language='en-in')
            print(f"You said: {query}")
        except Exception as e:
            print("Pls repeat again")
            return "None"
        return query

if __name__ == "__main__":
    print("Press 1 for Speech to Text")
    print("Press 2 for Text to Speech")
    a = input("Enter Your Choice: ")

    if a == "1":
        print("Speak 'Exit' or 'End' to terminate")
        while True:
            query = takeCommand()
            if query.lower() == "exit" or query.lower() == "end":
                break

    elif a == "2":
        print("Type 'Exit' or 'End' to terminate")
        while True:
            query = input("Enter a sentence: ")
            print(f"You entered: {query}")
            if query.lower() == "exit" or query.lower() == "end":
                break
            speak(query)