myList = [1, 2, 3]
# myString = "Hello I am Hazar"

# print(type(myList))
# print(type(myString))


class Movie:
    def __init__(self, title, director, duration):
        self.title = title
        self.director = director
        self.duration = duration
        print("Movie objesi oluşturuldu.")

    def __str__(self):
        return f"{self.title} by {self.director}"

    def __len__(self):
        return self.duration

    def __del__(self):
        print("Movie silindi.")


m = Movie("film adi", "yönetmen adi", 120)

# print(myList)
# print(m)
print(str(m))
# print(len(m))


# Kalanları internet üzerinden araştır.
