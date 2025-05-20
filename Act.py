# Elabora un programa en  Python que pida al usuario un número, una operación (+, -, *, /) y un segundo número.
# A partir de esto, debe mostrar el resultado de la correspondiente operación.
# Se deben considerar excepciones para si teclea un dato no numérico, se divide entre cero, operaciones invalidas casos similares.
# En caso de suceder excepciones, el programa deberá mostrar un aviso y volver a pedirlo, en vez de interrumpir la ejecución.

while True:  # Se usa un bucle infinito para seguir pidiendo datos hasta que todo esté correcto
    try:
        # Se solicita al usuario que ingrese el primer número
        num1 = float(input("Ingresa el primer número: "))  # Puede lanzar ValueError si el usuario no ingresa un número válido

        # Se solicita la operación a realizar
        operacion = input("Ingresa la operación (+, -, *, /): ")
        if operacion not in ['+', '-', '*', '/']:
            # Si el usuario escribe una operación inválida, se lanza una excepción ValueError personalizada
            raise ValueError("Operación no válida")  

        # Se solicita el segundo número
        num2 = float(input("Ingresa el segundo número: "))  # También puede lanzar ValueError si no es un número

        # Se realiza la operación seleccionada por el usuario
        if operacion == '+':
            resultado = num1 + num2
        elif operacion == '-':
            resultado = num1 - num2
        elif operacion == '*':
            resultado = num1 * num2
        elif operacion == '/':
            if num2 == 0:
                # Se lanza una excepción si el usuario intenta dividir entre cero
                raise ZeroDivisionError("No se puede dividir entre cero")
            resultado = num1 / num2

        # Si todo sale bien, se muestra el resultado
        print(f"Resultado: {resultado}")
        break  # Se rompe el ciclo para salir del programa

    # Manejo de errores:

    except ValueError as ve:
        # Captura errores cuando el usuario introduce algo que no es un número o una operación inválida
        print(f"Error: {ve}. Intenta de nuevo.")
    
    except ZeroDivisionError as zde:
        # Captura el error específico cuando se intenta dividir entre cero
        print(f"Error: {zde}. Intenta de nuevo.")
    
    except Exception as e:
        # Captura cualquier otro tipo de error no previsto (como errores internos del sistema o de otro tipo)
        print(f"Ocurrió un error inesperado: {e}. Intenta de nuevo.")
