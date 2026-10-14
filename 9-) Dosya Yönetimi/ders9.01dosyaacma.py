# Dosya açmak ve oluşturmak için open() fonksiyonu kullanılır.
# Kullanım : open(dosya_adi,dosya_erisme_modu) şeklindedir.
# Dosya Erişme Modu => dosyayı hangi amaçla açtığımızı belirler.
# "w" : (Write) yazma,
#  **dosyayı konumda oluşturur.
#  **dosya içeriğini siler ve yeniden ekleme yapar.


# file = open("newfile.txt", "w")
# file.close()

# file = open("newfile.txt", "w", encoding="utf-8")
# file.write("Hazar ıüğş")
# file.close


# "a" : (Append) ekleme, dosya konumda yoksa oluşturur.
# file = open("newfile.txt", "a", encoding="utf-8")
# file.write("\n asya kaya işğü")
# file.close()


# "x" : (Create) oluşturma, dosya zaten varsa hata verir.

file = open("newfile2.txt", "x", encoding="utf-8")

# "r" : (Read) okuma, varsayılan dosya konumda yoksa hata verir.
