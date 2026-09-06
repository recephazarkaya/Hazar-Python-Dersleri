# # class
# class Person :
#     # class isimleri genellikle  harfle başlatılır.


#     # class attributes
#     adress="no information"


#     # contrucator (yapıcı metod)
#     def  __init__(self, name, year ):


#     # object attributes
#       self.name = name
#       self.year = year


#     #  istance methods

#     def intro(self):
#        print("Hello There. I am " + self.name)

#     def calculateAge(self):
#        return 2026 - self.year


# # ocject(instance)
#      # objeler genellikle KÜÇÜK harfle başlatılır.

# p1 = Person(name="hazar" ,year= 2007)
# p2 = Person(name="asya" ,year= 1999)

# p1.intro()
# p2.intro()

# print(p1.calculateAge())
# print(p2.calculateAge())


class Circle:
    # Class object attribute
    pi = 3.14

    def __init__(self, yaricap=1):
        self.yaricap = yaricap

    # Methods
    def cevre_hesapla(self):
        return 2 * self.yaricap * self.pi

    def alanhesapla(self):
        return self.pi * (self.yaricap**2)


c1 = Circle()  # yaricap = 1
c2 = Circle(5)


print(f"c1 : alan = {c1.alanhesapla()} , cevre = {c1.cevre_hesapla()}")
print(f"c2 : alan = {c2.alanhesapla()} , cevre = {c2.cevre_hesapla()}")
