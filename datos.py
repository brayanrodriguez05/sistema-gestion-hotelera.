from datetime import datetime

# Datos guardados en memoria: se reinician al cerrar el programa.
huespedes = {}
habitaciones = {}
reservaciones = {}
pagos = {}
siguiente_huesped = 1
siguiente_reservacion = 1


def mostrar_caratula():
    print("\n" + "=" * 60)
    print("       UNIVERSIDAD MARIANO GÁLVEZ DE GUATEMALA")
    print("=" * 60)
    print("\n              FACULTAD DE INGENIERÍA")
    print("              EN SISTEMAS\n")
    print("Carrera: Ingeniería en Sistemas")
    print("Curso: Algoritmos")
    print("Proyecto: Sistema de Gestión Hotelera")
    print("\n" + "-" * 60)
    print("              INTEGRANTES DEL GRUPO")
    print("-" * 60)
    print("1. Brayan Emilio Rodríguez Gómez")
    print("2. Cesar Enrique Galindo Ajqui")
    print("3. Selvin Enrique Calderon Valiente")
    print("4. Oliver Osiel Lopez Guzman")
    print("\n" + "-" * 60)
    print("Docente: Demsshill Leonel Coutiveo Sandoval")
    print("Fecha: 30 de octubre de 2026")
    print("=" * 60)
    input("\nPresione Enter para ingresar al sistema...")


def pausar():
    input("\nPresione Enter para continuar...")


def leer_texto(mensaje):
    while True:
        valor = input(mensaje).strip()
        if valor:
            return valor
        print("Entrada inválida. No deje el campo vacío.")


def leer_entero(mensaje, minimo=1):
    while True:
        valor = input(mensaje).strip()
        try:
            numero = int(valor)
            if numero >= minimo:
                return numero
            print(f"El valor debe ser como mínimo {minimo}.")
        except ValueError:
            print("Entrada inválida. Escriba un número entero.")


def leer_decimal(mensaje, minimo=0):
    while True:
        valor = input(mensaje).strip().replace(",", ".")
        try:
            numero = float(valor)
            if numero >= minimo:
                return numero
            print(f"El valor debe ser como mínimo {minimo}.")
        except ValueError:
            print("Entrada inválida. Escriba una cantidad numérica.")


def leer_fecha(mensaje):
    while True:
        valor = input(mensaje).strip()
        try:
            fecha = datetime.strptime(valor, "%Y-%m-%d").date()
            return fecha
        except ValueError:
            print("Fecha inválida. Use el formato AAAA-MM-DD, por ejemplo 2026-10-30.")


def leer_opcion(mensaje, opciones):
    opciones_limpias = [str(x) for x in opciones]
    while True:
        valor = input(mensaje).strip()
        if valor in opciones_limpias:
            return valor
        print("Opción inválida. Valores permitidos: " + ", ".join(opciones_limpias))


def dinero(cantidad):
    return f"Q{cantidad:,.2f}"
