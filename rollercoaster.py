print("======Welcome to rollercoaster======")
height=int(input("What is your height in cm : "))
if height >= 120 :
    print("OK, you can ride rollcoaster ")
    age=int(input("How old are you? "))
    bill=0
    if age <=12:
        bill=5
        #print("You have to pay 5$.")
    elif age <=18:
        bill = 7
        #print("You have to pay 7$.")
    else:
        bill=12
        # print("You have to pay 12$.")

    photo=input("Do you want photo? Y or N")
    if photo.lower()== "y":
        bill +=3

    print(f"You will pay {bill}$")

else:
    print("Sorry , we will wait until you grow up.")