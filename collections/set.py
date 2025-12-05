
def execute():
    print("\n=== SET CREATION ===")
    num_set = {1, 2, 3, 4}
    print("Original set:", num_set)

    mixed_set = {1, "two", 3.0, True}
    print("Mixed type set:", mixed_set)

    empty_set = set()
    print("Empty set:", empty_set)

    name_set = set("Siddhesh")
    print("Set from string:", name_set)

    print("\n=== ADDING ELEMENTS ===")
    num_set.add(5)
    print("After add:", num_set)
    num_set.update([6, 7])
    print("After update:", num_set)

    print("\n=== REMOVING ELEMENTS ===")
    num_set.remove(7)
    print("After remove 7:", num_set)
    num_set.discard(10)  # No error if element not found
    print("After discard 10:", num_set)
    popped = num_set.pop()
    print(f"After pop (removed {popped}):", num_set)

    print("\n=== MEMBERSHIP CHECK ===")
    print("Is 3 in num_set?:", 3 in num_set)
    print("Is 10 not in num_set?:", 10 not in num_set)

    print("\n=== SET OPERATIONS ===")
    set_a = {1, 2, 3}
    set_b = {3, 4, 5}
    print("Union:", set_a | set_b)
    print("Intersection:", set_a & set_b)
    print("Difference (A-B):", set_a - set_b)
    print("Symmetric Difference:", set_a ^ set_b)

    print("\n=== USING METHODS FOR OPERATIONS ===")
    print("Union:", set_a.union(set_b))
    print("Intersection:", set_a.intersection(set_b))
    print("Difference:", set_a.difference(set_b))
    print("Symmetric Difference:", set_a.symmetric_difference(set_b))

    print("\n=== BUILT-IN FUNCTIONS ===")
    sample_set = {1, 2, 3, 4}
    print("Length:", len(sample_set))
    print("Max:", max(sample_set))
    print("Min:", min(sample_set))
    print("Sum:", sum(sample_set))

    print("\n=== CLEARING SET ===")
    sample_set.clear()
    print("After clear:", sample_set)

    print("\n=== FROZEN SET ===")
    frozen = frozenset([1, 2, 3])
    print("Frozen set:", frozen)

    print("\n=== CONVERSION BETWEEN LIST/TUPLE AND SET ===")
    my_list = [1, 2, 2, 3]
    converted_set = set(my_list)
    print("List to set:", converted_set)
    converted_list = list(converted_set)
    print("Set to list:", converted_list)

if __name__ == "__main__":
    execute()
