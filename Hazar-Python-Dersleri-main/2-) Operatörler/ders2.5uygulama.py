#girilen sayının 0-100 arasında olduğunu kontrol et .

sayi=int(input("sayi giriniz : "))

result=  sayi > 0 and sayi < 100


print(f"girdiginiz sayi '{sayi}' ve sayinin 0-100 araliginda olma durumu {result}.")



#girilen sayının pozitif çift sayı old. kontrol et

"""x=int(input("sayi girin : "))

result= (x > 0 and x%2 == 0)

print(f"girilen sayi {x} ve ve istenilen durumu karsilamasi {result}")"""

#kullanıcı adı ve parola bilgileri ile giriş kontrolü yapınız.
"""x="hazar"
y="14"

kadi=input("username : ")
sifre=input("password : ")

result=kadi==x
result2=sifre==y

print(f"username is : {result} password is : {result2}")"""



#girilen 3 sayıyı büyüklük olarak karşılaştırınız




#2 vize %60 ve 1 final notunu alıp ortalama hesaplayınız.

 # ortalama 50 olsa bile final notu en az 50 olmalıdır.
 # finalden 70 alındığında ortalamanın önemi olmasın.

"""x=int(input("1. : "))  
y=int(input("2. : "))  
z=int(input("3. : "))  


ortalama=(((x+y) /2 *0.6) + (z*0.4)) > 50 and z > 50   




result=(ortalama>=50) and z>=50

result=(ortalama>=50) or z>=70  



print(result)"""
  
  
   
  #kişinin kilo ve boy indekslerini alıp indeksi hesaplayın (kilo/boyun karesi)

  #0-20 zayıf
  #20-25 ort 
  #25+ şişman 
 
kilo=float(input("kilo : " ))
boy=float(input("boy : "))
hesap=(kilo/boy*2)

if  hesap < 20 :
    print("zayıf")

if 20<hesap<25 : 
    print("orta")

if 25<hesap:
    print("sisman")


 
