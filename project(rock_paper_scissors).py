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
user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
print("computer choose")
random_num = random.randint(0,2)
print(random_num)
rps = [rock,paper,scissors]
print(rps[random_num])

if user_input == 0 and random_num == 1 :
    print("you lose")
elif user_input == 0 and random_num == 2:
    print("you win")
elif user_input == 1 and random_num == 0:
    print("you win")
elif user_input == 1 and random_num == 2:
    print("you lose")
elif user_input == 2 and random_num == 0:
    print("you lose")
elif user_input == 2 and random_num == 1:
    print("you win")
else:
    print("match tie")


# # User choice
# user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))
#
# rps = [rock, paper, scissors]
#
# if user_input < 0 or user_input > 2:
#     print("Invalid choice! You lose.")
# else:
#     print("You chose:")
#     print(rps[user_input])
#
#     # Computer choice
#     random_num = random.randint(0, 2)
#     print("Computer chose:")
#     print(rps[random_num])
#
#     # Decide winner
#     if user_input == random_num:
#         print("It's a draw!")
#     elif (user_input == 0 and random_num == 2) or \
#          (user_input == 1 and random_num == 0) or \
#          (user_input == 2 and random_num == 1):
#         print("You win!")
#     else:
#         print("You lose!")