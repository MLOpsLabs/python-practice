
def execute():
    print("\n=== TUPLE CREATION ===")
    num_tuple = (1, 2, 3, 4)
    print("Original tuple:", num_tuple)

    nested_tuple = ((1, 2), (3, 4), (5, 6))
    print("Nested tuple:", nested_tuple)

    multi_type_tuple = (1, "two", 3.0, True, [5, 6], (7, 8), {9: 'nine'})
    print("Multi-type tuple:", multi_type_tuple)

    empty_tuple = tuple()
    print("Empty tuple:", empty_tuple)

    single_element_tuple = (5,)
    print("Single element tuple:", single_element_tuple)

    name_tuple = tuple("Siddhesh")
    print("Tuple from string:", name_tuple)

    print("\n=== ACCESSING ELEMENTS ===")
    print("First element:", num_tuple[0])
    print("Last element:", num_tuple[-1])

    print("\n=== SLICING ===")
    print("First 3 elements:", num_tuple[:3])
    print("Every second element:", num_tuple[::2])

    print("\n=== CONCATENATION AND REPETITION ===")
    tuple1 = (1, 2)
    tuple2 = (3, 4)
    print("Concatenated tuple:", tuple1 + tuple2)
    print("Repeated tuple:", tuple1 * 3)

    print("\n=== MEMBERSHIP CHECK ===")
    print("Is 3 in num_tuple?:", 3 in num_tuple)
    print("Is 10 not in num_tuple?:", 10 not in num_tuple)

    print("\n=== TUPLE METHODS ===")
    sample_tuple = (1, 2, 2, 3, 4, 2)
    print("Count of 2:", sample_tuple.count(2))
    print("Index of 3:", sample_tuple.index(3))

    print("\n=== BUILT-IN FUNCTIONS ===")
    print("Length:", len(sample_tuple))
    print("Max:", max(sample_tuple))
    print("Min:", min(sample_tuple))
    print("Sum:", sum(sample_tuple))

    print("\n=== PACKING AND UNPACKING ===")
    packed_tuple = (10, 20, 30)
    a, b, c = packed_tuple
    print(f"Unpacked values: a={a}, b={b}, c={c}")

    print("\n=== CONVERSION BETWEEN LIST AND TUPLE ===")
    my_list = [1, 2, 3]
    converted_tuple = tuple(my_list)
    print("List to tuple:", converted_tuple)
    converted_list = list(converted_tuple)
    print("Tuple to list:", converted_list)

    print("\n=== NESTED TUPLE ACCESS ===")
    print("Element [1][0] from nested tuple:", nested_tuple[1][0])

if __name__ == "__main__":
    execute()
