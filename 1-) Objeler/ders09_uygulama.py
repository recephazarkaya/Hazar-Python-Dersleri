website="www.recephazarkaya.com"
course ="PYTHON DERSLERİ RECEP HAZAR KAYA 14 GÜNDE"

#" Hello World " başındaki ve sonundaki boşlukları sil
"""message=" Hello World " 
message= message.strip()"""

#www.recephazarkaya.com içinden sadece recephazarkaya kalsın 
"""website=website.strip("w.com")
print(website)"""

#course nin bütün harflerini küçük yap 
"""course = course.lower()
print(course)"""

#website içinde kaç tane a var ? (count("a"))
"""print(website.count("a"))"""


#website www ile başlayıp bitiyor mu ? 
"""isFound=website.startswith("www")
print(isFound)"""

#website içinde com ifadesi var mı ? 
"""index = website.find("com")
print(index) """


#course içindeki karakterlerin hepsi alfabetik mi ? (isalpha, isdigit)
"""result = course.isalpha()
print(result)"""

#website ifadesini satırda 50 karakter içine yerleştirip sağına ve soluna "*" ekle 
"""website=website.center(50,"*")
print(website)"""

#course karakter dizisindeki tüm boşlukları "-" ile değiştirin 
"""course=course.replace(" " , "-")
print(course)"""
#"Hello World" karakter dizisinin "world" ifadesini "There" olarak değiştir 
"""message="Hello World"
message= message.replace("World" , "There")
print(message)"""
#"course" karakter dizisini boşluk karakterlerinden ayır.
"""course=course.split(" ")
print(course)"""

#print()