import time 
import pyttsx3 as speech

engine = speech.init();

voices = engine.getProperty('voices');
engine.setProperty('rate', 150)
engine.setProperty('voice', voices[1].id);

engine.say("タイマー　エンジン　起動します")
engine.runAndWait()

# define the countdown func. 
def countdown(t): 
    engine.runAndWait()
    while t: 
        time.sleep(1) 
        t -= 1
  
  
# input time in seconds 

# function call 

def timer(timePeriod):
    engine.say("timer is set for " + str(timePeriod / 60) + " minutes")
    engine.runAndWait()
    timeLimit = timePeriod * 60
    ptr = 0
    while(time):
        time.sleep(60)
        timeLimit -= 60
        ptr += 1
        engine.say(str(ptr) + "minutes has passed, quick donkey")
        engine.runAndWait()

def pomodoroJ(periodNum, workInterval, restInterval):
    engine.say("Pomodoro Initiate")
    engine.setProperty("voice", voices[3].id)
    engine.runAndWait()
    for i in range(periodNum):
        engine.say("ワーク ピリオド: " + str(i + 1) + " 開始")
        engine.runAndWait()
        print("ワーク ピリオド: " + str(i + 1) + "開始")
        countdown(workInterval * 30)
        
        engine.say("ワーク　ピリオド　" + str(i + 1) + " 半分経過")
        engine.runAndWait()
        print("ワーク　ピリオド　" + str(i + 1) + "半分経過")
        countdown(workInterval * 30)
        
        engine.say("ワーク　ピリオド　" + str(i + 1) + " 終了")
        engine.runAndWait()
        print("ワーク　ピリオド　" + str(i + 1) + "終了")
        engine.say("レスト　ピリオド　" + str(i + 1) + " 開始")
        engine.runAndWait()
        print("レスト　ピリオド　" + str(i + 1) + "開始")
        countdown(restInterval * 30)
        
        engine.say("レスト　ピリオド　" + str(i + 1) + " 半分経過")
        engine.runAndWait()
        print("レスト　ピリオド　" + str(i + 1) + "半分経過")
        countdown(restInterval * 30)
        
        engine.say("レスト　ピリオド　" + str(i + 1) + " 終了")
        engine.runAndWait()
        print("レスト　ピリオド　" + str(i + 1) + "終了")
        
def pomodoroE(periodNum, workInterval, restInterval):
    engine.setProperty("voice", voices[1].id)
    engine.say("Pomodoro Initiate")
    engine.runAndWait()
    for i in range(periodNum):
        engine.say("work period: " + str(i + 1) + " start")
        engine.runAndWait()
        print("work period: " + str(i + 1) + " start")
        countdown(workInterval * 30)
        
        engine.say("work period　" + str(i + 1) + " half")
        engine.runAndWait()
        print("work period　" + str(i + 1) + " half")
        countdown(workInterval * 30)
        
        engine.say("work period　" + str(i + 1) + " end")
        engine.runAndWait()
        print("work period　" + str(i + 1) + " end")
        engine.say("rest period　" + str(i + 1) + " start")
        engine.runAndWait()
        print("rest period　" + str(i + 1) + "start")
        countdown(restInterval * 30)
        
        engine.say("rest period　" + str(i + 1) + " half")
        engine.runAndWait()
        print("rest period　" + str(i + 1) + "half")
        countdown(restInterval * 30)
        
        engine.say("rest period　" + str(i + 1) + " end")
        engine.runAndWait()
        print("rest period　" + str(i + 1) + "end")

pomodoroJ(10, 30, 6)  