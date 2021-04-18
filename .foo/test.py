def is_same_num(a, b):
    a = int(a)
    b = int(b)
    return a == b

# print(is_same_num(input(), input()))
# print(is_same_num(input(), input()))

def AND(a, b):
    if a == 1 and b == 1:
        return 1
    return 0
def OR(a, b):
    if a == 1 or b == 1:
        return 1
    return 0
def NOT(a):
    if a == 1:
        return 0
print(OR(1, 1))
print(OR(1, 0))
print(OR(0, 1))
print(OR(0, 0))