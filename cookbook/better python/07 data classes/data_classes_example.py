from dataclasses import dataclass, field

@dataclass(order=True)
class Person:
    sort_index: int = field(init=False, repr=False)
    name: str
    job: str
    age: int
def __post_init__(self):
    self.sort_index = self.age


person1 = Person('Geralt', 'Witcher', 30)
person2 = Person('Yennefer', 'Sorceress', 25)
person3 = Person('Yennefer', 'Sorceress', 25)

print(id(person2))
print(id(person3))
print(person1)

print(person3 == person2)
print(person1 > person2)