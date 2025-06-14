#Tip Calculator 

print("Welcome to Tip Calculator!")

bill=float(input("What was the total bill? $ "))

tip=int(input("How much tip would you like to give? 10, 12, or 15? "))

people=int(input("How many people to split the bill? "))

actualBill=bill+(bill*(tip/100))
eachPay=actualBill/people
final="{:.2f}".format(eachPay)

print(f"Each person should pay: ${final}")