

class Parent:
    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name

    def get_name(self) -> str:
        return f"{self.first_name} {self.last_name}"


class Child(Parent):
    def __init__(self, first_name: str, last_name: str):
        super().__init__(first_name, last_name)
        self.previous_last_names = []

    def change_last_name(self, last_name) -> None:
        self.previous_last_names.append(self.last_name)
        self.last_name = last_name

    def get_full_name(self) -> str:
        suffix = ""
        if len(self.previous_last_names) > 0:
            suffix = f" (née {self.previous_last_names[0]})"
        return f"{self.first_name} {self.last_name}{suffix}"
  
  

person1 = Child("Elizaveta", "Alekseeva")
# Predict: Creates a Child object. Works perfectly.

print(person1.get_name())
# Predict: it will print "Elizaveta Alekseeva" 
# Child inherits this method from Parent
 
print(person1.get_full_name())
#  Predict: it will print "Elizaveta Alekseeva" because the last name has not been changed yet.
# get_full_name is defined in Child, but it uses the last name from Parent, which is "Alekseeva" at this point.

person1.change_last_name("Tyurina")
#  Predict: Changes last_name to "Tyurina" and saves "Alekseeva" in the
# previous_last_names list. Works perfectly.

print(person1.get_name())
# Predict: Prints "Elizaveta Tyurina". 
# get_name is inherited from Parent, but it uses the updated last name "Tyurina".

print(person1.get_full_name())
# Predict: Prints "Elizaveta Tyurina (née Alekseeva)".
# get_full_name uses the updated last name "Tyurina" and also includes the previous last name "Alekseeva" in the output.
print()

person2 = Parent("Elizaveta", "Alekseeva")
# Predict: Creates a Parent object. Works perfectly.

print(person2.get_name())
# Predict: it will print "Elizaveta Alekseeva"
# get_name is defined in Parent, so it works perfectly.

print(person2.get_full_name())
# Predict: it will raise an AttributeError because get_full_name is not defined in Parent, 
# and Parent does not have access to the methods of Child.

person2.change_last_name("Tyurina")
# Predict: it will raise an AttributeError because change_last_name is not defined in Parent,
# and Parent does not have access to the methods of Child.

print(person2.get_name())
# Predict: it will print "Elizaveta Alekseeva" because the last name has not been changed due to the previous error.

print(person2.get_full_name())
# Predict: it will raise an AttributeError again for the same reason as before.
