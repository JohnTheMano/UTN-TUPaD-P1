

def factorial_num(num):
    if num <= 0:
        return f'El número ingresado debe ser mayor a 0'
    elif num == 1:
        return 1
    else:
        return num*factorial_num(num-1)

num=int(input("Ingrese un numero"))
print(f'El factorial de {num} es: {factorial_num(num)}')