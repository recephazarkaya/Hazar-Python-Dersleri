# NOT : BU PROBLEMLERİ İLERİDE ÖĞRENECEĞİN (İF , ELSE) GİBİ KOŞUL İFADELERİ İLE DAHA KISA VE KOLAY ŞEKİLDE ÇÖZECEKSİN.

#girilen 2 sayıdan hangisi büyüktür
"""
a=int(input("a : "))
b=int(input("b : "))

result= (a > b)

print(f"a: {a} b: {b} den büyüktür : {result}") 

"""
# kullanıcıdan 2 vize(%60) ve 1 final (%40) notunu alıp ortalama hesaplayınız.
   # eğer ortalama 50 ve üzerindeyse geçti değilse kaldı yazdırın.
"""vize1= float(input("1. vize : "))
vize2= float(input("2. vize : "))
final= float(input("final : "))
ortalama = (((vize1+vize2) / 2) * 0.6) + ((final) * 0.4)

print(f"not ortalamasniz : {ortalama} ve dersten geçme durumunuz {ortalama>=50} ")"""


# girilen bir sayının tek mi çift mi olduğunu yazdırın.
"""sayi=int(input("sayi : "))
tekcift = sayi % 2 == 0

print(f"girdiginiz sayi : {sayi} ve sayinin cift olma durumu : {tekcift} ")"""

#girilen sayinin pozitif mi negatif mi olduğunu yazdırın.
"""sayi=int(input("sayi : "))

sayidurumu= sayi >= 0

print(f"girdiginiz sayi : {sayi} ve sayinin pozitiflik durumu {sayidurumu}.")"""

#kullanici adi ve sifre bilgisi isteyip dogruluğunu kontrol edin 
  #(kullanici adi  : Hazar14 , sifre : 1402 )

kullaniciad = "Hazar14" 
sifre= "1402"

kadi=input("kullanici adini girin : ")
password= input("sifre girin : ")

result=kadi==kullaniciad
result=sifre==password

print(result)