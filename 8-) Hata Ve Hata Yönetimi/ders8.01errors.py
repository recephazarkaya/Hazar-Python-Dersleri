# error
# print(a) -> NameError
#  int("1a2") -> ValueError
# print(10 / 0) -> ZeroDivisionError
# print("denem"e) -> SyntaxError
# https://docs.python.org/3/library/exceptions.html sayfasından bütün hata türlerine bak.

# error handling (hata yönetimi)

# try:
#     x = int(input("x : "))
#     y = int(input("y : "))
#     print(x / y)
# except ZeroDivisionError:
#     print("y için 0 girilemez.")
# except ValueError:
#     print("x ve y için sayisal değer girin.")
# try:
#     x = int(input("x : "))
#     y = int(input("y : "))
#     print(x / y)
# except (ZeroDivisionError, ValueError) as e:
#     print("hatali bilgi girildi.")
#     print(e)

while True:
    try:
        x = int(input("x : "))
        y = int(input("y : "))
        print(x / y)
    except (ZeroDivisionError, ValueError) as e:
        print("hatali bilgi girildi.", e)

    else:
        break
