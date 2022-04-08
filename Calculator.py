import math

# define functions
def addition(x,y):
    return x+y
def subtraction(x,y):
    return x-y
def multiplication(x,y):
    return x*y
def division(x,y):
    return x/y
def second_Power(x):
    return x**2
def square_root(x):
    return math.sqrt(x)

# Options for users to choose from
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. second_power")
print("6. square_root")
print("7. exit")

# Start loop.
while True:
    
    # user input number
    choice=input("choose operation: ")
   
    # stop and exit programe
    if choice == '7':
        print("Goodbye!")
        break
    
    # addition
    if choice == '1':
        num1=int((input("enter first number: ")))
        num2=int((input("enter second number: ")))
        print(num1, "+" ,num2, "=", addition(num1, num2))
    
    # subtraction
    if choice == '2':
        num1=int((input("enter first number: ")))
        num2=int((input("enter second number: ")))
        print(num1, "-", num2, "=", subtraction(num1, num2))
    
    # multiplication
    if choice == '3':
        num1=int((input("enter first number: ")))
        num2=int((input("enter second number: ")))
        print(num1, "*", num2, "=", multiplication(num1, num2))
    
    # division
    if choice == '4':
        num1=int((input("enter first number: ")))
        num2=int((input("enter second number: ")))
        print(num1, "/", num2, "=", division(num1, num2))
    
    # second_Power
    elif choice =='5':
        num3 = int(input("enter number: "))
        print(num3,"** 2=",second_Power(num3))
    
    # square_root
    elif choice =='6':
        num3 = int(input("enter number: "))
        print("√",num3,"=",math.sqrt(num3))
