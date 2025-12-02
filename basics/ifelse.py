
def execute():
    print("\n=== BASIC IF ===")
    x = 10
    if x > 5:
        print(f"{x} is greater than 5")

    print("\n=== IF-ELSE ===")
    y = 3
    if y % 2 == 0:
        print(f"{y} is even")
    else:
        print(f"{y} is odd")

    print("\n=== IF-ELIF-ELSE ===")
    score = 85
    if score >= 90:
        print("Grade: A")
    elif score >= 75:
        print("Grade: B")
    elif score >= 60:
        print("Grade: C")
    else:
        print("Grade: D")

    print("\n=== NESTED IF ===")
    age = 20
    if age >= 18:
        if age >= 60:
            print("Senior Citizen")
        else:
            print("Adult")
    else:
        print("Minor")

    print("\n=== SHORT HAND IF ===")
    a = 5
    if a > 0: print("Positive number")

    print("\n=== SHORT HAND IF-ELSE (TERNARY) ===")
    b = -3
    print("Positive" if b > 0 else "Negative")

    print("\n=== MULTIPLE CONDITIONS (AND/OR) ===")
    num = 15
    if num > 10 and num < 20:
        print(f"{num} is between 10 and 20")
    if num < 0 or num > 10:
        print(f"{num} is either negative or greater than 10")

    print("\n=== USING IN MEMBERSHIP ===")
    fruits = ["apple", "banana", "mango"]
    if "apple" in fruits:
        print("Apple is in the list")
    else:
        print("Apple is not in the list")

    print("\n=== USING IS FOR IDENTITY ===")
    x = None
    if x is None:
        print("x is None")
    else:
        print("x is not None")

    # print("\n=== COMBINING IF WITH INPUT ===")
    # Uncomment below lines for interactive input
    # user_input = int(input("Enter a number: "))
    # print("Even" if user_input % 2 == 0 else "Odd")

if __name__ == "__main__":
    execute()
