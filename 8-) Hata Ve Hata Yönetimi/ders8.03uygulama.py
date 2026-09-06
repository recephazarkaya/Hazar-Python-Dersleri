liste = ["1", "2", "7a", "14b", "hzr", "10", "50"]

# 1 : Liste elemanı içindeki sayısal değerleri bulunuz.

"""for x in liste:
    try:
        result = int(x)
        print(result)

    except: 
        continue"""

# 2 : kullanıcı "q" değerini girmedikçe aldığınız her inputun sayı olduğundan emin olunuz
# aksi halde hata mesajı yazın.
"""while True:
    sayi = input("sayi girin :")
    if sayi == "q":
        break
    try:
        result = float(sayi)
        print("girdiğiniz sayi :", result)
    except ValueError:
        print("geçersiz sayi")
        continue"""

# 3 : girilen parola içinde türkçe karakter hatası verin.

"""turke_karakterler = "sçğüöıİ"
def checkpassword(password):
    for i in password:
        if i in turke_karakterler:
            raise TypeError("türkçe karakter girilemez")

        else:
            pass
    print("parola oluşturuldu.")

password = input("parola : ")

try:
    checkpassword(password)
except TypeError as err:
    print(err)"""


# 4 : faktöriyel fonksiyonu oluşturup fonksiyona gelen değer için hata mesajları verin.
def faktoriyel(x):
    x = int(x)

    if x < 0:
        raise ValueError("negatif değer girilemez.")
    result = 1

    for i in range(1, x + 1):
        result *= i
    return result


for x in [5, 10, 20, -3, "10a"]:
    try:
        y = faktoriyel(x)
    except ValueError as err:
        print(err)
        continue
    print(y)
