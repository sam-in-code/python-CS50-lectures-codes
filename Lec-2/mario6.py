def main():
    s = int(input("Size: "))
    print_square(s)

def print_square(size):
    for i in range(size):
        print("#" * size)

main()