# try:
#     file = open("newfile.txt", "r")
#     print(file)
# except FileNotFoundError:
#     print("Dosya Okuma Hatasi.")
# finally:
#     print("Dosya kapandi.")
#     file.close()

file = open("newfile.txt", "r", encoding="utf-8")
# for döngüsü

# for i in file:
#     print(i, end=" ")
# content1 = file.read()
# print("içerik 1")
# print(content1)

# file = open("newfile.txt", "r", encoding="utf-8")

# content2 = file.read()
# print("içerik 2")
# print(content2)


# content = file.read(8)
# content = file.read(9)
# print(content)


# readline fonksiyonu

# content = file.readline()
# content = file.readline()
# content = file.readline()
# print(content)

# readlines fonksiyonu

# liste = file.readlines(0)
# liste = file.readlines(1)
# liste = file.readlines(2)
# print(liste)


file.close()
