#non return function
def greeting(name):
    print("Hello",name)


greeting("John")

#return function
# def get_total(val1,val2):
#     total=val1+val2
#     return total
#
# # print(get_total(4,5))
#
# totat=get_total(4,5)
# print(totat)

#Test Pass by value

# def test_fun(val):
#     print(f'Id = {id(val)}')
#     val=val+1
#     print(f'Id after change {id(val)}')
#     print(val)
#
# amount=5
# test_fun(amount)
# print(f'Id outside {id(amount)}')
# print(amount)

#31/08/2024
# def interest(amt,rate,/):
#     return amt*rate/100
# interest_amt= interest(10000,1)
# print(f'Interest Amount {interest_amt}')
#
# def myFunction(a,x,/,y,b,*,z,w):
#     print(a,x,y,b,z,w)
#
# myFunction(1,2,3,2 ,w=3,z=4)
#
# def show_infor(name,city):
#     print(name,city)
#
# show_infor("Dara","BTB")


# def fcn(nums,numberlist=[]):
#     numberlist.append(nums+1)
#     print(numberlist)
# fcn(5)
# fcn(10)
# fcn(15)


# def greeting(message,*name):
#     for val in name:
#         print(f'{message} {val}')
#
# greeting("Good morning","Thida","Dara","Pisey")

#lambda
# sum=lambda val1,val2:val1+val2
# print(sum(2,3))
#14/09/2024
# def myFumction(a:int,b:int)->int:
#     return a+b
#
# print(myFumction("app","le"))

def myFumction(a:"Should int",b:"Should int"=10)->int:
    return a+b

print(myFumction.__annotations__)