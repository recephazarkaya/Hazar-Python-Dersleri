# def changename(x) : 
#     x = "hazar"

# name = "recep"

# changename(name)
# print(name)

# def change(n) : 
#     n[0] = "istanbul"

# sehirler = ["ankara","izmir"]

# change(sehirler[:])

# print(sehirler)
# # change
# # n=sehirler[:] #slicing işlemi yapar
# # n[0]="istanbul" 

def add(a,b,c=0) : 
    return sum((a,b,c))

print(add(10,20))
print(add(10,20,30))



def add(*params) : 
    
    print(params)
    print(params[0])

    return sum((params))

print(add(10,20))
print(add(10,20,30))
print(add(10,20,30,40,50,60,70,))




