people = [
    {"name": "Harry", "House": "gryffindor"},
    {"name": "Cho", "House": "Ravenclaw"},
    {"name": "Draco", "House": "Slytherine"}
]

def f(person):
    return person["house"]
    ''
people.sort(key=lambda person: person["name"])
print(people)