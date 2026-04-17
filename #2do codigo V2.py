#2do codigo V2.2

print("      *** CALCULADORA ***")
print ("Escribe 'Salir' para finalizar\n")

while True:
    numeros = input("Ingresar: ").lower()
    if numeros == "salir":
        print("\nhasta luego")
        break

    try:
        resultado = eval(numeros)
        print(f"Resultado: {resultado}")
    except NameError:
        print("Error: texto invalido.")
    except SyntaxError:
       print("Error: operacion invalida.")
    except ZeroDivisionError:
        print("Error: No se puede dividir entre cero.")