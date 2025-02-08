# Programa para sumar dos números en Python

def sumar_dos_numeros(a, b):
    return a + b

# Solicitar al usuario que ingrese dos números
numero1 = float(input("Ingresa el primer número: "))
numero2 = float(input("Ingresa el segundo número: "))

# Sumar los números
resultado = sumar_dos_numeros(numero1, numero2)

# Mostrar el resultado
print("La suma de los dos números es:", resultado)