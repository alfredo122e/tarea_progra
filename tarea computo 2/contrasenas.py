from pickle import FALSE
print("========================================================================")
print(             "Bienvenido al Modulo de valiadacion de contraeñas:"         )
print("========================================================================")
print("========================================================================")
contrasena = input("por favor ingrese su contraseña a evaluar: ")
print("========================================================================")

#usamos def para poder usar el modulo en el siguiente archivo
def password(passwd):
    contra=passwd
    return contra
print("========================================================================")

#usamos lem para poder contar la cantidad de caracteres permitidos 
if len(contrasena) <8:
    print("La Contraseña es muy corta, debe tener más de 8 carácteres por favor vuelva a intertarlo: ")
    print("========================================================================")
    
    print("========================================================================")
#
else:
    minuscula = False
for minus in contrasena:
#El método islower() devuelve True si todos los caracteres están en minúsculas, de lo contrario, False. Los números, símbolos y espacios no están marcados, solo el alfabeto
    if minus.islower ==True:
     mayuscula = True
if not minuscula:
    print("La contraseña debe contener al menos una minusculas por favor vuelva a intenaro")
    print("========================================================================")
    
    print("========================================================================")
mayusculas = False
for mayus in contrasena:
#
   if mayus. isupper ()==True:
    mayusculas = True
if not mayusculas:
    print("La contraseña debe tener al menos una mayuscula")
    print("========================================================================")
    print("========================================================================")
num=FALSE
for carac in contrasena:
   if carac. isdigit ()== True:
    num=True
if not num:
    print("La contraseña debe tener al menos un numero")
    print("========================================================================")
    print("========================================================================")
if contrasena.count (" ")> 0:
    print("La contrasena no puede contener espacios en blanco")
    print("========================================================================")
    print("========================================================================")
else:
     print("Contraseña segura")
     print("========================================================================")
     
     
     