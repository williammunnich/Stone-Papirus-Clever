#prompt user for rock paper scissors

import random as rn

def RockPaperScissors(choice):
    
    options = ('rock', 'paper', 'scissors')

    

    '''while rpc != 'rock' and rpc != 'paper' and rpc != 'scissors':
        print("Not a valid input try again")
        #print(rpc)
     '''   
        
    rand = rn.choice(options)
    print(rand)

    if choice == rand:
        return "you both chose "  + choice + ". it's a tie"
    elif choice == "rock":
        if rand == "paper":
            return "you chose "  + choice + ". The bot chose " + rand + '. you lost'
        else:
            return "you chose "  + choice + ". The bot chose " + rand + '. you won'
    elif choice == "paper":
        if rand == "scissors":
            return "you chose "  + choice + ". The bot chose " + rand + '. you lost'
        else:
            return "you chose "  + choice + ". The bot chose " + rand + '. you won'
    elif choice == "scissors":
        if rand == "rock":
            return "you chose "  + choice + ". The bot chose " + rand + '. you lost'
        else:
            return "you chose "  + choice + ". The bot chose " + rand + '. you won'    
    else: 
        return "Invalid choice try again."                                      
#rpc = input("Choose either 'rock', 'paper', or 'scissors': ").lower()
#print(RockPaperScissors(rpc))
