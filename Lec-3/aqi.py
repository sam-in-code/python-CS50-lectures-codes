x = int(input("Enter AQI: "))
if x <= 100:
    print("Safe to breathe")
elif x > 100 and x < 200:
    print("Go outside with mask")
else:
    print("Don't go outside")

