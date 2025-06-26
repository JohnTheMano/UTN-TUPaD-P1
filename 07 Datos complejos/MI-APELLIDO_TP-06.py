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

def frase_a_lista(frase):
    frase_lista = frase.split()
    return frase_lista

def cuenta_palabras_a_diccionario(listado):
    for i in range(len(listado)):
        if listado[i] not in diccionario:
            diccionario[listado[i]]=1
        else:
            diccionario[listado[i]] += 1
    return diccionario  

diccionario={}

entrada = input("Ingrese una frase")

listado = frase_a_lista(entrada)

respuesta = cuenta_palabras_a_diccionario(listado)

print(respuesta)


# 6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas.
# Luego, mostrá el promedio de cada alumno.

alumnos={}
for i in range(3):
    notas =[]
    nombre = input(f"\ningrese nombre del alumno {i+1}: ")
    for j in range(3):
        notas.append(int(input(f"Ingrese la Nota {j+1}: ")))
    alumnos[nombre]=tuple(notas)

print(alumnos)

# 7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1
# y Parcial 2:
# • Mostrá los que aprobaron ambos parciales.
# • Mostrá los que aprobaron solo uno de los dos.
# • Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir)

parcial1 = {1001, 1002, 1003, 1007, 1010, 1012, 1015, 1020}
parcial2 = {1002, 1004, 1005, 1007, 1010, 1018, 1020, 1022}

def buscar_ambos(set1, set2):
    ambos_aprobados = set1 and set2  
    aprobaron_el_primero = set1 - set2 
    aprobaron_el_segundo = set2 - set1  
    return ambos_aprobados, aprobaron_el_primero, aprobaron_el_segundo

ambos, solo1, solo2 = buscar_ambos(parcial1, parcial2)

print(f"Aprobaron ambos parciales: {ambos}")
print(f"Aprobaron solo el parcial 1: {solo1}")
print(f"Aprobaron solo el parcial 2: {solo2}")
