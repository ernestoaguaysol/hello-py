myStr = "Texto de Prueba"

# print(dir(myStr)) # Métodos

print(myStr.upper())
print(myStr.lower())
print(myStr.capitalize())
print(myStr.swapcase())

print(myStr.split())

print(len(myStr)) # Longitud

print(myStr.isalpha()) # Es alfanumérico
print(myStr.isnumeric()) # Es numérico

print("Este es un "+myStr)
print(f"Este es un {myStr}") ## Solo a partir de la version 3.6
print("Este es un {0}".format(myStr))


