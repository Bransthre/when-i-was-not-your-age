import random as R;
import pyttsx3;
engine = pyttsx3.init();

userRes = "r";
qList = open("Interview Question Masterlist Northwestern.txt", "r",encoding='utf-8');
lines = qList.readlines();
qNum = 1

engine.setProperty('rate', 170);
voices = engine.getProperty('voices');
engine.setProperty('voice', voices[1].id);

assignmentTxt = "Please answer the question, then: \nType key 'n' to end interview \nType key 'r' to continue interview with randomized questions \nType key 'd' to continue interview with specific question of your choice \n Type your decision here: ";
sepLine = "\n====================================================================================\n";

print("\nWelcome to interview simulator!");
print("Author: Dun-Ming Huang \nDefault Mode: Random Questions");

while userRes != "n":
    
    if userRes == "r":
    	lineNum = int(round( 140 * R.random() + 1, 0));
    	intQ = "" + lines[lineNum];
    	engine.say(intQ);
    	print(sepLine + "\nThis is random question " + str(qNum) + " " + str(lineNum)  + ": "+ intQ + sepLine);
    	engine.runAndWait();
    	qNum += 1;
    	userRes = input(assignmentTxt);
        
    elif userRes == "d":
        switchNumConfirm = input("Do you want to stay on the current question? Key y to confirm, key other question number to move onto another question:　")
        if switchNumConfirm == "y":
            lineNum = int(lineNum);
        elif (1 <= int(switchNumConfirm) and int(switchNumConfirm) <= 140):
            lineNum = int(switchNumConfirm);
        intQ = "" + lines[lineNum];
        engine.say(intQ);
        print(sepLine + "\nThis is question " + str(lineNum) + ": "+ intQ + sepLine);
        engine.runAndWait();
        userRes = input(assignmentTxt);
    else:
        userRes = input(assignmentTxt);
    
print("Bye, user. Good luck on your interviews, don't forget to practice with and after simulations!            ")
engine.say("Bye, user. Good luck on your interviews, don't forget to practice with and after simulations!            ")
engine.runAndWait();