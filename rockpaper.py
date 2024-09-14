import random


# choice = ["rock", "paper","scissors"]

rock = '''
    ___
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    ___
---'   __)__
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    ___
---'   __)__
          ______)
       __________)
      (____)
---.__(___)
'''
choice = ["rock", "paper","scissors"]
your_choice=int(print("What is your choice ? Type 0 for rock, 1 for paper or 2 for scissors."))
computer_choice=random.randint(0,1)

print(f"Your choice {computer_choice}")
print(list[your_choice])
print(f"Computer Choice {computer_choice}")
print(list[computer_choice])
if computer_choice==0:
    if computer_choice==1:
        print("Computer win")
    elif computer_choice==2:
        print("You win")
    else:
        print("Draw")
# elif your_choice==1:
