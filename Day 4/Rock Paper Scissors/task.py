import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
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

game_images = [rock, paper, scissors]

my_choice = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n '))
print()
print("Your chose: ")
if my_choice >=0 and my_choice <=2:
    print(game_images[my_choice])
# if my_choice == 1:
#     print(rock)
# elif my_choice ==2:
#     print(paper)
# elif my_choice == 3:
#     print(scissors)
comp_move = random.randint(0, 2)
print('Computer chose: ')
print(game_images[comp_move])
# if comp_move == 1:
#     print(rock)
# elif comp_move ==2:
#     print(paper)
# elif comp_move == 3:
#     print(scissors)

if my_choice >=3 or my_choice < 0:
    print('Invalid nuber. You lose!')
elif my_choice == 0 and comp_move == 2:
    print("You win!")
elif my_choice == 2 and comp_move == 0:
    print("You lose!")
elif my_choice > comp_move:
    print('You win!')
elif my_choice < comp_move:
    print('You lose!')
elif my_choice == comp_move:
    print('It is a draw!')

