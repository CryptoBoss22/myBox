balance = 100

# our functions

def options():
    print("welcome to our seamless online banking")
    print("kindly choose from the options below")
    print("1. check balance")
    print("2. withdraw ")
    print("3. deposit")
    print("3. transfer")
    

def checkbalance(balance):

    balance
    print(f"your balance is {balance}")



def withdraw(balance):
    withdrawamount = int(input("Enter amount ..."))
    if withdrawamount > balance:
        print(" your have exceeded your withdrawal balance")
    else:
        balance = balance - withdrawamount 
        print(f"this is your current balance after withdrawal {balance}")


def deposit(balance):
    depositamount = int(input("enter deposit amount"))
    balance = depositamount + balance
    print(f"this is your current balance {balance}")


def transfer():
    pass



# main code
options()
chooseoptions = int(input("select from options : "))


# input condition


if chooseoptions == 1:
    checkbalance(balance)
elif chooseoptions == 2:
    withdraw(balance)
elif chooseoptions == 3:
    deposit(balance)
else:
    print("kindly choose from the options listed above, do you want to proceed? //y/n")
    question = input("yes or no.....")
    if question == "yes":
        options()
    else:
        print("thank you for banking with ,see you next time")
