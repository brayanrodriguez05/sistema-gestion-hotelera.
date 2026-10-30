from datos import reservaciones, huespedes, pagos, leer_decimal, leer_entero, leer_opcion, leer_texto, pausar, dinero


def seleccionar_reservacion():
    if not reservaciones:
        print("No hay reservaciones registradas.")
        return None
    print("\n--- RESERVACIONES ---")
    for codigo, r in reservaciones.items():
        nombre = huespedes.get(r["huesped_id"], {}).get("nombre", "Desconocido")
        print(f"{codigo}. {nombre} | Habitación {r['habitacion']} | Estado: {r['estado']} | Total: {dinero(r['total'] + r['cargos'])}")
    codigo = leer_entero("Código de reservación: ", 1)
    if codigo not in reservaciones:
        print("No existe esa reservación.")
        return None
    return codigo


def registrar_entrada():
    codigo = seleccionar_reservacion()
    if codigo is None:
        return
    r = reservaciones[codigo]
    if r["estado"] != "Reservada":
        print("Solo se puede registrar entrada a una reservación en estado 'Reservada'.")
        return
    r["estado"] = "Ocupada"
    print("Entrada del huésped registrada. Estado: Ocupada.")


def registrar_salida():
    codigo = seleccionar_reservacion()
    if codigo is None:
        return
    r = reservaciones[codigo]
    if r["estado"] != "Ocupada":
        print("Solo se puede registrar salida si la habitación está ocupada.")
        return
    r["estado"] = "Finalizada"
    print("Salida registrada. Estado: Finalizada.")


def agregar_cargo():
    codigo = seleccionar_reservacion()
    if codigo is None:
        return
    r = reservaciones[codigo]
    if r["estado"] in ("Cancelada", "Finalizada"):
        print("No se pueden agregar cargos a una reservación cancelada o finalizada.")
        return
    descripcion = leer_texto("Descripción del cargo adicional: ")
    cargo = leer_decimal("Monto del cargo en quetzales: ", 0.01)
    r["cargos"] += cargo
    print(f"Cargo agregado: {descripcion} — {dinero(cargo)}")
    print(f"Nuevo total: {dinero(r['total'] + r['cargos'])}")


def registrar_pago():
    codigo = seleccionar_reservacion()
    if codigo is None:
        return
    r = reservaciones[codigo]
    if r["estado"] == "Cancelada":
        print("No se pueden registrar pagos para una reservación cancelada.")
        return
    total = r["total"] + r["cargos"]
    pagado = sum(p["monto"] for p in pagos.get(codigo, []))
    pendiente = total - pagado
    if pendiente <= 0:
        print("La reservación ya está pagada por completo.")
        return
    print(f"Total actual: {dinero(total)} | Pagado: {dinero(pagado)} | Pendiente: {dinero(pendiente)}")
    monto = leer_decimal("Monto a registrar: Q", 0.01)
    if monto > pendiente:
        print("El pago no puede superar el saldo pendiente.")
        return
    print("Métodos: 1. Efectivo  2. Tarjeta  3. Transferencia")
    metodos = {"1": "Efectivo", "2": "Tarjeta", "3": "Transferencia"}
    metodo = metodos[leer_opcion("Seleccione método (1-3): ", metodos.keys())]
    pagos.setdefault(codigo, []).append({"monto": monto, "metodo": metodo})
    print(f"Pago registrado: {dinero(monto)} por {metodo}. Saldo pendiente: {dinero(pendiente - monto)}")


def ver_estado_cuenta():
    codigo = seleccionar_reservacion()
    if codigo is None:
        return
    r = reservaciones[codigo]
    total = r["total"] + r["cargos"]
    pagado = sum(p["monto"] for p in pagos.get(codigo, []))
    print("\n--- ESTADO DE CUENTA ---")
    print(f"Reservación: {codigo}")
    print(f"Total alojamiento/servicios menos descuento: {dinero(r['total'])}")
    print(f"Cargos adicionales: {dinero(r['cargos'])}")
    print(f"Total final: {dinero(total)}")
    print(f"Pagado: {dinero(pagado)}")
    print(f"Saldo pendiente: {dinero(max(0, total - pagado))}")
    if pagos.get(codigo):
        print("Pagos:")
        for p in pagos[codigo]:
            print(f"- {dinero(p['monto'])} | {p['metodo']}")


def menu_pagos():
    while True:
        print("\n--- ESTADÍA, PAGOS Y CARGOS ---")
        print("1. Registrar entrada del huésped")
        print("2. Registrar salida")
        print("3. Registrar pago")
        print("4. Aplicar cargo adicional")
        print("5. Consultar estado de cuenta")
        print("6. Volver al menú principal")
        op = input("Seleccione (1-6): ").strip()
        if op == "1":
            registrar_entrada()
            pausar()
        elif op == "2":
            registrar_salida()
            pausar()
        elif op == "3":
            registrar_pago()
            pausar()
        elif op == "4":
            agregar_cargo()
            pausar()
        elif op == "5":
            ver_estado_cuenta()
            pausar()
        elif op == "6":
            break
        else:
            print("Opción inválida. Escriba un número del 1 al 6.")
            pausar()
