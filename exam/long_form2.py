year = int(input("Greetings! What is your year of origin? "))

if year <= 1900:
    print("Whoah, that's in the past!")
elif year > 1900 and year < 2020:
    print("that's totally in the present!")
else:
    print("Far out that's the future!!")