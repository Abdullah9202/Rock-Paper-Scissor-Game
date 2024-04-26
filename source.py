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

# Creating a nested list
all_List = [rock, paper, scissors]

# Taking user input
user_Choice = int( input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. : "))
# Print out the user choice
print(f"You chose\n{all_List[user_Choice]}")

# Generating random choice of the computer
pc_Num_Pick = random.randint(0, len(all_List) - 1)
# Picking from random index
pc_Choice = all_List[pc_Num_Pick]
# Print out the PC choice
print(f"Computer chose\n{pc_Choice}")


# Making decision acording to the rules

# Rock wins against scissors
# Scissors wins against paper
# Paper wins against rock

# Checking the conditions ==> (Using truth table would be better)
if user_Choice >= 3 or user_Choice < 0:
    print("You typed an invalid number, you lose!")
elif user_Choice == pc_Num_Pick:
    print("It's a draw")
elif user_Choice == 0 and pc_Num_Pick == 1:
    print("You lose!")
elif user_Choice == 0 and pc_Num_Pick == 2:
    print("You win!")
elif user_Choice == 1 and pc_Num_Pick == 0:
    print("You win!")
elif user_Choice == 1 and pc_Num_Pick == 2:
    print("You lose!")
elif user_Choice == 2 and pc_Num_Pick == 0:
    print("You lose!")
else:
    print("You win!")