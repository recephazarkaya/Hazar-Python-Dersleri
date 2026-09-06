def selamver():
     print("selam")


selamver()


a=int(input("karesi alinacak sayi : "))

b=int(input("10 ile carpilacak sayi : "))




def islem(): 
     print(a**2 , b*10)


islem()


x= int(input("dyili gir :"))

def yashesapla(yas) : 
  print(2026-yas)


yashesapla(x)  


# isimsiz fonksiyonlar (lambda)

kareal= lambda x : x*x


print(kareal(5))



# args(*)

def toplama(*sayilar):
     toplam = 0 
     for sayi in sayilar :
         toplam +=sayi
     return toplam

print(toplama(1,2,3,4,5,6,7,8)) 
print(toplama(14,28))
print(toplama(1903,2007,1999,1970,1973,14,2))

#  args işlemi fonksiyonda istediğimiz kadar sayıyı veya veriyi kullanmamızı sağlar. 
# yani fonksiyonun yapısını değiştirmeden sonsuz sayıda veriyi işleme sokabiliriz.