# 1) Dado el diccionario precios_frutas
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':  1450}
#   Añadir las siguientes frutas con sus respectivos precios:
#   ● Naranja = 1200
#   ● Manzana = 1500
#   ● Pera = 2300

precios_frutas["Naranja"] = 1200
precios_frutas["Manzana"] = 1500
precios_frutas["Pera"] = 2300

print(precios_frutas)

# 2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
# desarrollado en el punto anterior, actualizar los precios de las siguientes frutas:

precios_frutas["Banana"]= 1330
precios_frutas["Manzana"] = 1700
precios_frutas["Melón"] = 2800

print(precios_frutas)

# 3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
# desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los
# precios.

lista_frutas = list(precios_frutas.keys())
print(lista_frutas)

# 4) Escribí un programa que permita almacenar y consultar números telefónicos.
# • Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
# • Luego, pedí un nombre y mostrale el número asociado, si existe

print("\n=== Programa de carga de números telefónicos ===")

guia = {}
for i in range(5):
    nombre = input("\ningrese su nombre: ")
    numero = input("ingrese el numero de teléfono: ")
    i+=1
    guia[f"{nombre}"] = numero
    print(f"\nRegistro {i} ingresado con exito!")
    
print(guia)

print(input("\n=== presione una tecla para continuar ==="))

nombre_a_buscar = input("=== ingrese el nombre que desea buscar en la guía:\n")
if  nombre_a_buscar in guia:
    print(f"El número de teléfono de {nombre_a_buscar} es: {guia[nombre_a_buscar]}")
else:
    print("El nombre ingresado no se encuetra registrado en la guía")

# 5) Solicita al usuario una frase e imprime:
# • Las palabras únicas (usando un set).
# • Un diccionario con la cantidad de veces que aparece cada palabra.