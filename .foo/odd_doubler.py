count = 0
for i in range(1, 1000):
    if i % 2 == 0 and i % 10 != 0: 
        if i/2 % 2 != 0:
            count+=1
            print(f'    {i}/2={i/2}')

print(count)