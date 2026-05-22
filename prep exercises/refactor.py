from dataclasses import dataclass
from typing import List

@dataclass(frozen=True)
class Person:
    name: str
    age: int
    preferred_operating_system: str


@dataclass(frozen=True)
class Laptop:
    id: int
    manufacturer: str
    model: str
    screen_size_in_inches: float
    operating_system: str


def find_possible_laptops(laptops: List[Laptop], person: Person) -> List[Laptop]:
    possible_laptops = []
    for laptop in laptops:
        if laptop.operating_system == person.preferred_operating_system:
            possible_laptops.append(laptop)
    return possible_laptops


people = [
    Person(name="Imran", age=22, preferred_operating_system="Ubuntu"),
    Person(name="Eliza", age=34, preferred_operating_system="Arch Linux"),
    Person(name="Alice", age=28, preferred_operating_system="macOS"),
    Person(name="Beko", age=30, preferred_operating_system="Red Hat Linux"),
]

laptops = [
    Laptop(1, "Dell", "XPS", 13, "Arch Linux"),
    Laptop(2, "Dell", "XPS", 15, "Ubuntu"),
    Laptop(3, "Dell", "XPS", 15, "Red Hat Linux"),
    Laptop(4, "Apple", "macBook", 13, "macOS"),
]

for person in people:
    possible_laptops = find_possible_laptops(laptops, person)
    print(f"Possible laptops for {person.name}: {possible_laptops}")