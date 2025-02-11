import random
rock = '''
_______
-'   ____)
    (_____)
    (_____)
    (____)
---.__(___)
'''

paper = '''
_______
--'   ____)____
        ______)
        _______)
        _______)
---.__________)
'''

scissors = '''
_______
---'   ____)____
        ______)
    __________)
    (____)
---.__(___)
'''
player = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
list_player = [rock,paper,scissors]
# player_user = list_player[player]
print(list_player[player])
#computer program
list_player_len = len(list_player)
int_player = random.randint(0,2)
names_player = list_player[int_player-0]
print(names_player)



if int_player == 2 and player == 0:
    print("you won!")
elif int_player == player:
    print("The match is draw")
elif int_player > player:
    print("you lose")
elif int_player == 0 and player == 2:
    print("You lose")
elif int_player < player:
    print("you won")
else:
    print("you have entered wrong number")



# list_player_len_usr = len(list_player)
# if list_player_len_usr > names_player_1:
#     print("computer won the game")
# elif list_player_len_usr < names_player_1:
#     print("user won the game")
# elif list_player_len_usr == names_player_1:
#     print("Draw the match")
# else:
#     print("Restart The Game")


    
# rock = scissors
# scissors = Papper
# Papper = rock


# if computer_choice == 0:
#     print("Rock")
# elif computer_choice == 1:
#     print("Papper")
# elif computer_choice == 2:
#     print("Scissors")
# else:
#     print("none")

