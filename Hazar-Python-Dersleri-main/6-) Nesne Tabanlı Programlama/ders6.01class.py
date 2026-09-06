# class
class Person:
    # class isimleri genellikle  harfle başlatılır.

    # class attributes
    adress = "no information"

    # contrucator (yapıcı metod)
    def __init__(self, name, year):

        # object attributes
        self.name = name
        self.year = year
        print("init metodu calisti.")

    # methods


# ocject(instance)
# objeler genellikle KÜÇÜK harfle başlatılır.

p1 = Person(name="hazar", year=2007)
p2 = Person(name="asya", year=1999)

# updating
p1.name = "recep"
p1.adress = "kastamonu"


# accessşng object attributes
print(f"p1 : name : {p1.name}, year : {p1.year}, adress= {p1.adress} ")
print(f"p2 : name : {p2.name}, year : {p2.year}, adress= {p2.adress} ")


# print(type(p1))
# print(type(p2))
