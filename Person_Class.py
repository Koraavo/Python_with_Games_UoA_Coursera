from datetime import date

class Person:
    pass


def main():
    person1 = create_person('Michael', 190, birthdate=date(1976, 3, 1))
    description = get_description(person1)
    print(description)

def get_description(person):
    age = get_age(person)
    return (f"{person.name} is {person.height} cm high and is {age} years old.")


def get_age(person):
    # Return the age of the person in years.
    today = date.today()
    person_age = (today.year - person.birthdate.year)
    if today.month < person.birthdate.month or today.day < person.birthdate.day:
        person_age -= 1
    return person_age


def create_person(name, height, birthdate):
    # Return a a new person object with the given
    # name, height and birthdate.
    # - name is a str
    # - height is an int object in centimetres
    # - birthdate is a date object from the
    # module datetime
    person = Person()
    person.name = name
    person.height = height
    person.birthdate = birthdate
    return person

main()
