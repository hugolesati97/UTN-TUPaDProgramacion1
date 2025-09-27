import statistics
from statistics import mode, median, mean
import random
#Practico 3: esctructuras condicionales

#1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años, deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”

edadUsuario = int(input("Ingrese edad: "))
if edadUsuario < 18:
    print("Sos menor de edad")
else:
    print("Sos mayor de edad")

#2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberámostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar elmensaje “Desaprobado”.

notaFinal = int(input("Ingrese la nota del examen: "))
if notaFinal >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

#3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa unnúmero par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en casocontrario, imprimir por pantalla "Por favor, ingrese un número par".

numPar = int(input("Ingrese un numero: "))
if numPar % 2 == 0:
    print("Ingresaste un numero par")
else:
    print("Ingresaste un numero impar")

#4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las siguientes categorías pertenece

categoriaEdad = int(input("Ingrese su edad: "))
if categoriaEdad < 12:
    print("Sos un niño")
elif categoriaEdad >= 12 and categoriaEdad < 18:
    print("Sos un adolescente")
elif categoriaEdad >= 18 and categoriaEdad < 30:
    print("Sos un adulto joven")
else:
    print("Sos adulto")

#Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres(incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por enpantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir porpantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el usode la función len() en Python para evaluar la cantidad de elementos que tiene un iterable talcomo una lista o un string.

contra = input("Ingrese contraseña: ")
len(contra)
if len(contra) <= 8 and len(contra) <= 14:
    print("La contraseña esta dentro del rango sugerido")
else:
    print("La contraseña esta fuera del rango sugerido")

#Ejercicio 6

numerosAleatorios = [random.randint(1,100) for i in range(50)]

moda = mode(numerosAleatorios)
mediana = median(numerosAleatorios)
media = mean(numerosAleatorios)

if media > mediana > moda:
    sesgo = "Sesgo positivo"
elif media < mediana < moda:
    sesgo = "Sesgo negativo"
elif media == mediana == moda:
    sesgo = "Sin sesgo"
else:
    sesgo= "La distribuicion no encaja"

print("Lista de numeros aleatorios: ")
print(numerosAleatorios)
print("Moda: ", moda)
print("Mediana: ", mediana)
print("Media: ", media)
print("Resultado:", sesgo)

#7)

fraseVocal = str(input("Ingrese la palabra: "))
if fraseVocal [-1] in "aeiou":
    print(fraseVocal,"!")
else:
    print(fraseVocal)

#8)

nombre = input("Ingrese el nombre pedo")
opcion = int(input("Ingrese una opcion del 1 al 3"))
if opcion == 1:
    print(nombre.upper())
elif opcion == 2:
    print(nombre.lower())
elif opcion == 3:
    print(nombre.title())
else:
    print("Ingresa una opcion correcta")

#9)

terremoto = float(input("Ingrese los grados en la escala de richter: "))
if terremoto >= 3 and terremoto <4:
    print("Leve")
elif terremoto >= 4 and terremoto <5:
    print("Moderado")
elif terremoto >= 5 and terremoto <6:
    print("Fuerte")
elif terremoto >=6 and terremoto <7:
    print("Muy fuerte")
elif terremoto >= 7:
    print("EXTREMO")
else:
    print("Imperceptible")

#10
hemisferio = input("En que hemisferio estas? (N/S)")
mes = int(input("En que mes estas? (1-12 segun corresponda)"))
dia = int(input("Que fecha es? (1-31 segun corresponda)"))
if (mes == 12 and dia >= 21) or (1 <= mes <= 2) or (mes == 3 and dia <= 20):
    periodo = 1
elif (mes == 3 and dia >= 21) or (4 <= mes <= 5) or (mes == 6 and dia <= 20):
    periodo = 2
elif (mes == 6 and dia >= 21) or (7 <= mes <= 8) or (mes == 9 and dia <= 20):
    periodo = 3
elif (mes == 9 and dia >= 21) or (10 <= mes <= 11) or (mes == 12 and dia <= 20):
    periodo = 4
else:
    periodo = None

if hemisferio == "N":
    if periodo == 1:
        estacion = "Invierno"
    elif periodo == 2:
        estacion = "Primavera"
    elif periodo == 3:
        estacion = "Verano"
    elif periodo == 4:
        estacion = "Otoño"
    else:
        estacion = "Fecha inválida"
elif hemisferio == "S":
    if periodo == 1:
        estacion = "Verano"
    elif periodo == 2:
        estacion = "Otoño"
    elif periodo == 3:
        estacion = "Invierno"
    elif periodo == 4:
        estacion = "Primavera"
    else:
        estacion = "Fecha inválida"
else:
    estacion = "Hemisferio inválido"
print("Estas en la estacion", estacion)