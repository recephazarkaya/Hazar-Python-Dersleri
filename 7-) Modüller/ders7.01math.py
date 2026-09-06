# YÖNTEM 1
# import math  # --> modülü çağırmaya yarar.
import math as islem  # bu şekilde math modülünü istediğimiz bir isime atayabiliriz.

# x = dir(math)  # modülün içinde hangi fonksiyonlar olduğunu görmemizi sağlar
# x = help(math)  # --> modülün içindeki fonksiyonların hepsinin nasıl çalıştığını anlatır.
# x = help(math.factorial)
# içindeki tek bir fonksiyonun (bu satır için faktöriyel) nasıl çalıştığını anlatır.

# y = math.sqrt(81)

# hzr = islem.factorial(5)
# print(x)
# print(y)
# print(hzr)

# YÖNTEM 2

from math import *  # --> * işareti math modülündeki bütün işlemleri kapsar.

# bu şekilde aşağıda gözüktüğü gibi sadece fonksiyonu çağırarak modülün fonksiyonlarını kullanabiliriz.
# eğer sadece belirli fonksiyonları kullanmak istiyorsak -from math import factorial, sqrt- şeklinde belirtmemiz gerekir.

value = factorial(5)


print(value)
