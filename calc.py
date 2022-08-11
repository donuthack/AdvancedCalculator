import requests
import os

def add(a, b):
    return a+b

def subtract(a, b):
    return a-b

def multiply(a, b):
    return a*b

def divide(a, b):
    return a // b
    
def read_file(path):
    f = open(path, "r")
    lines = f.readlines()
    return lines
    
def request_response(url):
    response = requests.get(url)
    return response.content
    
def os_commands(inputed_command):
    return os.system(inputed_command)


print("Select what you want to do: ")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Read file")
print("6. Return response")
print("7. Execute OS command(for Linux)")

while True:
    choice = input("Enter choice(1/2/3/4/5/6/7): ")

    # check if choice is one of the four options
    if choice in ('1', '2', '3', '4', '5', '6', '7'):
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        
        elif choice == '5':
            input_path = str(input("Enter path to file: "))
            print(read_file(input_path))
        
        elif choice == '6':
            input_link = str(input("Enter link for sending request: "))
            print(request_response(input_link))
        
        elif choice == '7':
            input_command = str(input("Enter your command: "))
            print(os_commands(input_command))
        
        
        next_step = input("Let's do next calculation? (y/n): ")
        if next_step == "n":
          break
    
    else:
        print("Invalid Input")
