from module5_mod import NumberProcessor

def main():
    n = int(input("Enter N (the number of integers to input): "))
    processor = NumberProcessor()
    processor.read_n_numbers(n)

    x = int(input("Enter X (the integer to search for): "))
    result = processor.search_x(x)

    if result == -1:
        print("-1")
    else: 
        print("the index of {} is {}.".format(x, result))

if __name__ == "__main__":
    main()