

from dataclasses import dataclass
from datetime import date

@dataclass(frozen=True)
class Person:
      name: str
      birth_day: date
      preferred_OS: str
      
      
      def is_adult(self):
            today = date.today()
            age = today.year - self.birth_day.year
            
            if (today.month, today.day) < (self.birth_day.month, self.birth_day.day):
                  age -= 1
            return age >= 18


beko = Person("Beko", date(2005, 2, 17), "Linux")
print(beko.is_adult())

noor = Person("Noor", date(2015, 2, 17), "Linux")
print(noor.is_adult())