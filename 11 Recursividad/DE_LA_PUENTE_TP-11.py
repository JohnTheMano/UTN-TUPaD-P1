
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