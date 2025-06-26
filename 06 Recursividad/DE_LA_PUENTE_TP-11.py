
# 1- Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa función para calcular y mostrar en pantalla el factorial de todos los números enteros entre 1 y el número que indique el usuario 

def factorial_num(num):
    if num <= 0:
        return f'El número ingresado debe ser mayor a 0'
    elif num == 1:
        return 1
    else:
        return num*factorial_num(num-1)

num=int(input("Ingrese un numero: "))
print(f'El factorial de {num} es: {factorial_num(num)}')



# 2- Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario especifique. 


def fibonacci(num):
    # Caso base: si la posición es 0, el valor es 0
    if num == 0:
        return 0
    # Caso base: si la posición es 1, el valor es 1
    elif num == 1:
        return 1
    # Caso recursivo: suma de los dos valores anteriores
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)

# Pedimos al usuario que ingrese la posición hasta la que desea ver la serie
posicion = int(input("Introduce la posición de la serie de Fibonacci que desea visualizar: "))

# Mostramos un mensaje indicando qué posición se va a mostrar
print(f"Posición fibonacci: {posicion}:")

# Usamos un bucle para imprimir todos los valores desde la posición 0 hasta la posición indicada
for i in range(posicion + 1):
    print(fibonacci(i))  # Imprimimos el valor de Fibonacci en la posición i



# 3- Crea una función recursiva que calcule la potencia de un número base elevado a un exponente, utilizando la fórmula 𝑛𝑚 = 𝑛 ∗ 𝑛(𝑚−1). Prueba esta función en un algoritmo general. 

def potencia_num(num, exp):
    if num <= 0:
        return f'El número ingresado debe ser mayor a 0'  # Validación base > 0
    elif exp == 0:
        return 1  # Cualquier número elevado a 0 es 1
    elif exp == 1:
        return num  # Base elevada a 1 es ella misma
    else:
        return num * potencia_num(num, exp - 1)  # Caso recursivo
    
def ejecutar():
    base = int(input("Ingrese la base (número mayor a 0): "))
    exponente = int(input("Ingrese el exponente (entero no negativo): "))
    resultado = potencia_num(base, exponente)
    print(f"{base} elevado a {exponente} es: {resultado}")

ejecutar()

# 4- Crear una función recursiva en Python que reciba un número entero positivo en base decimal y devuelva su representación en binario como una cadena de texto.

def recibir_entero(num):
    # Caso base: si el número es 0 o 1, devuelve como cadena
    if num < 2:
        return str(num)
    else:
        # División entera y agrega el residuo
        return recibir_entero(num//2)+str(num%2)
    
print(recibir_entero(8))

# 5- Implementá una función recursiva llamada es_palindromo(palabra) que reciba una cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no lo es.

def es_palindromo(palabra):
    # Si la palabra tiene 1 o ningún carácter, es un palíndromo
    if len(palabra) <= 1:
        return True
    # Si el primer y último carácter son distintos, no es palíndromo
    if palabra[0] != palabra[-1]:
        return False
    # Verifica recursivamente la subcadena sin el primer y último carácter
    return es_palindromo(palabra[1:-1])

print(es_palindromo("oro"))
print(es_palindromo("negro"))

# 6-Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un número entero positivo y devuelva la suma de todos sus dígitos.

def suma_digitos(n):
    # caso base: suma 0
    if n==0: 
        return n
    else:
        # suma último dígito + suma recursiva del resto
        return n % 10 + suma_digitos(n//10)
    
print(suma_digitos(45)) 

# 7- Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al último nivel con un solo bloque. Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el nivel más bajo y devuelva el total de bloques que necesita para construir toda la pirámide.

def contar_bloques(n):
    # caso base: 1 bloque
    if n==1:
        return n
    else:
        # suma actual + recursión
        return n+contar_bloques(n-1)
        
print(contar_bloques(10))


# 8- Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces aparece ese dígito dentro del número.

def contar_digito(numero, digito):
    # caso base: número terminado
    if numero == 0 :
        return 0
    # suma si hay coincidencia
    elif numero%10 == digito:
        return 1 + contar_digito(numero//10,digito)
    else:
        # sigue sin sumar
        return contar_digito(numero//10,digito)
        
        
print(contar_digito(233333335,3))