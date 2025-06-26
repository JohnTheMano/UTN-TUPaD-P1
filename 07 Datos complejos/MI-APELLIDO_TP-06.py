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

# 8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock.
# Permití al usuario:
# • Consultar el stock de un producto ingresado.
# • Agregar unidades al stock si el producto ya existe.
# •     

stock_productos = {
    "cuadernos": 120,
    "lapiceras": 200,
    "marcadores": 85,
    "trinchetas": 60,
    "reglas": 45,
    "mochilas": 30,
    "cartucheras": 25,
    "gomas": 150
}

def existe_producto(entrada,stock):
    return entrada in stock

def agregar_stock_producto(entrada, stock):
    if existe_producto(entrada, stock):
        cantidad = int(input(f"Ingrese la cantidad que desea sumar al stock de '{entrada}': "))
        stock[entrada] += cantidad
        print(f"Ahora el producto '{entrada}' tiene {stock[entrada]} unidades.")
    else:
        print(f"El producto '{entrada}' no existe en el inventario.")
        agregar = input(f"¿Deseás agregar '{entrada}' como nuevo producto? (s/n): ").lower()
        if agregar == "s":
            cantidad = int(input(f"Ingrese la cantidad inicial para '{entrada}': "))
            stock[entrada] = cantidad
            print(f"Producto '{entrada}' agregado con {cantidad} unidades.")
        else:
            print("No se agregó el producto.")


def consultar_stock(entrada):
    for producto in stock_productos.keys():
        if producto == entrada:
            return stock_productos[entrada]

while True:
    accion = input("¿Querés consultar o agregar un producto? (consultar/agregar/salir): ").lower()

    if accion == "consultar":
        producto = input("Nombre del producto a consultar: ").lower()
        stock = consultar_stock(producto)
        if stock is not None:
            print(f"Stock de '{producto}': {stock} unidades.")
        else:
            print("Ese producto no existe en el inventario.")

    elif accion == "agregar":
        producto = input("Nombre del producto a agregar o actualizar: ").lower()
        agregar_stock_producto(producto, stock_productos)

    elif accion == "salir":
        print("\nStock final actualizado:")
        for producto, cantidad in stock_productos.items():
            print(f"{producto}: {cantidad} unidades")
        break

    else:
        print("Opción no válida. Escribí 'consultar', 'agregar' o 'salir'.")


# 9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.

agenda = {}

def agregar_evento(dia, hora, evento):
    clave = (dia, hora)
    agenda[clave] = evento
    print(f"Evento agregado para el {dia} a las {hora}: {evento}")

def consultar_evento(dia, hora):
    clave = (dia, hora)
    if clave in agenda:
        print(f"Evento programado para el {dia} a las {hora}: {agenda[clave]}")
    else:
        print("No hay ningún evento programado en ese horario.")

agregar_evento("martes", "14:00", "reunión de grupo")
consultar_evento("martes", "14:00")
consultar_evento("viernes", "09:00")

# 10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo
# diccionario donde:
# • Las capitales sean las claves.
# • Los países sean los valores.

paises = {
    "argentina": "buenos aires",
    "colombia": "bogotá",
    "venezuela": "caracas",
    "perú": "lima",
    "bolivia": "la paz",
    "ecuador": "quito",
    "costa rica": "san josé",
    "brasil": "brasilia"
}

def invertir_diccionario(diccionario):
    invertido = {}
    for pais in diccionario:
        capital = diccionario[pais]
        invertido[capital] = pais
    return invertido

capitales = invertir_diccionario(paises)
print(capitales)
