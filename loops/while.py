
def execute():
    print("\n=== BASIC WHILE LOOP ===")
    i = 1
    while i <= 5:
        print(i, end=" ")
        i += 1
    print()

    print("\n=== WHILE WITH BREAK ===")
    i = 1
    while i <= 10:
        if i == 6:
            print("Breaking at", i)
            break
        print(i, end=" ")
        i += 1
    print()

    print("\n=== WHILE WITH CONTINUE ===")
    i = 0
    while i < 10:
        i += 1
        if i % 2 == 0:
            continue
        print(i, end=" ")
    print()

    print("\n=== WHILE WITH ELSE ===")
    i = 1
    while i <= 3:
        print(i, end=" ")
        i += 1
    else:
        print("\nLoop finished without break")

    print("\n=== INFINITE LOOP WITH BREAK ===")
    count = 0
    while True:
        print("Looping...", count)
        count += 1
        if count == 3:
            print("Breaking infinite loop")
            break

    print("\n=== WHILE LOOP WITH USER INPUT ===")
    # Uncomment for interactive input
    # while True:
    #     user_input = input("Enter 'exit' to stop: ")
    #     if user_input.lower() == 'exit':
    #         break
    #     print("You entered:", user_input)

    print("\n=== WHILE LOOP WITH LIST ITERATION ===")
    items = [10, 20, 30]
    index = 0
    while index < len(items):
        print(f"Item {index}: {items[index]}")
        index += 1

    print("\n=== WHILE LOOP WITH NESTED CONDITIONS ===")
    x = 0
    while x < 5:
        if x % 2 == 0:
            print(f"{x} is even")
        else:
            print(f"{x} is odd")
        x += 1

    print("\n=== WHILE LOOP WITH ACCUMULATION ===")
    total = 0
    num = 1
    while num <= 5:
        total += num
        num += 1
    print(f"Sum of first 5 numbers: {total}")

if __name__ == "__main__":
    execute()
