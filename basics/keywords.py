
import keyword

def execute():
    """
    Demonstrates Python keywords and identifiers.
    - Keywords: Reserved words in Python with predefined meaning.
    - Identifiers: Names for variables, functions, classes, etc.
    """

    # Display all Python keywords
    keywords = keyword.kwlist
    print("Python Keywords:")
    print(", ".join(keywords))
    print(f"\nTotal number of keywords: {len(keywords)}")

    # Identifiers vs Keywords
    valid_identifiers = ["my_var", "execute", "MyClass", "my_function", "_private_var", "var123"]
    invalid_identifiers = ["1stVar", "my-var", "def", "class", "import", "my var"]

    print("\nSample Valid Identifiers:")
    print(", ".join(valid_identifiers))

    print("\nInvalid Identifiers (keywords or invalid characters):")
    print(", ".join(invalid_identifiers))

if __name__ == "__main__":
    execute()
