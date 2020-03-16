lista = [1, 'hola', 1.23, True, [1, 2, 3]]
colores = ['Rojo', 'Verde', 'Azul']
print(len(lista))

print(colores[-3])
print(colores[2])
print('verde' in colores) # False
print('Verde' in colores) # True


# Construir una lista Constructor
number_list = list((1,2,3,4))
print(number_list)

r = list(range(0,10))
print(r)

## cambiar datos de una lista

print(colores)
colores[1] = 'Blanco'
print(colores)

colores.append('Blanco') # Solo agrega uno
# colores.append(['Rosa', 'Negro']) # Agraga un array dentro del array, no los agrega al final
print(colores)

colores.extend(['Rosa', 'Negro']) 
print(colores)

colores.insert(2, 'Otro color')
print(colores)

colores.pop() # le podeomos pasar el indice
print(colores)

colores.remove('Otro color')
print(colores)

# colores.clear() # borra toda la lista

colores.sort()
print(colores)
colores.sort(reverse=True)
print(colores)