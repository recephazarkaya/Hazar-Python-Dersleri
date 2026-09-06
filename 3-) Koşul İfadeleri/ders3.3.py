# if = eğer 
# elif = değilse eğer
# else = hiçbiri değilse 
# anlamına gelir.




#girilen sayının 0-100 arasında olduğunu kontrol et .

"""sayi=float(input("sayi : "))
result=(sayi>0) and (sayi<=100)

if result==True : 

    print("girdiğiniz sayi 1 ile 100 arasindadir.")

else : 
    print("girdiğiniz sayi 1 ile 100 arasinda değil.")"""

"""#girilen sayının pozitif çift sayı old. kontrol et
sayi=float(input("sayi : "))
if sayi > 0 and sayi%2==0 : 
    print("girdiginiz sayi pozitif ve çift bir sayidir ")
elif sayi> 0 and not(sayi%2==0) : 
    print("girdiginiz sayi pozitif fakat cift bir sayi degil ") 
elif sayi <= 0 : 
    print("girdiginiz sayi pozitif degil")"""

#kullanıcı adı ve parola bilgileri ile giriş kontrolü yapınız.

"""kadi="hazar"
sifre="14"

username=input("kullanici adi : ")
password=input("sifre girin : ")

if kadi==username :
  if sifre==password :    
    print("kadi ve sifre dogru.")
  else:
    print("hatali sifre.") 


elif  sifre==password :
  print("kullanici adi yanlis.")

else:
  print("kadi ve sifre hatali.")
"""











#2 vize %60 ve 1 final notunu alıp ortalama hesaplayınız.
 # ortalama 50 olsa bile final notu en az 50 olmalıdır.
 # finalden 70 alındığında ortalamanın önemi olmasın.

"""vize1=int(input("1. : "))  
vize2=int(input("2. : "))  
final=int(input("3. : "))  


ortalama=(((vize1+vize2) /2 *0.6) + (final*0.4))

if final<50 : 
    print("final 50 nin altinda kaldi")
elif ortalama>=50 : 
    print("final ve ortalama 50 üstü gecti")

elif final>=70 : 
    print("final 70 in üstünde oldugu icin gecti")

else: 
    print("kaldi")   """ 




