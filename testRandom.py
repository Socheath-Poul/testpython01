import random

print(random.randint(2, 50))

print(random.random())
print(random.random()*100)

# guess=["Head","Tails"]
# choosen=random.randint(0,1)
# print(guess[choosen])

choosen=random.randint(0,1)
if choosen ==0:
    print("Head")
else:
    print("Tails")

