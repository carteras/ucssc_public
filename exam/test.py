numbers = list(range(1, 10))
out = ''
for number in numbers:
    out += str(number)+','
out = out[:-1]
print(out)