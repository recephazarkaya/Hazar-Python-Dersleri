sayi=int(input("Sayi Giriniz : "))

if sayi==1 : 
    asalmi=False
    
    
    print(f"{sayi} asal değildir.")

for i in range (2,sayi) : 
    if (sayi % i == 0) :
        asalmi=False
        break
if asalmi :  
      print(f"{sayi} asal bir sayıdır.")

else:
        print(f"{sayi} asal değildir.")