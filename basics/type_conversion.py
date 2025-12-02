
import keyword
import ast

def execute():
    print("\n=== IMPLICIT TYPE CONVERSION ===")
    
    # int + float → float
    num_int, num_float = 10, 3.5
    print(f"Before: {num_int} ({type(num_int)}), {num_float} ({type(num_float)})")
    result = num_int + num_float
    print(f"After: {result} ({type(result)})\n")

    # bool + int → int
    num_bool, num_int = True, 5
    print(f"Before: {num_bool} ({type(num_bool)}), {num_int} ({type(num_int)})")
    result = num_bool + num_int
    print(f"After: {result} ({type(result)})\n")

    # int + complex → complex
    num_int, num_complex = 5, 3+4j
    print(f"Before: {num_int} ({type(num_int)}), {num_complex} ({type(num_complex)})")
    result = num_int + num_complex
    print(f"After: {result} ({type(result)})\n")

    print("\n=== EXPLICIT TYPE CONVERSION ===")

    # str → int
    num_str = "100"
    print(f"Before: {num_str} ({type(num_str)})")
    num_int = int(num_str)
    print(f"After: {num_int} ({type(num_int)})\n")

    # str → float
    num_str = "45.67"
    print(f"Before: {num_str} ({type(num_str)})")
    num_float = float(num_str)
    print(f"After: {num_float} ({type(num_float)})\n")

    # float → int
    num_float = 3.99
    print(f"Before: {num_float} ({type(num_float)})")
    num_int = int(num_float)
    print(f"After: {num_int} ({type(num_int)})\n")

    # int → str
    num_int = 200
    print(f"Before: {num_int} ({type(num_int)})")
    num_str = str(num_int)
    print(f"After: {num_str} ({type(num_str)})\n")

    # int → bool
    num_int = 0
    print(f"Before: {num_int} ({type(num_int)})")
    num_bool = bool(num_int)
    print(f"After: {num_bool} ({type(num_bool)})\n")

    # list → tuple
    my_list = [1, 2, 3]
    print(f"Before: {my_list} ({type(my_list)})")
    my_tuple = tuple(my_list)
    print(f"After: {my_tuple} ({type(my_tuple)})\n")

    # tuple → list
    my_tuple = (4, 5, 6)
    print(f"Before: {my_tuple} ({type(my_tuple)})")
    my_list = list(my_tuple)
    print(f"After: {my_list} ({type(my_list)})\n")

    # list → set
    my_list = [1, 2, 2, 3]
    print(f"Before: {my_list} ({type(my_list)})")
    my_set = set(my_list)
    print(f"After: {my_set} ({type(my_set)})\n")

    # tuple of pairs → dict
    my_tuple = (("a", 1), ("b", 2))
    print(f"Before: {my_tuple} ({type(my_tuple)})")
    my_dict = dict(my_tuple)
    print(f"After: {my_dict} ({type(my_dict)})\n")

    # str → complex
    num_str = "3+4j"
    print(f"Before: {num_str} ({type(num_str)})")
    num_complex = complex(num_str)
    print(f"After: {num_complex} ({type(num_complex)})\n")

    # str → bytes
    text = "Hello"
    print(f"Before: {text} ({type(text)})")
    text_bytes = bytes(text, 'utf-8')
    print(f"After: {text_bytes} ({type(text_bytes)})\n")

    # str → bytearray
    print(f"Before: {text} ({type(text)})")
    text_bytearray = bytearray(text, 'utf-8')
    print(f"After: {text_bytearray} ({type(text_bytearray)})\n")

    # str → eval (dynamic conversion)
    expr = "100 + 50"
    print(f"Before: {expr} ({type(expr)})")
    result = eval(expr)
    print(f"After: {result} ({type(result)})\n")

    # str → literal_eval (safe)
    data = "[1, 2, 3]"
    print(f"Before: {data} ({type(data)})")
    result = ast.literal_eval(data)
    print(f"After: {result} ({type(result)})\n")

    # Error handling example
    invalid_str = "abc"
    print(f"Trying to convert '{invalid_str}' to int:")
    try:
        num = int(invalid_str)
    except ValueError:
        print("Error: Cannot convert to int\n")

if __name__ == "__main__":
    execute()
