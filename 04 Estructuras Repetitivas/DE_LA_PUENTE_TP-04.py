
import random

# 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100 (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.
input("Presione <enter> para imprimir los números enteros desde el 1 a al 100 inclusive")
for i in range(101):
    print(i)
print("\n")


#2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de dígitos que contiene.

print("*** Programa contar dígitos ***")
# Solicitar un número entero
numero = int(input("Ingrese un número entero: "))
digitos = 0
# Verificar si el número es mayor que 0
if numero > 0:
    # Contar los dígitos del número
    while (numero > 0) :
        numero = numero//10      # Eliminar el último dígito
        digitos +=1              # Incrementar el contador de dígitos
    print("La cantidad de dígitos del número ingresado es: ", digitos) # Mostrar resultado de dígitos
else: print("El número ingresado no es un entero") # Mensaje de error si el número no es válido
print("\n")


#3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores dados por el usuario, excluyendo esos dos valores.

print("*** Programa suma de enteros comprendidos entre dos valores ***")
# Solicitar al usuario el primer número entero  
primer_numero = int(input("Ingrese el primer número entero: "))
# Comprobar si el primer número es mayor que 0
if primer_numero > 0:
    # Solicitar al usuario el segundo número entero
    segundo_numero = int(input("Ingrese el segundo número entero: "))
     # Verificar que el segundo número sea mayor que 0
    if segundo_numero > 0:
        # Determinar el rango en el que vamos a sumar
        if primer_numero > segundo_numero:
            inicio = segundo_numero
            final = primer_numero
        else:
            inicio = primer_numero
            final = segundo_numero
        suma = 0 # Inicializar la variable de suma    
        # Sumar los números entre 'inicio' y 'final', excluyendo los límites
        for i in range(inicio+1, final):
            suma+=i
        print(f'La suma de todos los números enteros comprendidos entre los dos valores dados es igual a: {suma}') # Mostrar el resultado
    else:  print("El segundo número ingresado no es un entero") # Error si el segundo número no es válido
else: print("El primer número ingresado no es un entero") # Error si el primer número no es válido
print("\n")


# 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0.

print("*** Suma de enteros en secuencia ***" )
# Solicitar el primer número entero
num = int(input("Ingrese un número entero (ingrese '0' para terminar): "))
suma_secuencia = 0
# Mientras el número ingresado no sea 0, continuar pidiendo números
while num != 0:
    suma_secuencia += num
    num = int(input("Ingrese otro número entero (ingrese '0' para terminar): "))
# Al ingresar 0, el programa muestra la suma acumulada    
print(f' La suma total de la secuencia es: {suma_secuencia}')
print("\n")

#5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

print("*** Juego de adivinar número ***")
# Generar un número aleatorio entre 0 y 9
numero_aleatorio = random.randint(0, 9)
# Imprimir el número aleatorio (esto es solo para pruebas, normalmente no se muestra al usuario)
print("El número a adivinar es: ", numero_aleatorio)
# Solicitar al usuario que ingrese un número entre 0 y 9
numero_intento = int(input("Ingrese un número entre el 0 y el 9: "))

cont=1 # Solicitar al usuario que ingrese un número entre 0 y 9

# Mientras el número ingresado no sea igual al número aleatorio
while numero_aleatorio != numero_intento:
    numero_intento = int(input("Usted no ha adivinado, ingrese un nuevo número: "))
    cont +=1
# Cuando el número es adivinado, imprimir los intentos realizados
print(f'Felicitaciones!, el número es {numero_aleatorio} y usted lo ha adivinado en: {cont} intentos.') 
print("\n")


# 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos entre 0 y 100, en orden decreciente.

input("Presione <enter> para imprimir los pares desde el número 100 al 0")
for i in range(100,-1,-2):
    print(i)
print("\n")

# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un número entero positivo indicado por el usuario.

print("*** Programa suma de enteros entre 0 y el número ingresado ***")
positivo = int(input("ingrese un número entero positivo: "))
if positivo > 0:
    suma = 0
    for i in range(positivo+1):
        suma+=i
    print(f' La suma de todos los números comprendidos entre 0 y {positivo} es: {suma}')
print("\n")

# 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad menor, pero debe estar preparado para procesar 100 números con un solo cambio).

# Inicialización de variables
numero_limite = 4       # Número de entradas a procesar
pares = 0               # Contador de números pares
impares = 0             # Contador de números impares
positivos = 0           # Contador de números positivos
negativos = 0           # Contador de números negativos
cont = 0                # Contador de entradas procesadas
numero_clasificar = 0   # Variable para almacenar el número 

# Bucle para ingresar y clasificar los números
while cont < numero_limite:
    # Solicitar al usuario un número para clasificar
    numero_clasificar = int(input(f'ingrese el numero a clasificar ({cont+1} de {numero_limite}): '))

    # Clasificar número cero como par
    if numero_clasificar == 0:
        pares +=1

    # Clasificar números distintos de cero
    if numero_clasificar != 0:
        # Clasificar número como positivo o negativo
        if numero_clasificar >0:
            positivos += 1
        else:
            negativos += 1

        # Clasificar número como par o impar
        if numero_clasificar % 2 == 0:
            pares += 1
        else:
            impares += 1

    cont +=1 # Incrementar contador de entradas

# Mostrar resultados finales
print(f'De los {numero_limite} números ingresados encontramos: ')
print(f'Números pares: {pares}')
print(f'Números impares: {impares}')
print(f'Números positivos: {positivos}')
print(f'Números negativos: {negativos}')
print("\n")

# 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe poder procesar 100 números cambiando solo un valor).

print("*** Programa de cálculo de promedio ***")
# Inicialización de variables
cant = 0            # Contador de números ingresados
suma = 0            # Variable para acumular la suma de los números
numero_limite =4    # Número límite de entradas a procesar

# Bucle para ingresar y sumar los números
while cant < numero_limite:
    # Solicitar al usuario un número para ingresar
    numero_ingresado = int(input(f'ingrese numero  ({cant+1} de {numero_limite}): '))
    # Sumar el número ingresado a la variable suma
    suma += numero_ingresado
    # Incrementar el contador de números ingresados
    cant +=1
# Calcular y mostrar el promedio de los números ingresados  
print(f'El promedio de los {numero_limite} números ingresados es: {suma/cant}')
print("\n")

# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.
print("*** Programa invertir números ***")
n1 = int(input("Ingrese el número que desea invertir: "))
numero_invertido = 0
# Invertir el número
if n1 > 0:
    while n1 > 0:
        digito = n1 % 10
        numero_invertido = numero_invertido * 10 + digito
        n1 = n1 // 10
    print(f'El número ingresado invertido es: {numero_invertido}')
else:
    print("El número ingresado debe ser mayor a 0")