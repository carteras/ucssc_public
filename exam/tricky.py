def change(i = 1, j = 2):
    i = i + j
    j = j + 1
    return f"{i} {j}"

print(change(j = 1, i = 2))

numbers = list(range(1, 10))
out =''
for number in numbers: 
    out += f'{number},'
out = out[:-1]
print(out)