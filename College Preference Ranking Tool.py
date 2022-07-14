ItemDeck = ["banana", "mushroom", "snake meat", "chicken testicle", "pig liver", "watermelon"]
ItemDeckRates = []

for i in range(0, len(ItemDeck)):
    ItemDeckRates.append(0)

decisionKey = -1;

for i in range(0, len(ItemDeck)):
    for j in range (i+1, len(ItemDeck)):
        print("\n0: ", ItemDeck[i])
        print("\n1: ", ItemDeck[j])
        decisionKey = input("\nIndicate your preference -> ")
        if(decisionKey == "0"): 
            ItemDeckRates[i] += 1
        if(decisionKey == "1"):
            ItemDeckRates[j] += 1

            
presentChoices = []
for i in range(0, len(ItemDeck)):
    presentChoices.append([ItemDeck[i], ItemDeckRates[i]])
    
presentChoices.sort(key = lambda x:x[1], reverse = True)

for i in range(0, len(presentChoices)):
    print((i+1), "th place is: ", presentChoices[i][0], ": ", str(presentChoices[i][1]))