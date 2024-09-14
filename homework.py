message = '''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    .--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .  `` ,  `"-._"-._   ". '|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."/` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,.--o;   |
|___________________|_| ;     (#) -.o "=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
'''

print(message)

print("Welcome to Treasure Island")
print("Your mission is to find the treasure.")
print("==============================================================")

choices1 = input('You\'re at a crossroad, where do you want to go? Type "left" or "right": ').lower()
if choices1 == "left":
    choices2 = input('You\'ve come to a lake. There is an island in the middle of the lake. '
                    'Type "wait" to wait for a boat. Type "swim" to swim across: ').lower()
    if choices2 == "wait":
        choices3 = input('You arrive at the island unharmed. There is a house with 3 doors. '
                        'One red, one yellow, and one blue. Which color do you choose? ').lower()
        if choices3 == "yellow":
            print("Congratulations! You Win!!!")
        elif choices3 == "red":
            print("Game over.")
        elif choices3 == "blue":
            print("Game over.")
        else:
            print("Game over.")
    else:
        print("Game over.")
else:
    print("Game over.")


