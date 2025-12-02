def execute():
    name = input("Enter your name: ")
    print(f"Hello, {name}!")
    age = input("Enter your age: ")
    print(f"You are {age} years old.")
    
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    sum_result = num1 + num2
    print(f"The sum of {num1} and {num2} is {sum_result}.")

if __name__ == "__main__":
    execute()
    