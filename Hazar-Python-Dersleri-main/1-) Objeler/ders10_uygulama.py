#Bmw,Mercedes Opel,Mazda" elemanlarına sahip bir liste oluşturunuz
mylist= ["Bmw","Mercedes","Opel","Mazda" ,"Nissan"]

#liste kaç elemanlıdır? 
print(len(mylist))

#listenin ilk ve son elemanı nedir ? 
"""ilkeleman= mylist[0]
soneleman= mylist[-1]
print(ilkeleman, soneleman)"""

#mazda değerini toyota ile değiştirin 
""" mylist[3] ="Toyota" """


#mercedes listenin bir elemanı mıdır ? 

"""isFound= "Mercedes" in mylist 
print(isFound) """


#listenin -2 indeksindeki değeri nedir ? 
"""print(mylist[-2])"""

#listenin son 2 elemanı yerine "toyota" ve " renault" değerlerini ekleyin 
"""mylist[-1]= "Toyota" 
mylist[-2] = "Renault"
print(mylist)"""

#Listenin üzerine "audi" ve "nissan" değerlerini ekleyin 
  # .append -> listenin en sonuna ekleme yapar
  # .insert(x,y) ->listenin x. indeksine y elemanını ekler
  #.extend -> başka bir listeyi ekler.

"""mylist2= ["Audi", "Nissan"]
mylist.extend(mylist2)
print(mylist)"""


#listenin son elemanını silin 

"""mylist.pop()     -> son elemani siler 
print(mylist)"""

#liste elemanlarını tersten yazdırın 

"""tersmylist= mylist[::-1]
print(tersmylist)"""

#aşağıdaki verileri bir liste içinde saklayınız ve liste elemanlarını ekrana yansıtınız
"""studentA = ("cengiz kaya", 1970, 70,60,70)
studentB = ("hazar kaya" ,2007 , 80,80,70)
studentC = ("asya kaya" ,1999  , 80,70,90)

students=[studentA,studentB,studentC]
print(students)"""

#print(mylist)