class Person:

    def __init__(self, name, surname, phone_number, date_of_birth):
        self.name = name
        self.surname = surname
        self.phone_number = phone_number
        self.date_of_birth = date_of_birth

    def __str__(self):
        return f"{self.__name} {self.__surname} {self.__phone_number} {self.__date_of_birth}"

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, surname: str):
        self.__surname = surname

    @property
    def phone_number(self):
        return self.__phone_number

    @phone_number.setter
    def phone_number(self, phone_number: int):
        if not isinstance(phone_number, int):
            raise TypeError("phone number must be integer value")
        self.__phone_number = phone_number

    @property
    def date_of_birth(self):
        return self.__date_of_birth

    @date_of_birth.setter
    def date_of_birth(self, date_of_birth: str):
        self.__date_of_birth = date_of_birth


class Notebook:

    def __init__(self):
        self.notes = []

    @staticmethod
    def print_notes(notes: list):
        printed_notes = list(map(lambda person: f"{person.name} {person.surname}, {person.phone_number}, "
                                                f"{person.date_of_birth}", notes))
        return f"{printed_notes}"

    def __str__(self):
        notes = self.print_notes(self.notes)
        return f"{notes}"

    def __add__(self, other):
        if not isinstance(other, Person):
            raise TypeError(f"Unsupported operand type for {type(self.__name__)} and {type(other.__name__)}")
        if any(other == obj for obj in self.notes):
            raise ValueError("Such person already exists in the notebook")
        self.notes.append(other)

    def __sub__(self, other):
        if not isinstance(other, Person):
            raise TypeError(f"Unsupported operand type for {type(self.__name__)} and {type(other.__name__)}")
        if not any(other == obj for obj in self.notes):
            raise ValueError("There is not such person in notebook")
        self.notes.remove(other)

    def __mul__(self, other):
        if not isinstance(other, Person):
            raise TypeError(f"Unsupported operand type for {type(self.__name__)} and {type(other.__name__)}")
        if not any(other == obj for obj in self.notes):
            return self.notes
        found_notes = self.notes
        for prop in other.__dict__:
            found_notes = list(filter(lambda obj: obj.__dict__[prop] == other.__dict__[prop], self.notes))
        notes_to_print = self.print_notes(found_notes)

        return notes_to_print


person1 = Person('John', 'Sims', 123, '20.11.2000')
person2 = Person('Jessi', 'Sims', 234, '20.11.2000')
person3 = Person('Mark', 'Berk', 546, '25.11.2000')
notebook = Notebook()
notebook + person1
notebook + person2
notebook + person3
print(notebook)
print(notebook * person1)
