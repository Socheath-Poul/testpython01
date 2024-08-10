# mark=float(input("Your total marks= \n"))
# result=" "
# if mark>=90 :
#         result="A"
# elif mark >=80 :
#         result="B"
# elif mark >= 70:
#         result="C"
# elif mark >=60:
#         result = "D"
# elif mark >=50 :
#         result="E"
# else:
#         result="F"
#
# print(f'Your grade is {result}')

def check_day(val) :
    match val:
        case 0:
            output="Monday"
        case 1:
            output="Tuesday"
        case 2:
            output="Wednesday"
        case 3:
            output="Thursday"
        case 4:
            output="Friday"
        case 5:
            output = "Saturday"
        case 6:
            output = "Sunday"
        case _ :
            output="Wrong Type"

    print(f'Day is {output}')


# check_day(0)
# check_day(6)

# def access(user):
#     match user:
#         case 'admin' | 'manager' : return "Full access"
#         case 'teller' : return 'Limit access'
#         case _:return "No Access"
# print(access('teller'))
# data=access('admin')
# print(data)
# def greating(detail):
#     match detail:
#         case[time,name]:
#             print(f'Good {time} {name}')
#         case[time,*name]:
#             for data in name:
#                 print(f' Good {time} {data}')
#         case _:
#             print("Wrong Type")
#
#
# greating(["Moring","John","David"])

# def inte(detail):
#     match detail:
#         case [amount,duration] if amount<10000:
#             return amount*0.02 *duration
#         case [amount,duration] if amount>=10000:
#             return amount*0.03*duration
#
#
# print(inte([20000,10]))

# words=['one', 'two', 'three']
# for d in words:
#     print(f'Number {d}')
#
# i =1
# while i<6:
#     print(f'Number {i}')
#     i+=1
#
# for count in range(6):
#     print(f'Data {count}')

#10/08/2024


# for val in range(10):
#     print(val)
# for val in range(2,10):
#     print(val)
# for val in range(2,10,2):
#     print(val)

# message= '''hello from BTBBBU
# '''
# for cha in message:
#     if cha not in 'aeiouAEIOU':
#         print (cha,end="")




# numbers=(3,4,5,1)
# total=0
# for num in numbers:
#     total+=num
# print(f'Total = {total}')



# numbers=[23,45,64,78,13,48]
# for d in numbers:
#     if d%2==0:
#         print(d)

# lenNum=len(numbers)
# for ind in range(lenNum):
#     print(numbers[ind])

####Dictionary####
# numbers={10:"Ten",20:"Tewnty",30:"Thirty"}
# for val in numbers:
#     print(val)

# for val in numbers.keys():
#     print(numbers[val])

# for val in numbers.values():
#     print(val)

# for k,val in numbers.items():
#     print(f'Key = {k} val= {val}')

# num=int(input("Input your number : "))
# total=0
# for val in range (num):
#     if val%2==0:
#         total +=val
# print(f'Total = {total}')


# val1="0"
# #print(val1.isnumeric())
# while val1.isnumeric()==True:
#
#     if(val1.isnumeric()==True):
#         print(f'Your value {val1}')
#     val1 = "Test"
#print("End Loop")













