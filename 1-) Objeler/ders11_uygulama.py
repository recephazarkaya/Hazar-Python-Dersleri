names=["elvan","cengiz","asya","hazar"]
years=[1973,1970,1999,2007]

#recep ismini listenin sonuna ekle
"""names.append("recep")"""

#türkan ismini listenin başına ekle
"""names.insert(0,"türkan")"""

#hazar ismini listeden sil
"""names.remove("hazar")"""

#hazar listenin kaçıncı indeksi ? 
"""print(names.index("hazar"))"""

#years elemanlarını ters çevir
"""years.reverse()
print(years)"""

#names elemanlarını alfabetik olarak sırala
"""names.sort()
print(names)"""

#years listesini rakamsal büyüklüğe göre sırala
"""years.sort()
print(years)"""

#str = "merhaba,nasilsin " karakter dizisini listeye çevir. ?

"""list=["merhaba","nasilsin"]
print(list)"""

#years dizisinin en büyük ve en küçük elemanı nedir ? 
"""valmin=min(years)
valmax=max(years)
print(valmin,valmax)"""

#years dizisinde kaç tane 1999 değeri vardır ? 
"""sayi=years.count(1999)
print(sayi)"""
#years dizisinin tüm elemanlarını sil 
"""years.clear()
print(years)"""

#kullanıcıdan alacağın 3 tane marka bilgisini bir listede sakla --->EN ÖNEMLİSİ 

marka1= input("1.marka : ")
marka2= input("2.marka : ")
marka3= input("3.marka : ")

mylist=[marka1,marka2,marka3]

print(mylist)

#print(names)
#print(years)