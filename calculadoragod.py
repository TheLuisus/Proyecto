import colorama
from colorama import Fore

colorama.init()
print(Fore.YELLOW + "-----------------------------------------")

print("¡hola! Bienbenido a la " +
      Fore.BLUE + "CALCULADORA" + Fore.RED + "GOD" + Fore.YELLOW + ".")
print("-----------------------------------------")
print(Fore.YELLOW + "para salir, solo escribe" +
      Fore.RED + " salir" + Fore.YELLOW + ". \n")
print(Fore.YELLOW + "la operaciones de esta calculadora son: suma, resta, multiplicacion y division.")


while True:
    try:
        n1 = input(Fore.CYAN + "ingresa el primer numero: ")
        if n1.lower() == "salir":
            print("adios")
            break
        n1 = int(n1)

        op = input(Fore.GREEN + "ingresa la operacion: ")
        if op.lower() == "salir":
            print("adios")
            break
        n2 = input(Fore.LIGHTBLACK_EX + "ingresa el siguiente numero: ")
        if n2.lower() == "salir":
            print("adios")
            break
        n2 = int(n2)

        if op.lower() == "suma":
            op = n1 + n2
        elif op.lower() == "resta":
            op = n1 - n2
        elif op.lower() == "multiplicacion" or op.lower() == "multiplicación":
            op = n1 * n2
        elif op.lower() == "division" or op.lower() == "divisíon":
            op = n1 / n2
        else:
            print("la operación operacion que ingresaste no existe en este programa.")
            break

        print(Fore.BLUE + "el resultado de tu operación es: " + Fore.RED + str(op))

        print(Fore.YELLOW + "en la siguiente pregunta responde solo " + Fore.GREEN +
              "si " + Fore.YELLOW + "o " + Fore.RED + "no")
        ri = input(Fore.YELLOW + "¿quieres seguir utilizando la " +
                   Fore.BLUE + "CALCULADORA" + Fore.RED + "GOD" + Fore.YELLOW + "?")

        print(ri)
        if ri.lower() != "si":
            print("gracias por utilizar la " + Fore.BLUE +
                  "CALCULADORA" + Fore.RED + "GOD" + Fore.YELLOW + ".")
            break

    except ValueError:
        print("solo tienes que ingresar numeros enteros.")
    except ZeroDivisionError:
          print("no puedes dividir por 0...")
