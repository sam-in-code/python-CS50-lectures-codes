def main():
    m = input("Mass (in kg): ")
    equation(m)

def equation(x):
    c = 3 * 10**8
    e = int(x) * c**2
    print("Energy (in Joules): ", e)
main()        