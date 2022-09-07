
from random import randint

#Starting point/main variables
roles = ["Bear", "Ninja", "Cowboy"]
computer = roles[randint(0, 2)]
player = False
score = 0

#Welcome Message
print(f"Get ready to play Bear, Ninja, or Cowboy!!")

#Ask if they need instructions
instructions = input("Do you need instructions? (yes/no) > ")
if instructions.lower() == "yes":
    print("Choose a character and see if you win!")
else:
    print("Ah, so you've been here before...")

#Get player input

while player == False:
    player = input("Choose One: Bear, Ninja, or Cowboy? > ")
    computer = roles[randint(0, 2)]

#Define Logic/Rules
def winner(player, computer):
    if computer == player:
        print("DRAW!")
    elif computer == "Cowboy":
        if player == "Bear":
            print("You lose!", computer, "shoots", player)
        else: #if computer is ninja, player is ninja
            print("You win!", player, "defeats", computer)
    elif computer == "Bear":
        if player == "Cowboy":
            print("You win!", player, "shoots", computer)
        else: #if computer is bear, player is ninja
            print("You lose!", computer, "eats", player)
    elif computer == "Ninja":
        if player == "Cowboy":
            print("You lose!", computer, "defeats", player)
        else: #if computer is ninja, player is bear
            print("You win!", player, "eats", computer)



#Ask them to play again
play_again = input("Would you like to play again? (yes/no) > ")
#create the loop -- need to come back to this, I can't figure it out
if play_again == "yes":
    player = False
    computer = roles[randint(0, 2)]
else:
    print("GAME OVER")
   
