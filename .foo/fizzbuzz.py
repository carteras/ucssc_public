print(
    *(
        not (r:='') 
        and (n % 3 or (r:='Fizz')) 
        and (n % 5 or (r:=f'{r}Buzz')) 
        and (r or n) 
        for n 
        in range(1, 101)
    ), 
    sep='\n'
)