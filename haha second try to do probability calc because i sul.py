from scipy.stats import binom
import matplotlib.pyplot as plt
import numpy as np

#binom(succeeded trial, total trial, prob)
def approxExpectedVal(numTrial, pMode):
    p = mul = sendback = 0
    if pMode == 4:
        p = 0.015
    elif pMode == 5:
        p = 0.008
    
    for i in range(1, 40):
        mul = binom.pmf(i, numTrial, p)
        if not np.isnan(i * mul):
            sendback += i * mul
    return sendback

def plotExpectedVal(maxTrialNum):
    ind_val = list(range(maxTrialNum))
    dataset_five = [approxExpectedVal(r, 5) for r in ind_val]
    dataset_four = [approxExpectedVal(r, 4) for r in ind_val]

    plt.plot(ind_val, dataset_five, color='red', linewidth = 3, 
         marker='o', markerfacecolor='cyan', markersize = 1)
    plt.plot(ind_val, dataset_four, color='blue', linewidth = 3, 
         marker='o', markerfacecolor='cyan', markersize = 1)
    plt.ylim(0.0, 5.0) 
    plt.xlim(1, maxTrialNum) 
    plt.xlabel('number of draw') 
    plt.ylabel('expected return (NP lv)')
    plt.title('Gacha Allocation Plot') 
    plt.show()

def inquire(maxTrialNum, tgNum, tgNumMode):
    sendback = 0
    sendbackStr = ""
    if(tgNumMode == 5):
        sendback = round(approxExpectedVal(maxTrialNum - tgNum, 4), 3)
        sendbackStr = "5*: " + str(tgNum) + ", expect: " + str(round(approxExpectedVal(tgNum, 5), 3)) + "\n4*: " + str(maxTrialNum - tgNum) + ", expect: " + str(sendback)
    elif(tgNumMode == 4):
        sendback = round(approxExpectedVal(maxTrialNum - tgNum, 5), 3)
        sendbackStr = "5*: " + str(maxTrialNum - tgNum) + ", expect: " + str(sendback) + "\n4*: " + str(tgNum) + ", expect: " + str(approxExpectedVal(tgNum, 4))
    return sendbackStr

def inquireSigma(maxTrialNum, interval):
    for i in range (1, (maxTrialNum // interval) + 1):
        print("\nif give 5* " + str(interval * i) + " draws:")
        print(inquire(maxTrialNum, interval * i, 5))


plotExpectedVal(561)
inquireSigma(561, 11)