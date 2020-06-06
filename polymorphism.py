class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)


class Student(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)

    def printname(self):
        print(self.firstname)


def main():

    x = Person("John", "Doe")
    x.printname()

    y = Student("Mike", "Olsen")
    y.printname()


if __name__ == '__main__':
    main()
