
def execute():
    print("\n=== DICTIONARY CREATION ===")
    my_dict = {"a": 1, "b": 2, "c": 3}
    print("Original dictionary:", my_dict)

    empty_dict = {}
    print("Empty dictionary:", empty_dict)

    dict_from_constructor = dict(x=10, y=20)
    print("Dictionary using dict():", dict_from_constructor)

    dict_from_list = dict([("name", "Alice"), ("age", 25)])
    print("Dictionary from list of tuples:", dict_from_list)

    nested_dict = {
        "person": {"name": "Bob", "age": 30},
        "address": {"city": "Pune", "zip": 411001}
    }
    print("Nested dictionary:", nested_dict)

    print("\n=== ACCESSING ELEMENTS ===")
    print("Value for key 'a':", my_dict["a"])
    print("Using get():", my_dict.get("b"))
    print("Using get() with default:", my_dict.get("z", "Not Found"))

    print("\n=== ADDING AND UPDATING ELEMENTS ===")
    my_dict["d"] = 4
    print("After adding key 'd':", my_dict)
    my_dict.update({"e": 5, "f": 6})
    print("After update():", my_dict)

    print("\n=== REMOVING ELEMENTS ===")
    removed = my_dict.pop("f")
    print(f"After pop('f') (removed {removed}):", my_dict)
    popped_item = my_dict.popitem()
    print(f"After popitem() (removed {popped_item}):", my_dict)
    my_dict.clear()
    print("After clear():", my_dict)

    print("\n=== RECREATING DICTIONARY FOR MORE OPERATIONS ===")
    my_dict = {"a": 1, "b": 2, "c": 3, "d": 4}
    print("New dictionary:", my_dict)

    print("\n=== DICTIONARY METHODS ===")
    print("Keys:", list(my_dict.keys()))
    print("Values:", list(my_dict.values()))
    print("Items:", list(my_dict.items()))

    print("\n=== MEMBERSHIP CHECK ===")
    print("Is 'a' in dictionary?:", "a" in my_dict)
    print("Is 'z' not in dictionary?:", "z" not in my_dict)

    print("\n=== BUILT-IN FUNCTIONS ===")
    print("Length:", len(my_dict))
    print("Max key:", max(my_dict))
    print("Min key:", min(my_dict))
    print("Sum of values:", sum(my_dict.values()))

    print("\n=== NESTED DICTIONARY ACCESS ===")
    print("Name from nested dict:", nested_dict["person"]["name"])

    print("\n=== DICTIONARY COMPREHENSIONS ===")
    squares = {x: x**2 for x in range(1, 6)}
    print("Squares dictionary:", squares)

    print("\n=== CONVERSION BETWEEN DICT AND OTHER TYPES ===")
    tuple_list = [("x", 10), ("y", 20)]
    converted_dict = dict(tuple_list)
    print("List of tuples to dict:", converted_dict)
    print("Dict to list of tuples:", list(converted_dict.items()))

if __name__ == "__main__":
    execute()
