#Calculator Program

logo = r"""
 _____________________
|  _________________  |
| | Calulator    0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def multi(a,b):
    return a*b

def div(a,b):
    return a/b

operation={"+":add , "-":sub , "*":multi , "/":div}

def calculator():
    num1=float(input("Enter first number?:"))
    for i in operation:
        print(i)

    start=True

    while start:
        user_oper=input("Pick an operation: ")
        if user_oper not in operation:
            print("Not a Valid Operation")
            calculator()
        num2=float(input("Enter next number?:"))
        calc=operation[user_oper]
        ans=calc(num1,num2)
        print(f"\n{num1} {user_oper} {num2} = {ans}")
        num1=ans
        ask=input("Type 'y' to continue calculation and 'n' to restart or else press other key to end : ").lower()
        if ask=="y":
            num1=ans
        elif ask=="n":
            start=False
            calculator()
        else:
            start=False

print(logo)
calculator()