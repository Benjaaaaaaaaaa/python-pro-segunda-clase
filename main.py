import random
caracteres = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
num=int(input("ingresa la cantidad de letras en tu contraseña:"))
password=""
for i in range(num):
    password += random.choice(caracteres)
print (password)
