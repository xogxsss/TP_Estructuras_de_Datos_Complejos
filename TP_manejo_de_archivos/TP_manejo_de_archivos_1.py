# ----------- NOTAS -----------

with open('notas.txt', 'r') as archivo:
    for linea in archivo:
        linea = linea.strip()
        alumno, nota = linea.split(',')
        print(f"Alumno: {alumno} | Nota: {nota}")

with open('notas.txt', 'a') as archivo:
    while True:
        alumno = input('Nombre: ')
        notas = input('Nota: ')
        if alumno.lower() == 'n':
            break
        archivo.write(f'{alumno}, {notas}\n')

with open('notas.txt', 'w') as archivo:
    for i in range(3):
        alumnos = input(f'Alumno N°{i+1}: ')
        notas = float(input('Nota: '))
        archivo.write(f'{alumnos}, {notas}\n')
    print('Contenido anterior reemplazado con éxito.')


# ----------- HELADERÍA -----------

with open('heladeria.csv', 'r') as documento:
    for linea in documento:
        linea = linea.strip()
        sabor, precio, disponible = linea.split(',')
        print(f"Sabor: {sabor} | Precio: ${precio} | Disponible: {disponible}\n")

sabor_agregado = input('Sabor: ')
precio = float(input('Precio: '))
disponible = input('Disponible (sí o no): ')

with open('heladeria.csv', 'a') as documento:
    documento.write(f'{sabor_agregado}, {precio}, {disponible}\n')
    print('Sabor agregado exitosamente.')


# ----------- CINE -----------

with open('cine.csv', 'r') as cine:
    peliculas = cine.read()
    print(peliculas)

with open('cine.csv', 'a') as cine:
    pelicula_agregada = input('Ingrese una película: ')
    cine.write(pelicula_agregada)
    print('Película agregada exitosamente.')

with open('cine.csv', 'r') as cine:
    print(cine.read())


# ----------- PACIENTES -----------

with open('pacientes.csv', 'r') as pacientes:
    pacientes_contenido = pacientes.read()
    print(pacientes_contenido)

with open('pacientes.csv', 'a') as pacientes:
    paciente_agregado = input('Paciente: ')
    edad_paciente = int(input('Edad: '))
    turno = input('Sí o No: ')
    pacientes.write(f'{paciente_agregado},{edad_paciente},{turno}\n')

with open('pacientes.csv', 'r') as pacientes:
    pacientes_contenido = pacientes.read()
    print(pacientes_contenido)


# ----------- EXCURSIONES -----------

with open('excursiones.csv', 'r') as excursiones:
    excursiones_contenido = excursiones.read()
    print(excursiones_contenido)

with open('excursiones.csv', 'a') as excursiones:
    excursion_agregada = input('Destino: ')
    precio_excursion = int(input('Precio: '))
    disponibilidad_excursion = input('Sí o No: ')
    excursiones.write(f'{excursion_agregada},{precio_excursion},{disponibilidad_excursion}\n')

with open('excursiones.csv', 'r') as excursiones:
    excursiones_contenido = excursiones.read()
    print(excursiones_contenido)