# 1. Crear una función llamada imprimir_hola_mundo que imprima por pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el programa principal.

def imprimir_hola_mundo():
    print("Hola Mundo!")
imprimir_hola_mundo()

# 2. Crear una función llamada saludar_usuario(nombre) que reciba como parámetro un nombre y devuelva un saludo personalizado. Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver: “Hola Marcos!”. Llamar a esta función desde el programa principal solicitando el nombre al usuario.

def  saludar_usuario(usuario):
    print(f'Hola {usuario}!')
usuario = input("ingrese su nombre: ")

saludar_usuario(usuario)

# 3. Crear una función llamada informacion_personal(nombre, apellido, edad, residencia) que reciba cuatro parámetros e imprima: “Soy [nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pedir los datos al usuario y llamar a esta función con los valores ingresados.

def informacion_personal(nombre, apellido, edad, residencia):
    print(f'Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}')

nombre = input("Ingrese su Nombre: ")
apellido = input("ingrese Su apellido: ")
edad = input("Ingrese su edad: ")
residencia = input("Ingrese su residencia: ")

informacion_personal(nombre,apellido,edad,residencia)

# 4. Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva el área del círculo. calcular_perimetro_circulo(radio) que reciba el radio como parámetro y devuelva el perímetro del círculo. Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados.


def calcular_area_circulo(radio):
    area = radio**2 * 3.1416
    print(f'El área de la circunferencia es: {area:.2f}')

def  calcular_perimetro_circulo(radio):
    perimetro = radio * 2 * 3.1416
    print(f' El perimetro de la circunferencia es: {perimetro:.2f}')

radio= float(input("Ingrese el radio de la circunferencia: "))
calcular_perimetro_circulo(radio)
calcular_area_circulo(radio)

# 5. Crear una función llamada segundos_a_horas(segundos) que reciba una cantidad de segundos como parámetro y devuelva la cantidad de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta función.

def segundos_a_horas(segundos):
    horas = segundos / 3600
    print(f"{segundos} segundos equivalen a {horas:.2f} horas.")

segundos = float(input("Ingrese la cantidad de segundos que quiere calcular en horas: "))
segundos_a_horas(segundos)

# 6. Crear una función llamada tabla_multiplicar(numero) que reciba un número como parámetro y imprima la tabla de multiplicar de ese número del 1 al 10. Pedir al usuario el número y llamar a la función.

def tabla_multiplicar(numero):
    for i in range(1,11):
        print(f' {numero} X {i} = {i*numero}')

numero = int(input("Ingrese el número para calcular su tabla de multiplicar: "))

tabla_multiplicar(numero)

# 7. Crear una función llamada operaciones_basicas(a, b) que reciba dos números como parámetros y devuelva una tupla con el resultado de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los resultados de forma clara.

def operaciones_basicas(a, b):
    tupla = (a+b,a-b,a*b,a/b)
    print(f'La Suma de {a} + {b} es ={tupla[0]}')
    print(f'La Resta de {a} - {b} es ={tupla[1]}')
    print(f'La Multiplicación de {a} * {b} es ={tupla[2]:.2f}')
    print(f'La División de {a} / {b} es ={tupla[3]:.2f}')

a = float(input("Ingrese el primer valor"))
b = float(input("Ingrese el segundo valor"))

operaciones_basicas(a,b)

# 8. Crear una función llamada calcular_imc(peso, altura) que reciba el peso en kilogramos y la altura en metros, y devuelva el índice de masa corporal (IMC). Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales.

def calcular_imc(peso, altura):
    imc = (peso/altura**2)
    print(f'El IMC es: {imc:.2f}')

peso = float(input("Ingrese su peso en kilogramos: "))
altura = float(input("Ingrese su altura en metros: "))
calcular_imc(peso, altura)

# 9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba una temperatura en grados Celsius y devuelva su equivalente en Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el resultado usando la función.

def celsius_a_fahrenheit(celsius):
    farenheit = (celsius*9/5)+32
    print(f'{celsius:.2f} grados Celsius equivale a {farenheit:.2f} grados Farenheit')

celsius = float(input("Ingrese los Grados Celsius que desea convertir a Farenheit: "))
celsius_a_fahrenheit(celsius)

# 10.Crear una función llamada calcular_promedio(a, b, c) que reciba tres números como parámetros y devuelva el promedio de ellos. Solicitar los números al usuario y mostrar el resultado usando esta función.

def calcular_promedio(a, b, c):
    promedio = (a+b+c)/3
    print(f'El promedio de los números {a} + {b} + {c} es = {promedio:.2f}')

print("Calcular Promedio: ")
a = float(input("Ingrese el primer valor:  "))
b = float(input("Ingrese el segundo valor: "))
c = float(input("Ingrese el tercer valor: "))

calcular_promedio(a,b,c)