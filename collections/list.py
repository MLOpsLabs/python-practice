
def execute():
    print("\n=== LIST CREATION ===")
    num_list = [1, 2, 3, 4]
    print("Original list:", num_list)

    nested_list = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    print("Nested list:", nested_list)

    multi_type_list = [1, "two", 3.0, True, [5,6], (7,8), {9: 'nine'}]
    print("Multi-type list:", multi_type_list)

    empty_list = list()
    print("Empty list:", empty_list)

    name_list = list("Siddhesh")
    print("List from string:", name_list)

    print("\n=== ACCESSING ELEMENTS ===")
    print("First element:", num_list[0])
    print("Last element:", num_list[-1])

    print("\n=== SLICING ===")
    print("First 3 elements:", num_list[:3])
    print("Every second element:", num_list[::2])

    print("\n=== ADDING ELEMENTS ===")
    num_list.append(5)
    print("After append:", num_list)
    num_list.extend([6, 7])
    print("After extend:", num_list)
    num_list.insert(2, 99)
    print("After insert at index 2:", num_list)

    print("\n=== REMOVING ELEMENTS ===")
    num_list.remove(99)
    print("After remove 99:", num_list)
    popped = num_list.pop()
    print(f"After pop (removed {popped}):", num_list)
    num_list.clear()
    print("After clear:", num_list)

    print("\n=== RECREATING LIST FOR MORE OPERATIONS ===")
    num_list = [1, 2, 3, 4, 2, 3]
    print("New list:", num_list)

    print("\n=== SEARCHING ===")
    print("Index of 3:", num_list.index(3))
    print("Count of 2:", num_list.count(2))
    print("Is 4 in list?:", 4 in num_list)

    print("\n=== SORTING AND REVERSING ===")
    num_list.sort()
    print("Sorted list:", num_list)
    num_list.reverse()
    print("Reversed list:", num_list)

    print("\n=== OTHER USEFUL FUNCTIONS ===")
    print("Length:", len(num_list))
    print("Max:", max(num_list))
    print("Min:", min(num_list))
    print("Sum:", sum(num_list))

    print("\n=== COPYING LIST ===")
    copy_list = num_list.copy()
    print("Copied list:", copy_list)

    print("\n=== LIST COMPREHENSIONS ===")
    squares = [x**2 for x in range(1, 6)]
    print("Squares:", squares)
    even_numbers = [x for x in range(10) if x % 2 == 0]
    print("Even numbers:", even_numbers)

    print("\n=== NESTED LIST ACCESS ===")
    print("Element [1][2] from nested list:", nested_list[1][2])

if __name__ == "__main__":
    execute()
