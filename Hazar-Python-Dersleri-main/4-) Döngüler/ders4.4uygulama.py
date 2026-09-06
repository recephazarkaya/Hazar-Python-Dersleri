sayilar= [1,3,5,7,9,12,19,21]

#sayilar listesini while ile ekrana yazdırın.
# i=0 
# while (i<len(sayilar)) : 
#     print(sayilar[i])
#     i+=1



#başlangıç ve bitiş değerlerini kullanıcıdan alıp aradaki tüm tek sayıları ekrana yazdırın.

# baslangic = int(input("baslangic : "))
# bitis = int(input("bitis : "))
# i = baslangic
# while( i <= bitis) :    
#     if i%2 ==1 :   
#      print(i)
#     i += 1


#1-100 arasındaki sayıları azalan şekilde yazdırın.
# i=100
# while i >= 1 : 
#     print(i)
#     i -= 1




#kullanıcıdan alacağınız 5 sayıyı ekrana sıralı şekilde yazdırın.
# sayi1=int(input("1.sayi : "))
# sayi2=int(input("2.sayi : "))
# sayi3=int(input("3.sayi : "))
# sayi4=int(input("4.sayi : "))
# sayi5=int(input("5.sayi : "))

# x=[sayi1,sayi2,sayi3,sayi4,sayi5]

# x.sort()
# print(x)

#kullanıcıdan alacağınız sınırsız ürün bilgsini urunler listesi içinde saklayın 
   #ürün sayısını kullanıcıya sor 
   #dictionary listesi yapısı (name,price) şeklinde olsun 
   #ürün ekleme işlemi bittiğinde ürünleri ekranda while ile listeleyin.


# urunler=[]
# adet=int(input("urun sayisi giriniz : "))
# i=0
# while (i<adet) : 
#  name= input("urun ismi : ")
#  price=input("urun fiyati : ")
#  urunler.append({
#     "name" : name,
#     "price" : price,
#     })
 
#  for urun in urunler :
#   print(f"ürün adı : {urun["name"]} urun fiyati :{urun["price"]} ")