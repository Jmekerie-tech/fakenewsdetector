import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
newVoiceRate=150
engine.setProperty('rate', newVoiceRate)

def say(audio):
    engine.say(audio)
    engine.runAndWait()

def secure_check():
    link = input("Enter the link:")
    if "https://" in link:
        say("Thw website is secure")
    else:
        say("The website is not secure, there are higher chances for the news to be fakeasdd")

secure_check()