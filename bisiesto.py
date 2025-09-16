"""
El programa determina si un año es bisiesto, bisisiesto quiere decir si es divisible entre 4, pero no entre 100, excepto que sea 
divisible entre 400
"""

# Declaraciones

# Entradas
año = int(input("Introduce el año: "))

# Proceso
if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
    resultado = "sí"
else:
    resultado = "no"

# Salidas
print(resultado)
