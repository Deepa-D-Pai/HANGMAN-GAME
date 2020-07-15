import random
#generate random numbers to give different guess word each time
k=random.randint(0,3)
j=random.randint(0,5)
# list of words
wordlist=[["apple","orange","papaya","banana","chikoo","mango"],["carrot","beetroot","tomato","potato","cabbage","brinjal"],["banglore","mumbai","delhi","hydrabad","hubli","chennai"],["perk","munch","kitkat","milkybar","silk","barone"]]
word=list(wordlist[k][j])
#to print '_' on board equal to number of letters in the word
hidden=[]
for i in word:
    hidden.append('_')
Game_over=False
attempts=4
#generate clue
if(k==0):
        print("CLUE: A FRUIT")
elif(k==1):
        print("CLUE: A VEGETABLE")
elif(k==2):
        print("CLUE: A CITY")
else:
        print("CLUE: A CHOCOLATE")
#actual code....loop runs until either the player wins or loses        
while not Game_over:
    print(f"You have {attempts} attempts left")
    #adds space between "_"
    hiddenStr=" ".join(hidden)
    print(f"Guessed word: {hiddenStr}")
    #create board
    print("    |--------------|")
    print("    |              "+"|" if attempts>1  else "    |              0")
    print("    |              "+"|" if attempts>2  else "    |              0")
    print("    |              "+"|" if attempts>3  else "    |              0")
    print("    |              "+"0" if attempts==4 else "    |               ")
    print("    |               ")
    print("    |               ")
    print("    ---------")
    #read input
    letterGuessed=input("Guess a Letter: ")
    #check if input in word
    if letterGuessed in word:
        print(f"Hurray! Guessed letter {letterGuessed} is in the word" )
        for i in range(0,len(word)):
            if(word[i]==letterGuessed):
                hidden[i]=word[i]
                word[i]='_'      
    else:
        print(f" NAH!! {letterGuessed} is not in the word")
        attempts-=1
        if attempts== 0:
           print("    |--------------|")
           print("    |            *****")
           print("    |              ")
           print("    |              ")
           print("    |              ")
           print("    |               ")
           print("    |               ")
           print("    ---------")
           print("YOU KILLED ME :( ")
           Game_over=True
    #check if word is completed        
    if "_" in hidden:
        continue
    else:
       print("You Won")
       print("YOU SAVED ME!!")
       Game_over=True
