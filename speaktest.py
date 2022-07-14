schoolDeck = ["台大資工","臺大電機","台大資管","交大資管金融","交大電機","交大資工","清大資工甲","清大資工乙","清大電機","清大電資學士"]
schoolDeckRates = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
decisionKey = -1;

for i in range(0, len(schoolDeck)):
    for j in range (i+1, len(schoolDeck)):
        print("\n0: ", schoolDeck[i])
        print("\n1: ", schoolDeck[j])
        decisionKey = input("\nIndicate your preference -> ")
        if(decisionKey == "0"): 
            schoolDeckRates[i] += 1
        if(decisionKey == "1"):
            schoolDeckRates[j] += 1

            
presentChoices = []
for i in range(0, len(schoolDeck)):
    presentChoices.append([schoolDeck[i], schoolDeckRates[i]])
    
presentChoices.sort(key = lambda x:x[0])

for i in range(0, len(presentChoices)):
    print(presentChoices[i][0], ": ", str(presentChoices[i][1]))