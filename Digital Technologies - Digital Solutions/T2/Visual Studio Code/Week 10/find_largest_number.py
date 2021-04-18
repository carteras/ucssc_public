from random import randint

numbers = []
count = 0
while count < 10_000:
    numbers.append(randint(1, 1_000_000))
    count += 1

