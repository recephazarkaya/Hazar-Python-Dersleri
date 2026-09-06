# x="global x"
# def function():
#     x= "local x"
#     print(x)
# function()
# print(x)

# fonksiyonun içinde yapılan değişiklikler yerel olarak algılanır ve fonksiyon dışını etkilemez.


#####################
name ="hazar"

# def changename(new_name) : 
#     name =new_name
#     print(name)

# changename("asya")
# print(name)

#####################
# name="hazar"

# def greeting(): 
#      name="asya"

#     def hello(): 
#         print("hello " + name)

#     hello()

# greeting()

# iç içe geçen fonksiyonlarda bu şekilde olur.


##############################


# x = 50  
# def test() : 
   
#    global x
#    print(f"x : {x}") 
#    x=100
    
#    print(f"changed x to  {x}")

# test()

# print(x)

# global keywordu fonksiyon içinde yeni bir tane değer oluşturulmasını engelleyip dışarıdaki değerin kullanılmasını(değiştirilmesini) sağlar.