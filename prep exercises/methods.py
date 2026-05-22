from datetime import date


class Person:
    def __init__(self, name: str, date_of_birth: date, preferred_operating_system: str, favorite_sport: str) -> None:
        self.name = name
        self.date_of_birth = date_of_birth
        self.preferred_operating_system = preferred_operating_system
        self.favorite_sport = favorite_sport

    def is_adult(self):
        today = date.today()
        age = today.year - self.date_of_birth.year

        birthday_passed = (
              (today.month, today.day) >= (self.date_of_birth.month, self.date_of_birth.day)
        )
        if not birthday_passed:
            age -= 1
        return age >= 18
        
        

beko = Person("Beko", date(2005, 2, 17), "Linux", "Football")
print(beko.is_adult())


# Advantages of methods over free functions:

# Keep data and behavior together: 
# A method belongs directly to an object. It combines the object's info (data) and actions (behavior) into one package

# Make code easier to read: 
# You call them using object.action(). This reads like a normal sentence, making the code self-explanatory.  
# same (imran.is_adult() is easier to understand than is_adult(imran))

# Support inheritance: 
# Child objects automatically get access to the parent's methods. This means you do not have to copy and paste code.

# Enable polymorphism: 
# Different objects can use the exact same method name but handle it in their own unique way 
# (like a Dog and a Cat both responding to a .makeSound() method)
