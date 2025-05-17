# 1. Crear una función llamada imprimir_hola_mundo que imprima por pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el programa principal.

def imprimir_hola_mundo():
    print("Hola Mundo!")
imprimir_hola_mundo()

# 2. Crear una función llamada saludar_usuario(nombre) que reciba como parámetro un nombre y devuelva un saludo personalizado. Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver: “Hola Marcos!”. Llamar a esta función desde el programa principal solicitando el nombre al usuario.

def saludar_usuario(nombre):
    return f"Hola {nombre}!"  # devuelve el saludo personalizado

# Programa principal
nombre_usuario = input("Ingrese su nombre: ")
saludo = saludar_usuario(nombre_usuario)
print(saludo)  # mostramos el saludo por consola

# 3. Crear una función llamada informacion_personal(nombre, apellido, edad, residencia) que reciba cuatro parámetros e imprima: “Soy [nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pedir los datos al usuario y llamar a esta función con los valores ingresados.

def informacion_personal(nombre, apellido, edad, residencia):
    return f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}"

# Programa principal
nombre = input("Ingrese su Nombre: ")
apellido = input("ingrese Su apellido: ")
edad = input("Ingrese su edad: ")
residencia = input("Ingrese su residencia: ")

print(informacion_personal(nombre,apellido,edad,residencia))


# 4. Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva el área del círculo. calcular_perimetro_circulo(radio) que reciba el radio como parámetro y devuelva el perímetro del círculo. Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados.


def calcular_area_circulo(radio):
    area = radio**2 * 3.1416
    return area

def  calcular_perimetro_circulo(radio):
    perimetro = radio * 2 * 3.1416
    return perimetro

# Programa principal
radio= float(input("Ingrese el radio de la circunferencia: "))
print(f'El Perímetro del radio ingresado es: {calcular_perimetro_circulo(radio):.2f} y el área es: {calcular_area_circulo(radio):.2f}')

# 5. Crear una función llamada segundos_a_horas(segundos) que reciba una cantidad de segundos como parámetro y devuelva la cantidad de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta función.

def segundos_a_horas(segundos):
    horas = segundos / 3600
    return horas

# Programa principal
segundos = float(input("Ingrese la cantidad de segundos que quiere convertir en horas: "))
print(f'{segundos} segundos equivalen a {segundos_a_horas(segundos):.2f} horas')

# 6. Crear una función llamada tabla_multiplicar(numero) que reciba un número como parámetro y imprima la tabla de multiplicar de ese número del 1 al 10. Pedir al usuario el número y llamar a la función.

def tabla_multiplicar(numero):
    for i in range(1,11):
        print(f' {numero} X {i} = {i*numero}')

# Programa principal
numero = int(input("Ingrese el número para calcular su tabla de multiplicar: "))
tabla_multiplicar(numero)

# 7. Crear una función llamada operaciones_basicas(a, b) que reciba dos números como parámetros y devuelva una tupla con el resultado de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los resultados de forma clara.

def operaciones_basicas(a, b):
    tupla = (a+b,a-b,a*b,a/b)
    return tupla

# Programa principal    
a = float(input("Ingrese el primer valor: "))
b = float(input("Ingrese el segundo valor: "))
tupla_operaciones = operaciones_basicas(a, b)
print(f'La Suma de {a} + {b} es ={tupla_operaciones[0]}')
print(f'La Resta de {a} - {b} es ={tupla_operaciones[1]}')
print(f'La Multiplicación de {a} * {b} es ={tupla_operaciones[2]:.2f}')
print(f'La División de {a} / {b} es ={tupla_operaciones[3]:.2f}')


# 8. Crear una función llamada calcular_imc(peso, altura) que reciba el peso en kilogramos y la altura en metros, y devuelva el índice de masa corporal (IMC). Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales.

def calcular_imc(peso, altura):
    imc = (peso/altura**2)
    return imc

# Programa principal
peso = float(input("Ingrese su peso en kilogramos: "))
altura = float(input("Ingrese su altura en metros: "))
print(f'El IMC del peso y altura ingresada es: {calcular_imc(peso, altura):.2f}')

# 9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba una temperatura en grados Celsius y devuelva su equivalente en Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el resultado usando la función.

def celsius_a_fahrenheit(celsius):
    farenheit = (celsius*9/5)+32
    return farenheit

grados = float(input("Ingrese los Grados Celsius que desea convertir a Fahrenheit: "))
print(f'{grados} grados Celsius equivale a {celsius_a_fahrenheit(grados)} Fahrenheit')

# 10.Crear una función llamada calcular_promedio(a, b, c) que reciba tres números como parámetros y devuelva el promedio de ellos. Solicitar los números al usuario y mostrar el resultado usando esta función.

def calcular_promedio(a, b, c):
    promedio = (a+b+c)/3
    return promedio

# Programa principal
print("Calcular Promedio: ")
a = float(input("Ingrese el primer valor:  "))
b = float(input("Ingrese el segundo valor: "))
c = float(input("Ingrese el tercer valor: "))

print(f'El promedio de los números {a} + {b} + {c} es = {calcular_promedio(a,b,c):.2f}')