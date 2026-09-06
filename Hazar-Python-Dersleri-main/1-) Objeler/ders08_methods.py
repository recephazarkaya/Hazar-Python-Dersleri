message = "Hello There. My name is Hazar Kaya"

#message= message.upper()
#upper etiketi bütün harflerin büyük harf ile yazılmasını sağlar.

#message =message.lower()
#lower etiketi bütün harflerin küçük harf ile yazılmasını sağlar.

#message= message.title()
#title etiketi sadece kelimelerin baş harflerinin büyük yazılmasını sağlar.

#message = message.capitalize()
#capitalize etiketi sadece cümlenin ilk harfini büyük yapar.

#message = message.strip()
#strip etiketi cümleden istediğimiz karakterleri siler.

#message = message.split()
#split etiketi cümledeki bütün kelimeleri ayırır.

#message=" ".join(message)
#join etiketi split ile ayrılan kelimelerin geri birleştirilmesini sağlar

#index = message.find("Hazar")
#print(index)
#verilen string içerisinde istediğimiz elemanı bulmamızı ve kaçıncı indexden başladığını gösterir.


#isFound= message.startswith("H")
#print(isFound)
#startswith etiketi girilen harf ile başlayan bir cümle olup olmadığını gösterir.

#isFound=message.endswith("a")
#print(isFound)
#endswith etiketi girilen harf ile BİTEN bir cümle olup olmadığını gösterir.

#message=message.replace("Hazar","Asya" )
#replace etiketi girilen kelime ile istenilen kelimeyi değiştirmeyi sağlar.

message=message.center(50)








print(message)