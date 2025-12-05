
def execute():
    text = "  Hello World!  "
    print("\n=== Original String ===")
    print(f"'{text}'")

    print("\n=== Case Conversion ===")
    print("upper():", text.upper())
    print("lower():", text.lower())
    print("title():", text.title())
    print("capitalize():", text.capitalize())
    print("swapcase():", text.swapcase())

    print("\n=== Whitespace Handling ===")
    print("strip():", text.strip())
    print("lstrip():", text.lstrip())
    print("rstrip():", text.rstrip())

    print("\n=== Searching ===")
    print("find('World'):", text.find("World"))
    print("rfind('l'):", text.rfind("l"))
    print("index('Hello'):", text.index("Hello"))
    print("rindex('l'):", text.rindex("l"))
    
    print("capitalize():", text.capitalize())
    print("swapcase():", text.swapcase())
    print("title():", text.title())
    print("upper():", text.upper())
    print("lower():", text.lower())
    print("casefold():", text.casefold())


    print("\n=== Counting ===")
    print("count('l'):", text.count("l"))

    print("\n=== Replace ===")
    print("replace('World', 'Python'):", text.replace("World", "Python"))

    print("\n=== Splitting and Joining ===")
    print("split():", text.split())
    print("split('o'):", text.split("o"))
    print("rsplit('o'):", text.rsplit("o"))
    print("splitlines():", "Line1\nLine2".splitlines())
    print("join(['a','b','c']):", "-".join(['a','b','c']))

    print("\n=== Checking Start/End ===")
    print("startswith('Hello'):", text.strip().startswith("Hello"))
    print("endswith('!'):", text.strip().endswith("!"))

    print("\n=== Alignment ===")
    print("center(20,'*'):", text.center(20, '*'))
    print("ljust(20,'-'):", text.ljust(20, '-'))
    print("rjust(20,'-'):", text.rjust(20, '-'))

    print("\n=== Zero Fill ===")
    print("'42'.zfill(5):", "42".zfill(5))

    print("\n=== Encoding/Decoding ===")
    encoded = text.encode('utf-8')
    print("encode('utf-8'):", encoded)
    print("decode('utf-8'):", encoded.decode('utf-8'))

    print("\n=== Character Checks ===")
    sample = "Python123"
    print("isalnum():", sample.isalnum())
    print("isalpha():", "Python".isalpha())
    print("isdigit():", "123".isdigit())
    print("isdecimal():", "123".isdecimal())
    print("isnumeric():", "123".isnumeric())
    print("isspace():", "   ".isspace())
    print("islower():", "python".islower())
    print("isupper():", "PYTHON".isupper())
    print("istitle():", "Python Is Fun".istitle())

    print("\n=== Partitioning ===")
    print("partition('World'):", text.partition("World"))
    print("rpartition('l'):", text.rpartition("l"))

    print("\n=== Formatting ===")
    print("format():", "My name is {} and I am {} years old".format("Alice", 25))
    print("f-string:", f"My name is {'Alice'} and I am {25} years old")

    print("\n=== Translation ===")
    trans_table = str.maketrans("Helo", "1234")
    print("translate():", text.translate(trans_table))

    print("\n=== Expand Tabs ===")
    print("'Hello\tWorld'.expandtabs(10):", "Hello\tWorld".expandtabs(10))

    print("\n=== Casefold (Aggressive Lowercase) ===")
    print("casefold():", text.casefold())

if __name__ == "__main__":
    execute()
