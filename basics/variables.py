
def execute():
    # Demonstrating variable reassignment
    my_var = "I am a variable"
    print(f"Initial value: {my_var}")

    for value in [42, 3.14, True]:
        my_var = value
        print(f"Reassigned value: {my_var}")

    # Multiple variable assignments
    a, b, c = 5, 10, 15
    print(f"Multiple variables: {a}, {b}, {c}")

    a, b, c = 1, 2, 3
    print(f"Multiple assignment: {a}, {b}, {c}")

    a = b = c = 100
    print(f"Chained assignment: {a}, {b}, {c}")

if __name__ == "__main__":
    execute()
