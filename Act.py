# Elabora un programa en  Python que pida al usuario un número, una operación (+, -, *, /) y un segundo número.
# A partir de esto, debe mostrar el resultado de la correspondiente operación.
# Se deben considerar excepciones para si teclea un dato no numérico, se divide entre cero, operaciones invalidas casos similares.
# En caso de suceder excepciones, el programa deberá mostrar un aviso y volver a pedirlo, en vez de interrumpir la ejecución.

while True:
    try:
        # Se pide el primer número
        num1 = float(input("Ingresa el primer número: "))
        
        # Se pide la operación
        operacion = input("Ingresa la operación (+, -, *, /): ")
        if operacion not in ['+', '-', '*', '/']:
            raise ValueError("Operación no válida")
        
        # Se pide el segundo número
        num2 = float(input("Ingresa el segundo número: "))
        
        # Se realiza la operación correspondiente
        if operacion == '+':
            resultado = num1 + num2
        elif operacion == '-':
            resultado = num1 - num2
        elif operacion == '*':
            resultado = num1 * num2
        elif operacion == '/':
            if num2 == 0:
                raise ZeroDivisionError("No se puede dividir entre cero")
            resultado = num1 / num2
        
        # Se muestra el resultado
        print(f"Resultado: {resultado}")
        break  # Se rompe el ciclo si todo sale bien

    except ValueError as ve:
        print(f"Error: {ve}. Intenta de nuevo.")
    except ZeroDivisionError as zde:
        print(f"Error: {zde}. Intenta de nuevo.")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}. Intenta de nuevo.")