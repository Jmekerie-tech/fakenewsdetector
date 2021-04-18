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
    trust_factor = 0
    link = input("Enter the news link:")
    if "https://" in link:
        trust_factor += 1
    else:
        say("There are higher chances for the news to be fake, becouse of the link...")
    if "protv" in link:
        trust_factor += 1
    if "digi" in link:
        trust_factor += 1
    if "observator" in link:
        trust_factor += 1
    if "sport.ro" in link:
        trust_factor += 1
    if trust_factor == 2:
        say("The news are over 90 percents true!")
    else:
        say("Acording to our algorithm, there are higher chances for the news to be fake.")
secure_check()