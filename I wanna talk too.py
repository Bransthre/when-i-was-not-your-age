import pyttsx3 as speech
engine = speech.init()
voices = engine.getProperty('voices');
engine.setProperty('rate', 190)
engine.setProperty('volume', 1)
engine.setProperty('voice', voices[1].id);

def switchLang(num):
    engine.setProperty('voice', voices[num].id)

def adjustSpeed(num):
    engine.setProperty('rate', num)

def speakAsBot():
    while True:
        print("input your words:")
        sentence = str(input())
        if(sentence == "lang"):
            print("input language:")
            langCode = int(input())
            switchLang(langCode)
            continue
        elif(sentence == "speed"):
            print("input speed:")
            wordsPerMin = int(input())
            adjustSpeed(wordsPerMin)
            continue
        elif(sentence == "halt"):
            break
        engine.say(sentence)
        engine.runAndWait()
        
speakAsBot()

#Just switch speaker from sound settings
#3 is Japanese, 4 is Chinese