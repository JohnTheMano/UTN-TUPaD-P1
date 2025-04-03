from statistics import mode, median, mean
import random

# 1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años, deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.

# Se solicita al usuario que ingrese su edad
edad = int(input("Ingrese su edad: "))

# Se verifica si la edad es 18 o más para determinar si es mayor de edad
if edad >= 18:
    # Si la edad es 18 o mayor, se muestra el mensaje
    print("Es mayor de edad")

# 2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el mensaje “Desaprobado”.

# Se solicita al usuario que ingrese su nota
nota = int(input("Ingrese su nota: "))

# Si la nota es 6 o mayor, se muestra "Aprobado"
if nota >= 6:
    print("Aprobado")
# Si la nota es menor a 6, se muestra "Desaprobado"
else:
    print("Desaprobado")

# 3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del operador de módulo (%) en Python para evaluar si un número es par o impar.

# Se solicita al usuario que ingrese un número
numero = int(input("Ingrese un número par: "))

# Se verifica si el número es par
if numero % 2 == 0:
    print("Ha ingresado un número par")
else:
    # Si el número no es par, se pide que ingrese otro
    print("Por favor, ingrese un número par")


# 4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las siguientes categorías pertenece:
#  ● Niño/a: menor de 12 años.
#  ● Adolescente: mayor o igual que 12 años y menor que 18 años.
#  ● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
#  ● Adulto/a: mayor o igual que 30 años.

# Se solicita al usuario que ingrese su edad
edad = int(input("Ingrese su edad: "))

# Se verifica en qué rango de edad cae el usuario y se imprime la categoría correspondiente
if edad >= 0 and edad < 12:
    print("Niño/a")
elif edad >= 12 and edad < 18:
    print("Adolescente")
elif edad >= 18 and edad < 30:
    print("Adulto/a joven")
else:
    print("Adulto/a")

# 5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres (incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal como una lista o un string.

# Se solicita al usuario que ingrese una contraseña
contraseña = input("Ingrese una contraseña (entre 8 y 14 caracteres)")

# Verifica si la longitud de la contraseña está dentro del rango válido y se confirma o no
if len(contraseña) >= 8 and len(contraseña) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

# 6) Escribir un programa que tome la lista numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.

# Genera una lista de 50 números aleatorios entre 1 y 100
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

# Calcula la media, mediana y moda de la lista de números
media = mean(numeros_aleatorios)
mediana = median(numeros_aleatorios)
moda = mode(numeros_aleatorios)

# Imprime la lista de números y las medidas estadísticas
print(numeros_aleatorios)
print("la mediana es: ",mediana)
print("la moda es: ", moda)
print("la media es: ", media)

# Determina el tipo de sesgo según las relaciones entre la media, mediana y moda y se informa
if media == mediana == moda:
    print("Sin sesgo")
elif media > mediana and mediana < moda:
    print("Hay sesgo Positivo")
elif media < mediana and mediana < moda:
    print("Hay sesgo Negativo")


# 7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por pantalla.

# Se solicita al usuario ingresar una palabra o frase y se convertirá a minúsculas
frase = input("Ingrese una palabra o frase").lower()

# Se verifica si la última letra de la frase es una vocal
if frase[-1] == 'a' or frase[-1]  == 'e' or frase[-1]  == 'i' or frase[-1]  == 'o' or frase[-1]  == 'u':

    # Si la última letra es una vocal, se agrega un "!" al final
    print(frase + "!")
else:
    # Si la última letra no es una vocal, se imprime sin modificaciones
    print(frase)


#8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 dependiendo de la opción que desee:
# 1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
# 2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
# 3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
# El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(), lower() y title() de Python para convertir entre mayúsculas y minúsculas.

# Se solicita al usuario su nombre
nombre = input("Ingrese su nombre: ")

# Se muestran las opciones para modificar el formato del nombre
print("Presione el '1' Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.")
print("Presione el '2' Si quiere su nombre en minúsculas. Por ejemplo: pedro.")
print("Presione el '3' Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.")

# Se solicita la opción de formato deseado
seleccion = input("Seleccione la opción deseada: ")

# Se evalúa la opción seleccionada, se aplica el formato correspondiente y se informa
if seleccion == "1":
    print(nombre.upper())
elif seleccion == "2":
    print(nombre.lower())
elif seleccion == "3":
    print(nombre.title())
else:
    print("selección no válida")

#9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado por pantalla:
# ● Menor que 3: "Muy leve" (imperceptible).
# ● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
# ● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero generalmente no causa daños).
# ● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras débiles).
# ● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
# ● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).

# Se solicita la magnitud del terremoto al usuario
magnitud = float(input("Ingrese la magnitud de un terremoto para su clasificación: "))

# Se verifica que la magnitud sea mayor que 0
if magnitud > 0:

     # Se clasifica según el rango de la magnitud y se informa según corresponda
    if magnitud < 3:
        print('"Muy leve" (imperceptible).')
    elif magnitud >= 3 and magnitud < 4:
        print('"Leve" (ligeramente perceptible).')
    elif magnitud >= 4 and magnitud < 5:
        print('"Moderado" (sentido por personas, pero generalmente no causa daños).')
    elif magnitud >= 5 and magnitud < 6:
        print('"Fuerte" (puede causar daños en estructuras débiles).')
    elif magnitud >= 6 and magnitud < 7:
        print('"Muy Fuerte" (puede causar daños significativos).')
    else:
        print('"Extremo" (puede causar graves daños a gran escala).')
else:
    print('El número ingresado debe ser mayor a 0')

# Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla si el usuario se encuentra en otoño, invierno, primavera o verano.

# Se solicita al usuario que ingrese el hemisferio (Norte o Sur)
hemisferio = input('Ingrese el hemisferio en el que se encuentra: "N" / "S"').upper()

# Se solicita el número del mes y el día actual
mes = input("Ingrese el número de mes actual: ")
dia = input("Ingrese la fecha actual: ")

# Si el mes tiene un solo dígito, se agrega un "0" al principio
if len(mes) == 1:
    mes = "0" + mes 
    
# Si el día tiene un solo dígito, se agrega un "0" al principio
if len(dia) == 1:
    dia = "0" + dia 



# Se combina el mes y el día para obtener una representación numérica del día del año
mes_dia = mes + dia
mes_dia_numerico = int(mes_dia)

# Se evalúa en qué rango de fechas estamos y se determina la estación según el hemisferio y se muestra en pantalla según corresponda
if mes_dia_numerico >= 321 and mes_dia_numerico <= 620:
    if hemisferio == "N":
        print("Primavera")
    else:
        print("Otoño")

elif mes_dia_numerico >= 621 and mes_dia_numerico <= 920:
    if hemisferio == "N": 
        print("Verano")
    else:
        print("Invierno")

elif mes_dia_numerico >= 921 and mes_dia_numerico <= 1220:
    if hemisferio == "N":
        print("Otoño")
    else:
        print("Primavera")

else:
    if hemisferio == "N":
        print("Invierno")
    else:
        print("Verano")