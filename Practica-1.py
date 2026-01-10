num1 = 4
num2 = 4

resultado = 0
operacion = ""

contador = 0
while contador < num2:
    resultado += num1
    operacion += str(num1) + " + "
    contador += 1

print("Operacion:", operacion)
print("Resultado:", resultado)
