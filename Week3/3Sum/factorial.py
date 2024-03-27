def factorial(userInput):
    # userInput = int(input("enter a num: "))

    if userInput == 1:
        return 1
    return userInput * factorial(userInput -1)



print(factorial(5))
