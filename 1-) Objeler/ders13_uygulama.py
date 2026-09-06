ogrenciler={}
number=input("ogrencino:")
name=input("ad : ")
surname=input("soyad : ")
phone=input("telefon : ")

ogrenciler[number] ={
    "ad" : name,
    "soyad" : surname,
    "telefon" : phone 

}
ogrenciler.update({
    number : {
        "ad" : name,
        "soyad" : surname,
        "telefon" : phone
    }
})

number=input("ogrencino:")
name=input("ad : ")
surname=input("soyad : ")
phone=input("telefon : ")



number=input("ogrencino:")
name=input("ad : ")
surname=input("soyad : ")
phone=input("telefon : ")

print(ogrenciler)

ogrNo=input("Öğrenci no : " )
ogrenci=ogrenciler[ogrNo]
print(ogrenci)
    
