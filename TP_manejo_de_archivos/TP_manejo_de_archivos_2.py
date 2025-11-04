# ----------- PRODUCTOS -----------
with open('productos.txt', 'r') as archivo:
    for lineas in archivo:
        lineas = lineas.strip()
        producto, precio, cantidad = lineas.split(',')
        print(f'Producto: {producto} | Precio: ${precio} | Cantidad: {cantidad}\n')

# --------- AGREGAR NUEVOS PRODUCTOS ---------
producto_agregado = input('Nuevo producto: ')
precio_producto = float(input('Precio: '))
stock_producto = int(input('Cantidad: '))

with open('productos.txt', 'a') as archivo:
    archivo.write(f'\n{producto_agregado},{precio_producto},{stock_producto}')
    print('Producto agregado exitosamente')

# --------- CREAR LISTA CON DICCIONARIOS ---------

productos = []

with open('productos.txt', 'r') as archivo:
    for lineas in archivo:
        lineas = lineas.strip()
        producto, precio, cantidad = lineas.split(',')
        productos.append({
                'Nombre': producto,
                'Precio': precio,
                'Cantidad': cantidad
            })

# --------- BUSCAR PRODUCTO POR NOMBRE ---------
with open('productos.txt', 'r') as archivo:
    buscar = input('Ingrese el nombre del producto que desea buscar: ').lower()
    encontrado = False

    for prod in productos:
        if prod['Nombre'].lower() == buscar:
            print('\nProducto encontrado:')
            print(f'Nombre: {buscar.capitalize()}')
            print(f'Precio: {prod['Precio']}')
            print(f'Cantidad: {prod['Cantidad']}') 
            encontrado = True
            break
    if not encontrado:
        print('Producto no encontrado.')  

# --------- ACTUALIZAR LISTA ---------
with open('productos.txt', 'w') as archivo:
    for prod in productos:
        archivo.write(f'{prod['Nombre']},{prod['Precio']},{prod['Cantidad']}\n')

print('Lista actualizada.')