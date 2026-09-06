# Gönderilen bir kelimeyi belirtilen kez ekranda gösteren bir fonksiyon yazın.
"""def yazdir(kelime,adet) : 
    print(kelime * adet)

yazdir("hazar " , 10)
yazdir("asya\n" , 5)"""

# Kendine gönderilen sınırsız sayıdaki parametreyi bir listeye çeviren fonksiyon yazınız.
"""def Listeyecevir(*params) : 
    liste = []
    
    
    for param in params: 
        liste.append(param)

    return liste
result = Listeyecevir(14,28,"hazar","asya")

print(result)"""


# Gönderilen 2 sayı arasındaki asal sayıları bulacak bir fonksiyon yazınız



"""def asalbul(sayi1,sayi2):
    for sayi in range(sayi1,sayi2+1) : 
        if sayi > 1 :
            for i in range (2 , sayi):
                 if (sayi % i == 0) :
                     break 
            else: 
                 print(sayi)  
     
sayi1 = int(input("sayi 1 : "))
sayi2 = int(input("sayi 2 : "))

asalbul(sayi1,sayi2)"""


# kendisine gönderilen bir sayıyın tam bölenlerini bir liste şekline dönüştürecek fonksiyonu yazınız.

"""def tambolenbul(sayi) : 
    tambolenler=[]

    for i in range(2,sayi) : 
      if (sayi % i == 0 ) : 
       tambolenler.append(i)
    return tambolenler
print(tambolenbul(14))"""
