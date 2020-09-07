from datetime import date


class Person:
    def __init__(self, name, height, birthdate):
        self._name = name
        self._height = height
        self._birthdate = birthdate

    def get_name(self):
        return str(self._name)

    def get_height(self):
        return int(self._height)

    def get_age(self):
        today = date.today()
        person_age = (today.year - self._birthdate.year)
        if today.month < self._birthdate.month or today.day < self._birthdate.day:
            person_age -= 1
        return int(person_age)

    def get_description(self):
        return f"{self._name} is {self._height} cm high and is {Person.get_age(self)} years old."


my_person = Person('Michael', 190, birthdate=date(1976, 8, 1))

print(my_person.get_description())
