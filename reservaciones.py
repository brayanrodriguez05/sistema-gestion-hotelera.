from datos import (huespedes, habitaciones, reservaciones, leer_fecha,
                   leer_entero, leer_decimal, leer_opcion, pausar, dinero)


def hay_conflicto(habitacion, entrada, salida, ignorar_codigo=None):
    for codigo, r in reservaciones.items():
        if codigo == ignorar_codigo or r["habitacion"] != habitacion:
            continue
        if r["estado"] == "Cancelada":
            continue
        # Dos periodos chocan si la nueva entrada es anterior a la salida existente
        # y la nueva salida es posterior a la entrada existente.
        if entrada < r["salida"] and salida > r["entrada"]:
            return True
    return False


def consultar_disponibilidad(entrada=None, salida=None):
    if entrada is None:
        entrada = leer_fecha("Fecha de entrada (AAAA-MM-DD): ")
        salida = leer_fecha("Fecha de salida (AAAA-MM-DD): ")
    if salida <= entrada:
        print("La salida debe ser posterior a la entrada.")
        return
    disponibles = []
    for numero, h in habitaciones.items():
        if h["activa"] and not hay_conflicto(numero, entrada, salida):
            disponibles.append((numero, h))
    if not disponibles:
        print("No hay habitaciones disponibles para ese periodo.")
        return
    print("\nHabitaciones disponibles:")
    for numero, h in disponibles:
        print(f"{numero} | {h['tipo']} | Capacidad: {h['capacidad']} | {dinero(h['precio'])} por noche")


def crear_reservacion():
    import datos
    if not huespedes:
        print("Primero debe registrar al menos un huésped.")
        return
    if not habitaciones:
        print("Primero debe registrar al menos una habitación.")
        return

    print("\n--- HUÉSPEDES REGISTRADOS ---")
    for codigo, h in huespedes.items():
        print(f"{codigo}. {h['nombre']} ({h['documento']})")
    huesped_id = leer_entero("Código del huésped: ", 1)
    if huesped_id not in huespedes:
        print("El huésped seleccionado no existe.")
        return

    entrada = leer_fecha("Fecha de entrada (AAAA-MM-DD): ")
    salida = leer_fecha("Fecha de salida (AAAA-MM-DD): ")
    if salida <= entrada:
        print("La salida debe ser posterior a la entrada.")
        return

    consultar_disponibilidad(entrada, salida)
    habitacion = input("Escriba el código de la habitación que desea reservar: ").strip()
    if habitacion not in habitaciones:
        print("La habitación indicada no existe.")
        return
    h = habitaciones[habitacion]
    if not h["activa"]:
        print("Esta habitación está inhabilitada.")
        return
    if hay_conflicto(habitacion, entrada, salida):
        print("No se puede reservar: la habitación ya está reservada u ocupada en esas fechas.")
        return

    huespedes_cantidad = leer_entero("Cantidad de huéspedes: ", 1)
    if huespedes_cantidad > h["capacidad"]:
        print(f"La habitación solo permite {h['capacidad']} huésped(es).")
        return

    noches = (salida - entrada).days
    servicios = leer_decimal("Costo total de servicios adicionales (Q; 0 si ninguno): ", 0)
    descuento = leer_decimal("Descuento en quetzales (Q; 0 si ninguno): ", 0)
    subtotal = noches * h["precio"] + servicios
    if descuento > subtotal:
        print("El descuento no puede superar el subtotal.")
        return
    total = subtotal - descuento

    codigo = datos.siguiente_reservacion
    datos.siguiente_reservacion += 1
    reservaciones[codigo] = {
        "codigo": codigo, "huesped_id": huesped_id, "habitacion": habitacion,
        "entrada": entrada, "salida": salida, "noches": noches,
        "servicios": servicios, "descuento": descuento, "total": total,
        "estado": "Reservada", "cantidad_huespedes": huespedes_cantidad,
        "cargos": 0.0
    }
    print(f"Reservación creada. Código: {codigo}")
    print(f"Noches: {noches} | Total estimado: {dinero(total)}")


def listar_reservaciones():
    if not reservaciones:
        print("Todavía no hay reservaciones.")
        return
    print("\n--- RESERVACIONES ---")
    for codigo, r in reservaciones.items():
        nombre = huespedes.get(r["huesped_id"], {}).get("nombre", "Huésped desconocido")
        print(f"Código {codigo} | {nombre} | Habitación {r['habitacion']} | {r['entrada']} a {r['salida']} | Estado: {r['estado']} | Total: {dinero(r['total'] + r['cargos'])}")


def obtener_codigo():
    listar_reservaciones()
    if not reservaciones:
        return None
    try:
        codigo = int(input("Código de reservación: ").strip())
    except ValueError:
        print("El código debe ser un número entero.")
        return None
    if codigo not in reservaciones:
        print("No existe esa reservación.")
        return None
    return codigo


def modificar_reservacion():
    codigo = obtener_codigo()
    if codigo is None:
        return
    r = reservaciones[codigo]
    if r["estado"] in ("Cancelada", "Finalizada"):
        print("No se puede modificar una reservación cancelada o finalizada.")
        return
    nueva_entrada = leer_fecha("Nueva fecha de entrada (AAAA-MM-DD): ")
    nueva_salida = leer_fecha("Nueva fecha de salida (AAAA-MM-DD): ")
    if nueva_salida <= nueva_entrada:
        print("La salida debe ser posterior a la entrada.")
        return
    if hay_conflicto(r["habitacion"], nueva_entrada, nueva_salida, codigo):
        print("Las fechas se cruzan con otra reservación de esa habitación.")
        return
    h = habitaciones[r["habitacion"]]
    noches = (nueva_salida - nueva_entrada).days
    subtotal = noches * h["precio"] + r["servicios"]

    if r["descuento"] > subtotal:
        print("El descuento no puede superar el nuevo subtotal.")
        return

    r["entrada"], r["salida"], r["noches"] = nueva_entrada, nueva_salida, noches
    r["total"] = subtotal - r["descuento"]
    print("Reservación modificada correctamente.")
    print(f"Nuevo total estimado: {dinero(r['total'] + r['cargos'])}")


def cancelar_reservacion():
    codigo = obtener_codigo()
    if codigo is None:
        return
    r = reservaciones[codigo]
    if r["estado"] in ("Cancelada", "Finalizada"):
        print("La reservación ya está cancelada o finalizada.")
        return
    r["estado"] = "Cancelada"
    print("Reservación cancelada correctamente.")


def menu_reservaciones():
    while True:
        print("\n--- RESERVACIONES Y DISPONIBILIDAD ---")
        print("1. Consultar disponibilidad")
        print("2. Crear reservación")
        print("3. Listar reservaciones")
        print("4. Modificar reservación")
        print("5. Cancelar reservación")
        print("6. Volver al menú principal")
        op = input("Seleccione (1-6): ").strip()
        if op == "1":
            consultar_disponibilidad()
            pausar()
        elif op == "2":
            crear_reservacion()
            pausar()
        elif op == "3":
            listar_reservaciones()
            pausar()
        elif op == "4":
            modificar_reservacion()
            pausar()
        elif op == "5":
            cancelar_reservacion()
            pausar()
        elif op == "6":
            break
        else:
            print("Opción inválida. Escriba un número del 1 al 6.")
            pausar()
