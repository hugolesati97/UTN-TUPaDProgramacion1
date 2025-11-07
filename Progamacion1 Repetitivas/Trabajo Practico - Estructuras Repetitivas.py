#EJERCICIO 1
#for i in range (0,100+1):
#   print(i)

#EJERCICIO 2
#numero_entero = int(input("Ingrese un numero: "))
#digitos = len(str(numero_entero))
#print("El numero es", numero_entero, "Y tiene", digitos, "digitos")

#EJERCICIO 3
#suma = 0

#primero = int(input("Ingrese un numero: "))
#ultimo = int(input("Ingrese un numero: "))

#if primero > ultimo:
#    primero, ultimo = ultimo, primero

#for i in range(primero +1, ultimo):
#    suma += i

#print("La suma de los numeros entre", primero, "y", ultimo, "es", suma)

#EJERCICIO 4
#suma = 0 

#while True:
#    numero = int(input("Ingrese un numero (0 si queres terminarlo): "))
#    if numero == 0:
#         break
#     suma += numero

#print("La suma de todo es: ", suma)

#EJERCICIO 5

# print("Juego de adeivianar el numero de entre 0 a 9")

# while True:
#     numero_secreto = int(input("Ingrese un numero del 0 al 9 asi el jugador lo adivina: "))
#     if 0 <= numero_secreto <= 9:
#         break
#     else:
#         print("Ingres un numero del 0 al 9 por favor")

# print("Ahora adivina el numero")

# intentos = 0

# while True:
#     intento = int(input("Cual es el numero?: "))

#     if intento < 0 or intento > 9:
#         print("Debe ser un numero del 0 al 9")
#         continue

#     intentos += 1

#     if intento == numero_secreto:
#         print("Felicidades adivinaste el numero el cual era:", numero_secreto)
#         break
#     else:
#         print("Pronba con otro numero")

# print("Lo lograste, el numero era", numero_secreto, "Y lo lograste en", intentos, "Intentos")

#EJERCICIO 6
# for i in range (100, -1, -2):
#     print(i)        

#EJERCICIO 7
# numero = int(input("Ingresa un numero entero: "))

# if numero < 0:
#     print("El numero debe ser positivo")
# else:
#     suma = 0
#     for i in range(numero + 1):
#         suma += i
#     print("La suma de todos los numeros desde 0 hasta", numero, "es:", suma)

#EJERCICIO 7
cantidad_numeros = 5
pares = 0
impares = 0
positivos = 0
negativos = 0

print("Por favor ingresa", cantidad_numeros, "numeros enteros")
print("-" * 50)

for i in range(cantidad_numeros):
    numero = int(input(f"Numero {i + 1}: "))

    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

    if numero < 0:
        negativos += 1
    elif numero > 0:
        positivos+= 1


print(f"Números pares:     {pares}")
print(f"Números impares:   {impares}")
print(f"Números positivos: {positivos}")
print(f"Números negativos: {negativos}")
