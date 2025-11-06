import random
game_console=''' 
/        _____________        \  
| == .  |             |     o |  
|   _   |             |    B  |  
|  / \  |             | A   O |  
| | O | |             |  O    |  
|  \_/  |             |       |  
|       |             | . . . |  
|  :::  |             | . . . |  
|  :::  |_____________| . . . |  
|           S N K             |  
\_____________________________/
'''
print(game_console)
print("Let's Play Bro")
user=input("Enter your input in game ")
computer_choice=random.choice(["Rock","Scissor","Paper"])
print(user,computer_choice)

if user==computer_choice:
    print("Your choice and sytem choice both are same ,match ties")
elif user=="Rock":
    if computer_choice=="scissor":
        print("Rock Break scissor ,User wins")
    else:
        print("Computer wins")
elif user=="Scissor":
    if computer_choice=="paper":
        print("Scissor cut paper ,User wins")
    else:
        print("Computer wins")
elif user=="Paper":
    if computer_choice=="Rock":
        print("Paper Fold rock ,User wins")
    else:

        print("Computer wins")
