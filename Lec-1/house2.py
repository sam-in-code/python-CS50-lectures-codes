name = input("What is your name? ")

match name:
    case "Robert" | "Stannis" | "Renly":
        print("House Baratheon")
    case "Eddard" | "Robb" | "Sansa":
        print("House Stark")
    case "Tywin" | "Jaime" | "Tyrion":
        print("House Lannister")
    case _:
        print("Who?")
                   