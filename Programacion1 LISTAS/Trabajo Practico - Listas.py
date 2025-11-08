# #Actividad 1
# notas_estudiantes = [7, 2.5, 3, 8, 10, 7.5, 9.2, 8.3, 4, 6.75]

# print("////////////////////////////")
# print("Notas de los 10 estudiantes")
# print("////////////////////////////")
# for i in range(len(notas_estudiantes)):
#     print(f"Estudiante {i+1}: {notas_estudiantes[i]}" )
# print("////////////////////////////")

# promedio_notas = sum(notas_estudiantes) / len(notas_estudiantes)
# print(f"El promedio de las notas fue: {promedio_notas}")
# print("////////////////////////////")

# nota_alta = max(notas_estudiantes)
# nota_baja = min(notas_estudiantes)
# print(f"La nota mas baja fue {nota_baja} y la nota mas alta fue {nota_alta}")

#Actividad 2

# productos = []

# print("Ingresa los 5 productos: ")
# for i in range(5):
#     producto = input(f"Producot {i+1}: ")
#     productos.append(producto)


# print("/" * 22)
# print("Lista de productos")
# print("/" * 22)
# for i, producto in enumerate(productos):
#     print(f"Produto {i + 1}: {producto}")
# print("/" * 22)


# print("")
# print("Productos ordenados alfabeticamente")
# print("/" * 22)
# productos_ordenados = sorted(productos)
# for i, producto in enumerate(productos_ordenados, start=1):
#     print(f"Producto {i}: {producto}")
# print("/" * 22)


# print("")
# producto_eliminar = input("Que producto quers borrar?: ")

# if producto_eliminar in productos_ordenados:
#     productos_ordenados.remove(producto_eliminar)
#     print(f"El producto  {producto_eliminar} fue eliminado")
# else:
#     print(f"El producto {producto_eliminar} no existe")


# print("")
# print("Lista actualizada")
# print("/" * 22)
# for i, producto in enumerate(productos_ordenados, start=1):
#     print(f"Producto {i}: {producto}")




#Actividad 3
# numeros_azar = [45, 12, 87, 34, 56, 23, 78, 91, 2, 67, 38, 55, 84, 19, 50]

# print("Lista de 15 numeros")
# print(numeros_azar)

# pares =[]
# for num in numeros_azar:
#     if num % 2 == 0:
#         pares.append(num)

# impares = []
# for num in numeros_azar:
#     if num % 2 != 0:
#         impares.append(num)

# print("Lista de numeros pares:")
# print(pares)

# print("Lista de numeros impares:")
# print(impares)


#Actividad 4
# datos = [1, 3, 5, 3, 7, 1, 9, 5, 3]

# repeticion = {}
# for num in datos:
#     repeticion[num] = repeticion.get(num, 0) + 1

# no_repetidos = []
# for num in datos:
#     if repeticion[num] == 1 and num not in no_repetidos:
#         no_repetidos.append(num)

# print(no_repetidos)



#Actividad 5

# estudiantes = ["Juan", "María", "Carlos", "Ana", "Luis", "Sofia", "Pedro", "Laura"]

# while True:
#     print("===== ESTUDIANTES =====")
#     for i, estudiante in enumerate(estudiantes, 1):
#         print(f"Estudiante {i}: {estudiante}")

#     print(f"El total de estudiantes {len(estudiantes)}")
#     print("="*50)
#     print("Opciones:")
#     print("="*50)
#     print("1. Agregar un estudiante")
#     print("2. Eliminar un estudiante")
#     print("3. Salir")
#     print("="*50)
    
#     opcion = input("Selecciona una opcion: ")

#     if opcion == "1":
#         nombre = input("Como se llama el nuevo estudiante?")
#         if nombre:
#             estudiantes.append(nombre)
#             print(f"El estudiante {nombre} fue agregado con exito")
    
