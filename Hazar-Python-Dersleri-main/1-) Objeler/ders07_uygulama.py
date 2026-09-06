

website = "https://www.recephazarkaya.com.tr"
course= "https://www.btkakademi.gov.tr/portal/course/player/deliver/sifirdan-ileri-seviye-python-programlama-5877"

length= len(website)


# course karakter dizisinde kaç karakter bulunmaktadır ? 
"""result = len(course)
  print(result)"""

#website içinden www karakterlerini alın
"""print(website[8:11])"""

#website içinden com karakterlerini alın
"""print(len(website)) => kaç karakter olduğunu öğrendik 
print=(website[27:30]) veya result=website[27:30]
result = website[length-3:length] => alternatif
"""
#course içinden ilk15 ve son 15 karakteri yazdırın
"""print(course[:15]) 
print(course[88:104])"""

#course ifadesindeki karakterleri tersten yazdırın
"""print(course[::-1]) """



name,surname,age,job = "Hazar", "Kaya", 19 , "Student"
#yukarıda verilen değişkenler ile ekrana aşağıdaki ifadeyi yazdırın 
#"Benim adım hazar kaya yaşım 19 ve mesleğim öğrenci"
"""print(f"My name is {name} {surname} I am {age} years old and My job is {job}" )"""


#"Hello world" ifadesindeki w harfini W ile değiştirin 

"""s="Hello world"
 

s=s[0:6] + "W" +s[-4:]"""

#"abc" ifadesini yan yana 3 kez yazdırın.
"""x= "abc"
print(x,x,x)
"abc"*3
"""

"""print(s)"""