#number1 = 33
#number2 = 40

#if number1 > number2:
#    print(f" {number1} is greater than {number2}")
#else:
#    print(f"{number1} is not greater than {number2}")

#print("....please kindly check if youre eligible to use this app....")
#checkage = int(input("how old are you ? : "))

#if checkage < 18:
#    print("youre not eligible")
#else:
#    print("welcome, this app is for you")

#    print("proceed to the next step")

#checkcgpa = float(input("whats your cgpa ? : "))

#if checkcgpa > 3.5:
#    print("your're qualified")
#else:
#    print("you have to try again next year after you upgrade")



print("welcome to our banking page")
checkAge = int(input("enter your age"))

if checkAge > 30:
    print("youre eligible")
    checkSalary = int(input("your monthly income"))
    if checkSalary > 50000:
        print("you can proceed")
        checkSocial = input("are you on facebook? y/n ")
        if checkSocial == "yes":
            print("thats good, you can proceed")
        else:
            print("you will need to create a facebook account before you can proceed")

    else:
        print("your salary is too low for this loan")


else:
    print("youre not eligible")





