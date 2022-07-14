import pyttsx3 as speech
engine = speech.init()
voices = engine.getProperty('voices');

for i in range(len(voices)):
    engine.setProperty('voice', voices[i].id)
    engine.say("hello, this language is number" + str(i))
    print("hello, this language is number" + str(i))
    engine.runAndWait()