from random import randint

numbers = []
count = 0
while count < 10:
    numbers.append(randint(1, 1_000_000))
    count += 1

biggest_number_so_far = -1
for number in numbers:
    if number > biggest_number_so_far:
        biggest_number_so_far = number
print(biggest_number_so_far)
