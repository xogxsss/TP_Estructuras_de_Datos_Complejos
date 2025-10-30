#1
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':
1450}

precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

print(precios_frutas)

#2 
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

#3 
frutas = [precios_frutas.keys()]
print(frutas)


#4 Consulta de números telefónicos

numeros_telefonicos = {}

for i in range(5):
    nombre = input('Nombre: ')
    telefono = input('Número de teléfono: ')

    numeros_telefonicos[nombre] = telefono

consulta = input('Ingrese un nombre: ')

if consulta in numeros_telefonicos:
    print(f"Nombre: {consulta}\nTeléfono: {numeros_telefonicos[consulta]} ")
else:
    print(f"No se halló el número de {consulta}.")

#5 
frase = input('Ingrese una frase: ')
palabras = frase.split()
conjunto_palabras = set(palabras)

diccionario_palabras = {}

for palabra in palabras:
    if palabra in diccionario_palabras:
        diccionario_palabras[palabra] += 1
    else:
        diccionario_palabras[palabra] = 1

print(f"\nConjunto de palabras:{conjunto_palabras}")
print(f"\nConteo de palabras:{diccionario_palabras}")

#6 
from statistics import mean

alumnos = {}
promedio = {}

for i in range(3):
    nombre = input('Nombre del alumno: ')
    notas = []
    for j in range(3):
        nota = float(input(f'Nota {j+1}: '))
        notas.append(nota)
    alumnos[nombre] = tuple(notas)
    promedio[nombre] = mean(alumnos[nombre])

print("\nPromedio de cada alumno:")
for nombre, prom in promedio.items():
    print(f"{nombre}: {prom:.2f}")


#7 
aprobados_parcial_1 = {'Juan', 'Luis', 'María', 'Ana'}
aprobados_parcial_2 = {'Luis', 'María'}

print(f"\nAprobados en ambos parciales: {aprobados_parcial_1 & aprobados_parcial_2}")

print(f"\nAprobaron solo uno: {aprobados_parcial_1 ^ aprobados_parcial_2}")

print(f"\nAprobaron al menos uno: {aprobados_parcial_1 | aprobados_parcial_2}")

#8
productos = {
    "manzanas": 10,
    "peras": 5,
    "bananas": 8
}

producto = input("Ingrese el nombre del producto: ").lower()

if producto in productos:
    print(f"Stock actual de {producto}: {productos[producto]} unidades.")
    agregar = input("¿Desea agregar unidades al stock? (s/n): ").lower()
    if agregar == "s":
        cantidad = int(input("¿Cuántas unidades desea agregar?: "))
        productos[producto] += cantidad
        print(f"Nuevo stock de {producto}: {productos[producto]} unidades.")
    else:
        print("No se realizaron cambios en el stock.")
else:
    print(f"El producto '{producto}' no existe en el inventario.")
    agregar = input("¿Desea agregarlo? (s/n): ").lower()
    if agregar == "s":
        cantidad = int(input("Ingrese la cantidad inicial de stock: "))
        productos[producto] = cantidad
        print(f"Producto '{producto}' agregado con {cantidad} unidades.")
    else:
        print("No se agregó el producto.")

print("\nInventario actual:")
for prod, stock in productos.items():
    print(f"{prod}: {stock} unidades")


#9
agenda = {
    (1, "10:00"): "Reunión de equipo",
    (2, "14:00"): "Clase de Programación 1",
    (3, "09:30"): "Llamada con cliente",
    (4, "16:00"): "Entrega de proyecto",
    (5, "11:00"): "Corrección de trabajos"
}

dia = int(input("Ingrese el día (1-7): "))
hora = input("Ingrese la hora (formato HH:MM): ")

clave = (dia, hora)

if clave in agenda:
    print(f"El evento en el día {dia} a las {hora} es: {agenda[clave]}")
else:
    print("No hay ningún evento programado en ese día y hora.")

#10

paises = {
    "Argentina": "Buenos Aires",
    "Brasil": "Brasilia",
    "Chile": "Santiago",
    "Uruguay": "Montevideo",
    "Paraguay": "Asunción"
}

capitales = {capital: pais for pais, capital in paises.items()}

print("Diccionario original (país → capital):")
print(paises)

print("\nDiccionario invertido (capital → país):")
print(capitales)
