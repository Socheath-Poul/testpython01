print("-----BODY MASS INDEX(BMI)-----")
W = float(input("Input your weight in Kg: "))
H = float(input("Input your Height: "))
BMI=(W//(H**2))
if BMI <16 :
    print("Classification is Severe Thinness")
elif BMI <17:
    print("Classification is Moderate Thinness")
elif BMI <18.5:
    print("Classification is Mild Thinness")
elif BMI <25:
    print("Classification is Normal")
elif BMI < 30:
    print("Classification is Overweight")
elif BMI <35:
    print("Classification is Obese Class I")
elif BMI <40:
    print("Classification is Obese Class II")
else:
    print("Classification is Obese Class III")



# print("Your BMI = " + str(int(BMI)))
# print("Your BMI = ",int(BMI))
# print(f'For Weight = {W} and Height = {H} So Your BMI= {BMI}')
# print("For weight ={} and height ={} so Your BMI ={}".format(W,H,BMI))

#Tip Calcultor
# print("====Welcome to the tip calculator====")
# totalBill=float(input("What was the total bill ? "))
# tip=float(input("How much tip would you like to give? 10 ,12 ,15?"))
# person=float(input("How many people to spit the bill ? "))
# total=(totalBill+(totalBill*tip/100)) // person
#
# print("Each person should pay :$" + str(total))
# print(f'Eeach person should pay: {total}$')