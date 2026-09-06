"""BU UYGULAMADA PYHTONDA ÖĞRENDİĞİM İLK 5 ÜNİTENİN BİR ÖDEVİ OLARAK BANKAMATİK UYGULAMASI YAPIYORUM."""

# Global değişkenler
kadi = ""
sifre = ""
eposta = ""
tlfno = ""
bakiye = 0


def kayitol():
    global kadi, sifre, eposta, tlfno, bakiye
    print("--- Hesap Olusturma Ekrani ---")
    kadi = input("Kullanici Adiniz : ")
    sifre = input("Sifre Belirleyin : ")
    eposta = input("E-Postanizi Girin : ")
    tlfno = input("Telefon Numaranizi Girin : ")
    bakiye = int(input("Baslangic Bakiyesi belirleyin : "))
    print("\nBasarili Bir Sekilde Kayit Oldunuz.")


def girisyap():
    while True:
        print("\n--- Giris Ekranina Hos Geldiniz. ---")
        username = input("Kullanici Adinizi Giriniz : ")
        password = input("Sifrenizi Giriniz : ")

        if username == kadi and password == sifre:
            print(f"Basarili Bir Sekilde Giris Yapildi. Sayin {kadi} Hos Geldiniz.")
            return True
        else:
            print("Kullanici Adi veya sifre hatali lütfen tekrar deneyin.")


def anaprogram():
    global bakiye  # Bakiyeyi güncelleyebilmek için global şart.

    kayitol()  # Önce kayıt oluyoruz

    if girisyap():  # Giriş başarılıysa döngüye giriyoruz
        while True:
            print("\n1- Bakiye Sorgula\n2- Para Yatirma\n3- Para Cekme\n4- Cikis Yap")
            secim = input("Islem Secin (1-4) : ")

            if secim == "4":  # Tırnak içinde yazdım çünkü input string gelir
                print("Cikis Yapildi.")
                break

            elif secim == "1":
                print(f"Mevcut Bakiyeniz: {bakiye} TL")

            elif secim == "2":
                yatirilacakmiktar = int(input("Yatirilacak Miktari Girin : "))
                bakiye += yatirilacakmiktar
                print(f"Islem basarili yeni bakiyeniz : {bakiye} TL")

            elif secim == "3":
                cekilecekmiktar = int(input("Cekmek istediginiz Miktari giriniz : "))
                if cekilecekmiktar <= bakiye:
                    bakiye -= cekilecekmiktar  # Bakiyeden düşmesi lazım.
                    print(f"Islem basarili. Güncel bakiyeniz : {bakiye} TL ")
                else:
                    print(f"Bakiye Yetersiz. Mevcut bakiyeniz : {bakiye} TL ")

            else:
                print("Gecersiz sayi lütfen 1 ile 4 arasinda bir sayi secin.")


# PROGRAMI BAŞLATAN SATIR
anaprogram()
