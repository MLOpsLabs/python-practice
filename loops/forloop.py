
def execute():
    print("\n=== BASIC FOR LOOP (Range) ===")
    for i in range(1, 6):
        print(i, end=" ")
    print()

    print("\n=== FOR LOOP WITH STEP ===")
    for i in range(0, 10, 2):
        print(i, end=" ")
    print()

    print("\n=== FOR LOOP OVER LIST ===")
    fruits = ["apple", "banana", "mango"]
    for fruit in fruits:
        print(fruit, end=" ")
    print()

    print("\n=== FOR LOOP OVER STRING ===")
    text = "Python"
    for char in text:
        print(char, end=" ")
    print()

    print("\n=== FOR LOOP WITH BREAK ===")
    for i in range(1, 10):
        if i == 5:
            print("Breaking at", i)
            break
        print(i, end=" ")
    print()

    print("\n=== FOR LOOP WITH CONTINUE ===")
    for i in range(1, 10):
        if i % 2 == 0:
            continue
        print(i, end=" ")
    print()

    print("\n=== FOR LOOP WITH ELSE ===")
    for i in range(3):
        print(i, end=" ")
    else:
        print("\nLoop finished without break")

    print("\n=== NESTED FOR LOOPS ===")
    for i in range(1, 4):
        for j in range(1, 4):
            print(f"({i},{j})", end=" ")
    print()

    print("\n=== FOR LOOP WITH ENUMERATE ===")
    colors = ["red", "green", "blue"]
    for index, color in enumerate(colors):
        print(f"Index {index}: {color}")

    print("\n=== FOR LOOP WITH ZIP ===")
    names = ["Alice", "Bob", "Charlie"]
    scores = [85, 90, 95]
    for name, score in zip(names, scores):
        print(f"{name} scored {score}")

    print("\n=== FOR LOOP WITH DICTIONARY ===")
    my_dict = {"a": 1, "b": 2, "c": 3}
    for key, value in my_dict.items():
        print(f"{key}: {value}")

    print("\n=== FOR LOOP WITH SET ===")
    my_set = {10, 20, 30}
    for val in my_set:
        print(val, end=" ")
    print()

    print("\n=== FOR LOOP WITH RANGE AND ACCUMULATION ===")
    total = 0
    for i in range(1, 6):
        total += i
    print(f"Sum of first 5 numbers: {total}")

    print("\n=== FOR LOOP WITH LIST COMPREHENSION ===")
    squares = [x**2 for x in range(1, 6)]
    print(f"Squares: {squares}")

    print("\n=== FOR LOOP WITH CONDITIONAL LIST COMPREHENSION ===")
    even_squares = [x**2 for x in range(1, 11) if x % 2 == 0]
    print(f"Even Squares: {even_squares}")

if __name__ == "__main__":
    execute()
