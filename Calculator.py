a = int(input("Please enter a number 1: "))
b = int(input("Please enter a number 2: "))

print("+ - * /")
choice = input("Please entere a the Operator to perform the operation: ")

if(choice == "+"):
    print(f"The sum is {a+b}")

elif(choice == "-"):
    print(f"The subtraction is {a-b if a>=b else b-a}")

elif(choice == "*"):
    print(f"The Multiplication is {a*b}")

elif(choice == "/"):
    print(f"The devide is {a/b}")

else:
    print("Wrong Input")