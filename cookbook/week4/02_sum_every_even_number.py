from random import randint

list_numbers = []

for i in range(1, 10000):
    list_numbers.append(str(randint(1, 1000)))

std_input = ','.join(list_numbers)
print(std_input)

numbers = std_input#input()
numbers = numbers.split(',')

sum_of_numbers = 0
for number in numbers:
    number = int(number)
    if number % 2 == 0:
        sum_of_numbers += number
print(sum_of_numbers)