name = input("What is your name? ")

match name:
    case "Robert":
        print("House Baratheon")
    case "Tywin":
        print("House Lannister")
    case "Eddard":
        print("House Stark")
    case _:
        print("Who?")
                    