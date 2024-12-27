def huge_income(name):
    print(f'Dear {name},you have lot of money')

def low_income(name):
    print(f"opps {name},your income is below requirement")



nameinput = input("enter your name   ..")
checksalary = int(input("whats your salary?"))

if checksalary > 50000:
    huge_income(nameinput)

else:
    low_income(nameinput)    


huge_income