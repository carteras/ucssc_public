class Animal:
    def __init__(self, name: str, db = AnimalDB()):
        self.name = name
        self.db = db
    
    def get_name(self) -> str:
        return self.name

    

class AnimalDB:
    def get_animal(self, id) -> Animal:
        pass
    def save(self, animal: Animal):
        pass

animal = Animal("bobcat")

print(animal.get_name())