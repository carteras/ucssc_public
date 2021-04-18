def fizz_buzz(number, a=3, b=5):
    if number % a == 0 and number % b == 0:
        return 'fizzbuzz'
    elif number % a == 0:
        return "fizz"
    elif number % b == 0:
        return "buzz"
    else: 
        return number

for i in range(1, 16):
    print(fizz_buzz(i))
    
