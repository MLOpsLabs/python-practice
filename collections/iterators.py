
class CountDown:
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.start <= 0:
            raise StopIteration
        current = self.start
        self.start -= 1
        return current

def execute():
    print("\n=== BASIC ITERATOR USING iter() AND next() ===")
    my_list = [1, 2, 3]
    iterator = iter(my_list)
    print(next(iterator))  # 1
    print(next(iterator))  # 2
    print(next(iterator))  # 3
    # Uncomment below to see StopIteration
    # print(next(iterator))

    print("\n=== ITERATING USING FOR LOOP (Implicit Iterator) ===")
    for item in my_list:
        print(item, end=" ")
    print()

    countdown = CountDown(5)
    for num in countdown:
        print(num, end=" ")
    print()

    print("\n=== ITERATOR USING BUILT-IN FUNCTIONS ===")
    text = "Python"
    iterator = iter(text)
    print("Characters using next():", end=" ")
    while True:
        try:
            print(next(iterator), end=" ")
        except StopIteration:
            break
    print()

if __name__ == "__main__":
    execute()
