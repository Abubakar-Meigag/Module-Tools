


class Person:
    def __init__(self, name: str, age: int, preferred_operating_system: str, favorite_sport: str) -> None:
        self.name = name
        self.age = age
        self.preferred_operating_system = preferred_operating_system
        self.favorite_sport = favorite_sport

    def is_adult(self) -> bool:
          return self.age >= 18
        
    def get_favorite_sport(self) -> str:
          return self.favorite_sport
        
        

imran = Person("Imran", 22, "Ubuntu", "Football")
print(imran.name)
print(imran.is_adult())
print(imran.preferred_operating_system)
print(imran.get_favorite_sport())

eliza = Person("Eliza", 34, "Arch Linux", "Tennis")
print(eliza.name)
print(eliza.is_adult())
print(eliza.preferred_operating_system)
print(eliza.get_favorite_sport())