def main():
    print("Welcome to the Pokemon Battle Simulator!")
    pokemon1 = input("Enter the name of the first Pokemon: ")
    pokemon2 = input("Enter the name of the second Pokemon: ")
    
    print(f"\nBattle between {pokemon1} and {pokemon2}!")
    print(f"{pokemon1} attacks {pokemon2}!")
    print(f"{pokemon2} attacks {pokemon1}!")
    
    winner = input("Who won the battle? (Enter the name of the winning Pokemon): ")
    
    print(f"\nCongratulations to {winner} for winning the battle!")
main()        