#prompt user for rock paper scissors
#random fucntion 0-2 
#   0=rock
#   1=paper
#   2=scissors
import random as rn

options = ('rock', 'paper', 'scissors')

rpc = input("Choose either 'rock', 'paper', or 'scissors': ").lower()

while rpc != 'rock' and rpc != 'paper' and rpc != 'scissors':
    print("Not a valid input try again")
    #print(rpc)
    rpc = input("Choose either 'rock', 'paper', or 'scissors': ").lower()
    
rand = rn.choice(options)
print(rand)

if rpc == rand:
    print("Tie")
elif rpc == "rock":
    if rand == "paper":
        print("you lose")
    else:
        print('you won')
elif rpc == "paper":
    if rand == "scissors":
        print("you lose")
    else:
        print('you won')
elif rpc == "scissors":
    if rand == "rock":
        print("you lose")
    else:
        print('you won')                                                                                                  
