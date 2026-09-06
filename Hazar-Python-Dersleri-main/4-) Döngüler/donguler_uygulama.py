import random

sayi = random.randint(1, 10)
# can = int(input("kaç can istersiniz ? : "))
hak = 5
sayac = 0

while hak > 0:
    hak -= 1
    sayac += 1
    tahmin = int(input("Write Your Guess : "))

    if sayi == tahmin:
        print(f"Congrats Thats True ! {sayac} and your point is : {100-((sayac-1)*20)} ")
        break

    if hak == 0:
        print(f"your right has finished the number is : {sayi} ")
        print("your point is 0 ")
        break

    elif sayi > tahmin:
        print("Up")

    else:
        print("Down")
