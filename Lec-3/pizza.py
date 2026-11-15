def main():
    print("Welcome to the Pizza Order System!")
    size = input("Enter pizza size (small, medium, large): ")
    toppings = input("Enter toppings (comma-separated): ")
    
    order = {
        "size": size,
        "toppings": [t.strip() for t in toppings.split(",")]
    }
    
    print("\nYour order summary:")
    print(f"Size: {order['size']}")
    print("Toppings:")
    for topping in order['toppings']:
        print(f"- {topping}")

if __name__ == "__main__":
    main()