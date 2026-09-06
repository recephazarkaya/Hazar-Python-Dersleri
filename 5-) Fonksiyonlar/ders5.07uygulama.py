hesap1= {
    "ad" : "hazar kaya" ,
    "hesapno" : "140207",
    "bakiye" : 14000,
    "ekhesap" : 10000,
    }

hesap2={
    "ad" : "asya kaya",
    "hesapno" :"190999",
    "bakiye" : 27000,
    "ekhesap" : 20000,
}

def paracek(hesap,miktar) :
    print(f"Merhaba {hesap["ad"]}")
    
    if hesap["bakiye"] >= miktar : 
      hesap["bakiye"]-=miktar
      print("Paranizi alabilirsiniz.")
      bakiyesorgula(hesap) 
    else :
        toplam =    hesap["bakiye"] + hesap["ekhesap"] 

        if (toplam >=miktar) : 
           ekhesapkullanimi= input("ek hesap kullanilsin mi ? (e/h) : ")
           if ekhesapkullanimi == "e" : 
              ekhesapkullanilacakmiktar= (miktar - hesap["bakiye"])
              hesap["bakiye"] = 0
              hesap["ekhesap"] -=ekhesapkullanilacakmiktar
              print("paranizi ek hesabinizi kullanarak alabilirsiniz.")
              bakiyesorgula(hesap)
           else : 
              print(f"{hesap["hesapno"]} nolu hesabinizda {hesap["bakiye"]},ek hesabinizda ise {hesap["ekhesap"]} tl  bulunmaktadir.")
        else : 
           print("Bakiye yetersiz.")  
           bakiyesorgula(hesap)



def bakiyesorgula(hesap) : 
   print(f"{hesap["hesapno"]}lu hesabinizda {hesap["bakiye"]} ve ek hesabinizda {hesap["ekhesap"]}tl bulunmaktadir. ")

paracek(hesap1,1000)



