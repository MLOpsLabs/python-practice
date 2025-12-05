
def execute():
    print("\n=== BASIC LAMBDA FUNCTION ===")
    add = lambda x, y: x + y
    print("Addition using lambda:", add(5, 3))

    print("\n=== LAMBDA WITH SINGLE ARGUMENT ===")
    square = lambda x: x ** 2
    print("Square of 4:", square(4))

    print("\n=== LAMBDA WITH NO ARGUMENT ===")
    greet = lambda: "Hello, World!"
    print(greet())

    print("\n=== LAMBDA WITH DEFAULT ARGUMENTS ===")
    power = lambda x, y=2: x ** y
    print("Power (5^2):", power(5))
    print("Power (5^3):", power(5, 3))

    print("\n=== LAMBDA INSIDE SORTING ===")
    numbers = [(1, 'one'), (3, 'three'), (2, 'two')]
    sorted_numbers = sorted(numbers, key=lambda x: x[0])
    print("Sorted by first element:", sorted_numbers)

    print("\n=== LAMBDA WITH MAP ===")
    nums = [1, 2, 3, 4]
    squares = list(map(lambda x: x ** 2, nums))
    print("Squares using map:", squares)

    print("\n=== LAMBDA WITH FILTER ===")
    evens = list(filter(lambda x: x % 2 == 0, nums))
    print("Even numbers using filter:", evens)

    print("\n=== LAMBDA WITH REDUCE ===")
    from functools import reduce
    sum_all = reduce(lambda x, y: x + y, nums)
    print("Sum using reduce:", sum_all)

    print("\n=== LAMBDA WITH CONDITIONAL EXPRESSION ===")
    check_even = lambda x: "Even" if x % 2 == 0 else "Odd"
    print("Check 5:", check_even(5))
    print("Check 8:", check_even(8))

    print("\n=== LAMBDA IN DICTIONARY ===")
    operations = {
        "add": lambda x, y: x + y,
        "sub": lambda x, y: x - y,
        "mul": lambda x, y: x * y
    }
    print("Add using dict lambda:", operations"add")
    print("Mul using dict lambda:", operations"mul")

    print("\n=== LAMBDA WITH SORTING BY STRING LENGTH ===")
    words = ["apple", "banana", "kiwi"]
    sorted_words = sorted(words, key=lambda w: len(w))
    print("Sorted by length:", sorted_words)

    print("\n=== LAMBDA WITH NESTED FUNCTION ===")
    def apply_func(func, value):
        return func(value)
    print("Apply lambda:", apply_func(lambda x: x * 10, 7))

if __name__ == "__main__":
    execute()
