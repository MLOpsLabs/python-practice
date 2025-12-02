
def execute():
    print("\n=== ARITHMETIC OPERATORS ===")
    a, b = 10, 3
    print(f"a + b = {a + b}")
    print(f"a - b = {a - b}")
    print(f"a * b = {a * b}")
    print(f"a / b = {a / b}")      # Float division
    print(f"a // b = {a // b}")    # Floor division
    print(f"a % b = {a % b}")      # Modulus
    print(f"a ** b = {a ** b}")    # Exponentiation

    print("\n=== COMPARISON OPERATORS ===")
    print(f"a == b: {a == b}")
    print(f"a != b: {a != b}")
    print(f"a > b: {a > b}")
    print(f"a < b: {a < b}")
    print(f"a >= b: {a >= b}")
    print(f"a <= b: {a <= b}")

    print("\n=== LOGICAL OPERATORS ===")
    x, y = True, False
    print(f"x and y: {x and y}")
    print(f"x or y: {x or y}")
    print(f"not x: {not x}")

    print("\n=== BITWISE OPERATORS ===")
    a, b = 10, 3  # Binary: 1010 & 0011
    print(f"a & b = {a & b}")   # AND
    print(f"a | b = {a | b}")   # OR
    print(f"a ^ b = {a ^ b}")   # XOR
    print(f"~a = {~a}")         # NOT
    print(f"a << 2 = {a << 2}") # Left shift
    print(f"a >> 2 = {a >> 2}") # Right shift

    print("\n=== ASSIGNMENT OPERATORS ===")
    c = 5
    print(f"Initial c = {c}")
    c += 2; print(f"c += 2 → {c}")
    c -= 1; print(f"c -= 1 → {c}")
    c *= 3; print(f"c *= 3 → {c}")
    c /= 2; print(f"c /= 2 → {c}")
    c //= 2; print(f"c //= 2 → {c}")
    c %= 2; print(f"c %= 2 → {c}")
    c = 5; c **= 2; print(f"c **= 2 → {c}")
    c = 5; c &= 3; print(f"c &= 3 → {c}")
    c = 5; c |= 3; print(f"c |= 3 → {c}")
    c = 5; c ^= 3; print(f"c ^= 3 → {c}")
    c = 5; c <<= 1; print(f"c <<= 1 → {c}")
    c = 5; c >>= 1; print(f"c >>= 1 → {c}")

    print("\n=== IDENTITY OPERATORS ===")
    x = [1, 2, 3]
    y = x
    z = [1, 2, 3]
    print(f"x is y: {x is y}")
    print(f"x is z: {x is z}")
    print(f"x is not z: {x is not z}")

    print("\n=== MEMBERSHIP OPERATORS ===")
    my_list = [1, 2, 3, 4]
    print(f"my list: {my_list}")
    print(f"2 in my_list: {2 in my_list}")
    print(f"5 not in my_list: {5 not in my_list}")

if __name__ == "__main__":
    execute()