#     elif opcion == "2":
#         try:
#             numero = int(input("Ingresa el numero del estudiante que queres eliminar: "))
#             if 1 <= numero <= len(estudiantes):
#                 eliminado = estudiantes.pop(numero - 1)
#                 print(f"El estudiando {eliminado} ha sido eliminado con exito")
#             else:
#                 print("El numero no es valido")
#         except:
#             print("Ingresa un numero valido")    
        
#     elif opcion == "3":
#         print("===== LISTA FINAL =====")
#         for i, estudiante in enumerate(estudiantes, 1):
#             print(f"Estudiante {i}: {estudiante}")
#         print(f"El total de estudiantes {len(estudiantes)}")
#         break

#     else:
#         print("Opcion invalida")


#Actividad 6

# numeros = [1, 2, 3, 4, 5, 6, 7]
# numeros_rotados = []

# numeros_rotados.append(numeros[-1])

# for i in range(len(numeros) - 1):
#     numeros_rotados.append(numeros[i])

# print(numeros_rotados)

#Actividad 7

# temperaturas = [
#     [12, 25],  #Lunes
#     [14, 28],  #Martes
#     [11, 24],  #Miércoles
#     [15, 29],  #Jueves
#     [13, 26],  #Viernes
#     [10, 22],  #Sábado
#     [16, 30]   #Domingo
# ]

# dias = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]

# suma_minimas = 0
# for i in range(len(temperaturas)):
#     suma_minimas = suma_minimas + temperaturas[i][0]
# promedio_minimas = suma_minimas / len(temperaturas)

# suma_maximas = 0
# for i in range(len(temperaturas)):
#     suma_maximas = suma_maximas + temperaturas [i][1]
# promedio_maximas = suma_maximas / len(temperaturas)

# mayor_amplitud = 0
# dia_mayor_amplitud = 0
# for i in range(len(temperaturas)):
#     amplitud = temperaturas[i][1] - temperaturas[i][0]
#     if amplitud > mayor_amplitud:
#         mayor_amplitud = amplitud
#         dia_mayor_amplitud = i

# print(f"El promedio de minimas es: {promedio_minimas} grados celsios")
# print(f"El promedio de maximas es: {promedio_maximas} grados celsios")
# print(f"La mayor amplitud es de {mayor_amplitud} grados celsios y fue el {dias[dia_mayor_amplitud]}")

#Actividad 8
# notas = [
#     [85, 90, 78], #Estudiante 1
#     [92, 88, 85], #Estudiante 2
#     [78, 82, 80], #Estudiante 3
#     [88, 95, 92], #Estudiante 4
#     [90, 87, 86]  #Estudiante 5
# ]

# estudiantes = ["Estudiante 1", "Estudiante 2", "Estudiante 3", "Estudiante 4", "Estudiante 5"]
# materias = ["Matemática", "Ingles", "Plastica"]

# print("====== PROMEDIO POR ESTUDIANTE ======")
# for i in range(len(notas)):
#     suma = 0
#     for j in range(len(notas[i])):
#         suma = suma + notas[i][j]
#     promedio = suma / len(notas[i])
#     print(f"Estudiante {estudiantes[i]}: {promedio}")

# print("====== PROMEDIO POR MATERIA ======")
# for j in range(len(materias)):
#     suma = 0
#     for i in range(len(notas)):
#         suma = suma + notas[i][j]
#     promedio = suma / len(notas)
#     print(f"Materia {materias[j]}: {promedio}")



#Actividad 9
# tablero = []
# for i in range(3):
#     fila = []
#     for j in range(3):
#         fila.append("-")
#     tablero.append(fila)

# print("==== TA-TE-TI ====")
# print("Jugador 1: X")
# print("Jugador 2: O")

# print("  1  2  2")
# print("-" * 13)
# for i in range(3):
#     print(f"{i} {tablero[i][0]} | {tablero[i][1]} | {tablero[i][2]}")
#     if i < 2:
#         print("  ---------")
# print()

