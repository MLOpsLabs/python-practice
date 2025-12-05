
def execute():
    print("\n=== BASIC GENERATOR FUNCTION ===")
    def simple_generator():
        yield 1
        yield 2
        yield 3

    gen = simple_generator()
    print(next(gen))  # 1
    print(next(gen))  # 2
    print(next(gen))  # 3
    # Uncomment below to see StopIteration
    # print(next(gen))

    print("\n=== GENERATOR WITH LOOP ===")
    def count_up_to(n):
        i = 1
        while i <= n:
            yield i
            i += 1

    for num in count_up_to(5):
        print(num, end=" ")
    print()

    print("\n=== GENERATOR FOR SQUARES ===")
    def squares(n):
        for i in range(n):
            yield i ** 2

    for sq in squares(5):
        print(sq, end=" ")
    print()

    print("\n=== GENERATOR WITH CONDITIONAL LOGIC ===")
    def even_numbers(n):
        for i in range(n):
            if i % 2 == 0:
                yield i

    print("Even numbers up to 10:", list(even_numbers(10)))

    print("\n=== GENERATOR EXPRESSIONS ===")
    gen_exp = (x ** 2 for x in range(5))
    print("Squares using generator expression:", list(gen_exp))

    print("\n=== USING next() WITH GENERATOR ===")
    gen = count_up_to(3)
    print(next(gen))  # 1
    print(next(gen))  # 2
    print(next(gen))  # 3

    print("\n=== MEMORY EFFICIENCY DEMO ===")
    # Compare generator vs list comprehension
    import sys
    gen_exp = (x for x in range(1000000))
    list_comp = [x for x in range(1000000)]
    print("Generator size:", sys.getsizeof(gen_exp))
    print("List comprehension size:", sys.getsizeof(list_comp))

if __name__ == "__main__":
    execute()
