# inheritance


class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
        print("Person Created.")

    def whoami(self):
        print("I am a Person.")


class Student(Person):
    def __init__(self, fname, lname, number):
        Person.__init__(self, fname, lname)

        self.StundentNumber = number
        print("Student Created.")

    # override
    def whoami(self):
        print("I am a Student")


class Teacher(Person):
    def __init__(self, fname, lname, branch):
        super().__init__(fname, lname)
        self.branch = branch

    def whoami(self):
        print(f"I am a {self.branch} teacher.")


p1 = Person("Asya", "Kaya")
s1 = Student("Hazar", "Kaya", "1023")
t1 = Teacher("Cengiz", "Kaya", "Primary School")

print(p1.firstname + " " + p1.lastname)
print(s1.firstname + " " + s1.lastname + " " + s1.StundentNumber)
print(t1.firstname + " " + t1.lastname + " " + t1.branch)


p1.whoami()
s1.whoami()
t1.whoami()