# juego_activo = True
# jugador_actual = "X"

# while juego_activo:
#     entrada = input(f"Jugador {jugador_actual} - Ingresa posicion (fila columna): ")

#     try:
#         partes = entrada.split()
#         fila = int(partes[0])
#         columna = int(partes[1])

#         if fila < 0 or fila > 2 or columna < 0 or columna > 2:
#             print("Posicion fuera de rango")
#             continue

#         if tablero[fila][columna] != "-":
#             print("Posicion ya ocupada")
#             continue

#         tablero[fila][columna] = jugador_actual

#         print()
#         print("  0   1   2")
#         print("-" * 13)
#         for i in range(3):
#             print(f"{i} {tablero[i][0]} | {tablero[i][1]} | {tablero[i][2]}")
#             if i < 2:
#                 print("  ---------")
#         print()

#         ganador= False
#         for i in range(3):
#             if tablero[i][0] == jugador_actual and tablero[i][1] == jugador_actual and tablero[i][2] == jugador_actual:
#                 ganador = True

#         if not ganador:
#             for j in range(3):
#                 if tablero[0][j] == jugador_actual and tablero[1][j] == jugador_actual and tablero[2][j] == jugador_actual:
#                     ganador = True

#         if not ganador:
#             if tablero[0][0] == jugador_actual and tablero[1][1] == jugador_actual and tablero[2][2] == jugador_actual:
#                 ganador = True

#         if not ganador:
#             if tablero[0][2] == jugador_actual and tablero[1][1] == jugador_actual and tablero[2][0] == jugador_actual:
#                 ganador = True

#         if ganador:
#             print(f"Tenemos un ganador!! Felicidades {jugador_actual} por la victoria!")
#             juego_activo = False

#         empate = True
#         for i in range(3):
#             for j in range(3):
#                 if tablero[i][j] == "-":
#                     empate = False

#         if empate:
#             print("Es un empate, que aburrido")
#             juego_activo = False

#         if jugador_actual == "X":
#             jugador_actual = "O"
#         else:
#             jugador_actual = "X"

#     except:
#         print("Entrada invalida")


#Actividad 10

ventas = [
    [120, 150, 130, 160, 140, 180, 200],  # Producto 1
    [90, 110, 100, 120, 95, 130, 140],    # Producto 2
    [200, 180, 220, 210, 195, 240, 260],  # Producto 3
    [110, 130, 125, 115, 140, 150, 160]   # Producto 4
]

productos = ["Producto 1", "Producto 2", "Producto 3", "Producto 4"]
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

print("==== TOTAL VENDIDO POR PRODUCTO ====")
totales_productos = []
for i in range(len(ventas)):
    suma = 0
    for j in range(len(ventas[i])):
        suma = suma + ventas[i][j]
    totales_productos.append(suma)
    print(f"{productos[i]}: ${suma}")

print("==== VENTAS TOTALES POR DIA ====")
totales_dias = []
for j in range(len(dias)):
    suma = 0
    for i in range(len(ventas)):
        suma = suma + ventas[i][j]
    totales_dias.append(suma)
    print(f"{dias[j]}: ${suma}")

mayor_venta_dia = totales_dias[0]
indice_mayor_dia = 0
for j in range(len(totales_dias)):
    if totales_dias[j] > mayor_venta_dia:
        mayor_venta_dia = totales_dias[j]
        indice_mayor_dia = j

print(f"El dia con mayor ventas fue: {dias[indice_mayor_dia]} (${mayor_venta_dia})")

mayor_venta_producto = totales_productos[0]
indice_mayor_producto = 0
for i in range(len(totales_productos)):
    if totales_productos[i] > mayor_venta_producto:
        mayor_venta_producto = totales_productos[i]
        indice_mayor_producto = i

print(f"Producto más vendido fue: {productos[indice_mayor_producto]} (${mayor_venta_producto})")