x = input("1.sayi: ")
y = input("2.sayi: ")
toplam = int(x) + int(y)

print(type(x))
print(type(y))
print("Toplam: ", toplam)


# inputtan gelen bir deger str olarak algınalır dolayısıla toplama islemi yaparken birlestirme islemi yapar.
# bunu engellemek icin int() veya float() fonksiyonu kullanılır.

# Type Conversion (Tip Dönüşümü)
# 1 int to float
"""x=float(x)
print(x)
print(type(x))"""

# float to int
"""y=int(y)
print(y)
print(type(y))"""

# bool to str
"""isOnline= True
print(isOnline)
print(type(isOnline))"""

# bool to int
"""isOnline= int(isOnline)
print(isOnline)
print(type(isOnline))"""
