# --------- EJERCICIO 1 -----------
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

numero = int(input("Ingrese un número: "))

print(f"\nFactoriales del 1 al {numero}:")
for i in range(1, numero + 1):
    print(f"{i}! = {factorial(i)}")

# --------- EJERCICIO 2 -----------
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

posicion = int(input("Ingrese una posición: "))

print(f"\nSerie de Fibonacci hasta la posición {posicion}:")
for i in range(posicion + 1):
    print(fibonacci(i), end=" ")
print()

# --------- EJERCICIO 3 -----------
def potencia(base, exponente):
    if exponente == 0:
        return 1
    return base * potencia(base, exponente - 1)

base = int(input("Ingrese la base: "))
exponente = int(input("Ingrese el exponente: "))

print(f"{base}^{exponente} = {potencia(base, exponente)}")

# --------- EJERCICIO 4 -----------
def decimal_a_binario(n):
    if n == 0:
        return "0"
    if n == 1:
        return "1"
    return decimal_a_binario(n // 2) + str(n % 2)

numero = int(input("Ingrese un número entero positivo: "))
print(f"El número {numero} en binario es {decimal_a_binario(numero)}")

# --------- EJERCICIO 5 -----------
def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])

texto = input("Ingrese una palabra: ")
print(es_palindromo(texto))

# --------- EJERCICIO 6 -----------
def suma_digitos(n):
    if n < 10:
        return n
    return (n % 10) + suma_digitos(n // 10)

numero = int(input("Ingrese un número entero positivo: "))
print(f"La suma de los dígitos de {numero} es {suma_digitos(numero)}")

# --------- EJERCICIO 7 -----------
def contar_bloques(n):
    if n == 1:
        return 1
    return n + contar_bloques(n - 1)

nivel = int(input("Ingrese el número de bloques del nivel más bajo: "))
print(f"Total de bloques necesarios: {contar_bloques(nivel)}")

# --------- EJERCICIO 8 -----------
def contar_digito(numero, digito):
    if numero == 0:
        return 0
    if numero % 10 == digito:
        return 1 + contar_digito(numero // 10, digito)
    else:
        return contar_digito(numero // 10, digito)

num = int(input("Ingrese un número entero positivo: "))
dig = int(input("Ingrese un dígito (0-9): "))
print(f"El dígito {dig} aparece {contar_digito(num, dig)} veces en {num}")

