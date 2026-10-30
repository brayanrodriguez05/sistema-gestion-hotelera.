from datos import huespedes, reservaciones, leer_solo_letras, leer_digitos, leer_entero, pausar


def registrar_huesped():
    global_dummy = None
    from datos import siguiente_huesped
    # Se actualiza el contador del módulo datos mediante asignación explícita.
    import datos
    nombre = leer_solo_letras("Nombre completo: ")
    documento = leer_digitos("DPI (13 dígitos): ", 13)
    telefono = leer_digitos("Teléfono (8 dígitos): ", 8)
    correo = input("Correo electrónico (opcional): ").strip()

    for existente in huespedes.values():
        if existente["documento"].lower() == documento.lower():
            print("Ya existe un huésped con ese documento.")
            return

    codigo = datos.siguiente_huesped
    datos.siguiente_huesped += 1
    huespedes[codigo] = {
        "nombre": nombre, "documento": documento,
        "telefono": telefono, "correo": correo
    }
    print(f"Huésped registrado correctamente. Código: {codigo}")


def listar_huespedes():
    if not huespedes:
        print("Todavía no hay huéspedes registrados.")
        return
    print("\n--- LISTADO DE HUÉSPEDES ---")
    for codigo, h in huespedes.items():
        print(f"Código: {codigo} | Nombre: {h['nombre']} | Documento: {h['documento']} | Teléfono: {h['telefono']}")


def consultar_historial():
    if not huespedes:
        print("No hay huéspedes registrados.")
        return
    listar_huespedes()

    codigo = leer_entero("\nCódigo del huésped: ", 1)

    if codigo not in huespedes:
        print("No existe un huésped con ese código.")
        return

        print(f"\nHistorial de {huespedes[codigo]['nombre']}:")
    encontrados = [r for r in reservaciones.values() if r["huesped_id"] == codigo]
    if not encontrados:
        print("Este huésped aún no tiene reservaciones.")
        return
    for r in encontrados:
        print(f"Reserva {r['codigo']} | Habitación {r['habitacion']} | {r['entrada']} a {r['salida']} | Estado: {r['estado']} | Total: Q{r['total']:.2f}")


def menu_huespedes():
    while True:
        print("\n--- GESTIÓN DE HUÉSPEDES ---")
        print("1. Registrar huésped")
        print("2. Listar huéspedes")
        print("3. Consultar historial de un huésped")
        print("4. Volver al menú principal")
        op = input("Seleccione (1-4): ").strip()
        if op == "1":
            registrar_huesped()
            pausar()
        elif op == "2":
            listar_huespedes()
            pausar()
        elif op == "3":
            consultar_historial()
            pausar()
        elif op == "4":
            break
        else:
            print("Opción inválida. Escriba un número del 1 al 4.")
            pausar()
