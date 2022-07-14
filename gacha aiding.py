import random

def averageTimes(sampleCnt, gachaProb):
    sendback, maximumCnt, minimumCnt = 0, 0, 0
    cntArr = []
    for i in range(sampleCnt):
        currentCnt, currentNP = 0, 0
        while(currentNP < 5):
            if(random.random() <= gachaProb):
                currentNP += 1
            currentCnt += 1
        if(currentCnt > maximumCnt):
            maximumCnt = currentCnt
        if(currentCnt < minimumCnt):
            minimumCnt = currentCnt
        cntArr.append(currentCnt)
        sendback += currentCnt / sampleCnt
    cntArr.sort()
    print("Minimum count was: " + str(cntArr[0]))
    print("Maximum count was: " + str(cntArr[-1]))
    print("Average count was: " + str(round(sendback, 2)))

averageTimes(1000, 0.015)