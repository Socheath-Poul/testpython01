import random
import string

#Get all string , symbol and number
myString=string.ascii_lowercase
mySymbol=string.punctuation
myNumber=string.digits

#### Test Password Generator#####
print("Welcome to Password Generator")
let=int(input("How many letters would you like in your password?\n"))
sym=int(input("How many symbols would you like in your password?\n"))
num=int(input("How many numbers would you like?\n"))

# print(myString)
# print(mySymbol)
# print(myNumber)

# print(myString)
####Way1
tmpPassword=[]
tmpPassword+=random.choices(myString,k=let)
tmpPassword+=random.choices(mySymbol,k=sym)
tmpPassword+=random.choices(myNumber,k=num)

random.shuffle(tmpPassword)

tmpPassword=''.join(tmpPassword)
print(f'Your password should be :  {tmpPassword}')


###Way2
#Loop pick values
# for d in  range(let):
#     tmpPassword +=random.choice(myString)
#
# for d in  range(sym):
#     tmpPassword +=random.choice(mySymbol)
#
# for d in  range(num):
#     tmpPassword +=random.choice(myNumber)
# #Convert string to list
# tmpPassword=list(tmpPassword)
# #Shuffle List
# random.shuffle(tmpPassword)
# #Convert list to string
# tmpPassword=''.join(tmpPassword)
#
# print(f'Your password should be {tmpPassword}')








