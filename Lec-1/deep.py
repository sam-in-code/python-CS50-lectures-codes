def main():
    x = input("What is the answer to the great question of life, the universe, and everything? ")
    deep(x)

def deep(answer):
    answer = answer.strip().lower()
    if answer == "42" or answer == "forty two" or answer == "forty-two":
        print("Yes")
    else:
        print("No")

main()

