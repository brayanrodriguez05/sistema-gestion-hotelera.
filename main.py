from huespedes import menu_huespedes
from habitaciones import menu_habitaciones
from reservaciones import menu_reservaciones
from pagos import menu_pagos
from datos import mostrar_caratula, pausar


def menu_principal():
    mostrar_caratula()
    while True:
        print("\n" + "=" * 58)
        print("       SISTEMA DE RESERVACIONES Y ADMINISTRACIÓN")
        print("=" * 58)
        print("1. Gestión de huéspedes")
        print("2. Gestión de habitaciones")
        print("3. Reservaciones y disponibilidad")
        print("4. Estadía, pagos y cargos adicionales")
        print("5. Salir")
        opcion = input("Seleccione una opción (1-5): ").strip()

        if opcion == "1":
            menu_huespedes()
        elif opcion == "2":
            menu_habitaciones()
        elif opcion == "3":
            menu_reservaciones()
        elif opcion == "4":
            menu_pagos()
        elif opcion == "5":
            print("\nGracias por utilizar el sistema. ¡Hasta pronto!")
            break
        else:
            print("Opción inválida. Escriba un número del 1 al 5.")
            pausar()


if __name__ == "__main__":
    menu_principal()
