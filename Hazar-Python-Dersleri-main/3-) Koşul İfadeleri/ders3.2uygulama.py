#isim yaş ve eğitim bilgilerini isteyip ehliyet alabilme durumunu kontrol edin 
"""name=input("isim : ")
age=float(input("yas : "))
egitim=input("edu : ")

if age >=18 :
 if egitim == "lise" or egitim == "üniversite":
    
    print("Ehliyet Alabilirsiniz")
     
else: 
    print("Ehliyet Alamazsiniz") """

# yazılı  notunu alıp  not bilgisini yazın 
 # < 24 =0
 #25-44 1
 #45 54 2 
 # 55 69 3 
 # 70 84 4 
 # 85 100 5

yazilinotu = float(input("notu girin : "))


if 0<= yazilinotu<24 : 
    print("0")
elif 25<= yazilinotu <=44 :
    print("1")
elif 45<= yazilinotu <=54 :
    print("2")    
elif 55<= yazilinotu <=69 :
    print("3")
elif 70<= yazilinotu <=84 :
    print("4")
elif 85<= yazilinotu <=100 :
    print("5")    
else : 
    print("hatali not girdiniz")
    




#trafik tarihi alınan bir aracın servis zamanını hesaplayın 
# 1. bakım 1. yıl 
# 2. bakım 2. yıl
# 3.bakım 3. yıl   
#** süre hesabını alınan gün ay yıl bilgisine göre gün bazlı hesaplayın 
#***datetime kullan.










#AYI GİBİ ÖNELİ NOT 
 #: import dediğimizde başka bir dosyadaki hazır kodları kendi sayfana çağırırsın dev bir alet çantası gibi düşün 
 #import datetime dediğimizde 
 #   date	Sadece tarihle ilgilenir.	2026-02-07
#  time 	Sadece saatle ilgilenir.	16:10:00
#  datetime  	Hem tarih hem saatle ilgilenir.	2026-02-07 16:10:00
#  timedelta 	İki zaman arasındaki farkı (süre) tutar.	5 gün, 3 saat









