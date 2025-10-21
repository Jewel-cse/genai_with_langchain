from typing import TypedDict

class Person(TypedDict):

    name: str
    age: int

new_person: Person = {'name':'Jewel', 'age':'26'}

print(new_person)