# method 

list = [1,2,3,4]

list.append (5)

print(type(list))
 
myString = "hello"

print(myString.upper())

print(list)



#  fonksiyon 

def sayHello(name= "user"): 
     print("hello "+ name)

sayHello("hazar")
sayHello("asya") 
sayHello()   


def sayHello(name= "user"): 
    return "hello "+ name

msg= sayHello("recep")
msg= sayHello("türkan")

print(msg)
           # bu tarz sıralı durumlarda dosyaya en son atanan değer olduğu için çıktıda sadece türkan görünür.

def total(x,y) : 
     return x + y 

result = total (14,37)

print(result)


def yashesapla(dogumyili) : 
    return 2026 - dogumyili 

agehazar = yashesapla(2007)
ageasya= yashesapla(1999)
agecengiz = yashesapla(1970)
ageelvan = yashesapla(1973)
print(agehazar,ageasya,ageelvan,agecengiz)

def emeklilik(dogumyili, isim) : 
    """
    DOCSTRING : dogum yiliniza gore emeklilige kac yil kaldi.
    INPUT :  dogum yili.
    OUTPUT : hesaplanan yil bilgisi.
    
    """
    yas = yashesapla(dogumyili)
    emeklilik = 65 - yas

    if emeklilik > 0 :
        print(f"emeklilige {emeklilik} yil kaldi.")
    else : 
        print("zaten emeklisiniz.")    

emeklilik(1983,"ali")
print(help(emeklilik))