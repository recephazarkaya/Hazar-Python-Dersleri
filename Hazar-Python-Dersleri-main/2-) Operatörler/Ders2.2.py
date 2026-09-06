x,y,z= 2,5,107
numbers = 1,5,7,10,6
toplam=(x+y+z)
#kullanıcıdan aldığınız 2 sayının çarpımı ile x,y,z toplamının farkı nedir 
"""
plus=x+y+z

sayi1=input("1. sayiyi giriniz : ")

sayi2 =input("2.sayiyi giriniz : ")

print(int(sayi1)*int(sayi2)-int(plus))

"""
# y nin x e kalansız bölümünü hesapla 
"""print(y//x)"""

# (x,y,z) toplamının mod 3 ü nedir ? 
"""print(toplam%3)"""

#y nin x. kuvvetini hesaplayınız
"""print(y**x)"""

#x,y*,z = numbers işlemine göre z nin küpü kaçtır ? 
   #normalde x,y,z = numbers dediğimizde kodumuz çalışmaz çünkü numbers kümesindeki 5 elemanı 3 elemana vermeye çalışıyoruz 
    # ama y yerine (*y) ifadesini kullandığımızda x en baştaki , z en sondaki, ve (*y) ise ortada kalan bütün elemanları alır. ve kodumuz çalışır.
"""x,*y,z = numbers
print(z**3)"""

#x,y*,z = numbers işlemine göre y nin değerleri toplamı kaçtır ? 

"""x,*y,z = numbers
print()

result= y[0]+y[1]+y[2]

print(result)"""
