def execute():
    my_string = "Hello, World!"
    my_integer = 100
    my_float = 25.5
    my_boolean = True
    my_list = [1, 2, 3, 4, 5]
    my_tuple = (10, 20, 30)
    my_dict = {"name": "Siddhesh", "age": 25}
    my_complex = 3 + 4j  # Complex number

    print("Type :", type(my_string))
    print("String:", my_string, end="\n\n")
    
    print("Type :", type(my_integer))
    print("Integer:", my_integer, end="\n\n")
    
    print("Type :", type(my_float))
    print("Float:", my_float, end="\n\n")
    
    print("Type :", type(my_boolean))
    print("Boolean:", my_boolean, end="\n\n")
    
    print("Type :", type(my_list))
    print("List:", my_list, end="\n\n")
    
    print("Type :", type(my_tuple))
    print("Tuple:", my_tuple, end="\n\n")
    
    print("Type :", type(my_dict))
    print("Dictionary:", my_dict, end="\n\n")
    
    print("Type :", type(my_complex))
    print("Complex Number:", my_complex, end="\n\n")
    
    x = 1
    print("Type :", type(x))
    x = 1e308
    print("Type :", type(x))
    print(x)

if __name__ == "__main__":
    execute()