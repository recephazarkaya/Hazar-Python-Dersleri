import random

# sayi = random.random()  #Varsayilan değer aralığı "0.0 - 1.0" dir
# sayi = random.random() *100 #çıkan değerler 100 ile çarpılır.
# sayi = random.uniform(1, 10)  # metodu ile istediğimiz aralığı oluşturabiliriz.
sayi = random.randint(1, 10)  # metodu ile sayılar ondalıklı olarak çıkar

names = ["asya", "hazar", "elvan", "cengiz", "recep", "türkan"]
result = names[random.randint(0, len(names) - 1)]


# liste = list(range(10))

# random.shuffle(liste) #listenin içindeki elemanların sırasını karıştırır.

liste = list(range(100))

x = random.sample(liste, 5)  # liste içersinden 5 tane rastgele eleman alır.

print(x)

# print(liste)

print(result)


# print(sayi)
