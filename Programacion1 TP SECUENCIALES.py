#Primer ejercicio
print("Hola Mundo")

#Segundo ejercicio

nombre = input("Ingrese su nombre: ")

print("Hola", nombre)

#Tercer ejercicio

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
residencia = input("Ingrese su residencia: ")

print(f"Soy", nombre, apellido, "tengo", edad, "años y vivo en", residencia)

#Cuarto ejercicio

radio = float(input("Ingrese el radio: "))
area = 3.1416 * (radio ** 2)
perimetro = 2 * radio
print(f"el area del circulo es", area, "y su perimetro es", perimetro)

#Quinto ejercicio

segundos = int(input("Ingrese los segundos: "))
horas = segundos / 3600
print(f"Los segundos equivalen a", horas, "horas")

#Sexto ejercicio

numero = int(input("Ingrese un número: "))

print(f"Tabla de multiplicar del {numero}:")
print(f"{numero} x 1 = {numero * 1}")
print(f"{numero} x 2 = {numero * 2}")
print(f"{numero} x 3 = {numero * 3}")
print(f"{numero} x 4 = {numero * 4}")
print(f"{numero} x 5 = {numero * 5}")
print(f"{numero} x 6 = {numero * 6}")
print(f"{numero} x 7 = {numero * 7}")
print(f"{numero} x 8 = {numero * 8}")
print(f"{numero} x 9 = {numero * 9}")
print(f"{numero} x 10 = {numero * 10}")

#Septimo ejercicio

num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))
print(f"La suma es {num1 + num2}, la resta es {num1 - num2} y la multiplicacion {num1 * num2}")

#Octavo ejercicio

peso = float(input("Ingrese su peso: "))
altura = float(input("Ingrese su altura: "))
imc = peso / (altura ** 2)
print(f"su IMC es {imc}")

#Noveno ejercicio

celsius = float(input("Ingrese los grados Celsius: "))
farenheit = (celsius * 9/5) + 32
print(f"Los grados celsius equivalen a {farenheit} grados farenheit")

#Decimo Ejercicio

numPromedio1 = int(input("Ingrese el primer numero: "))
numPromedio2 = int(input("Ingrese el segundo numero: "))
numPromedio3 = int(input("Ingrese el tercer numero: "))
promedio = (numPromedio1 + numPromedio2 + numPromedio3) / 3
print(f"El promedio es {promedio}")