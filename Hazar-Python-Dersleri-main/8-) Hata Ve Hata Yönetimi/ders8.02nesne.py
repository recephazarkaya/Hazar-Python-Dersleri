# x = int(input("x :"))


# if x > 5:
#     raise Exception("x 5 den büyük değer alamaz.")


# def check_password(psw):
#     import re

#     if len(psw) < 8:
#         raise Exception("parola en az 8 karakter içermelidir. ")
#     elif not re.search("[a-z]", psw):
#         raise Exception("parola en az 1 küçük harf içermelidir")

#     elif not re.search("[A-Z]", psw):
#         raise Exception("parola en az 1 büyük harf içermelidir")

#     elif not re.search("[0-9],psw"):
#         raise Exception ("parola sayı içermelidir.")


class Person:
    def __init__(self, name, year):
        if len(name) > 10:
            raise Exception("name alanı fazla karakter içeriyor")
        else:
            self.name = name


p = Person("Hazarrrrrrrrrrrrrrrrrr", 2007)
