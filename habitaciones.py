from datos import habitaciones, leer_texto, leer_entero, leer_decimal, leer_opcion, pausar, dinero


def registrar_habitacion():
    numero = leer_texto("Número o código de habitación: ")
    if numero in habitaciones:
        print("Ya existe una habitación con ese código.")
        return
    print("Tipos: 1. Individual  2. Doble  3. Matrimonial  4. Familiar  5. Suite")
    tipos = {"1": "Individual", "2": "Doble", "3": "Matrimonial", "4": "Familiar", "5": "Suite"}
    tipo = tipos[leer_opcion("Seleccione el tipo (1-5): ", tipos.keys())]
    capacidad = leer_entero("Capacidad de huéspedes: ", 1)
    precio = leer_decimal("Precio por noche en quetzales: ", 0.01)
    habitaciones[numero] = {
        "tipo": tipo, "capacidad": capacidad, "precio": precio,
        "activa": True
    }
    print("Habitación registrada correctamente.")


def listar_habitaciones():
    if not habitaciones:
        print("Todavía no hay habitaciones registradas.")
        return
    print("\n--- HABITACIONES ---")
    for numero, h in habitaciones.items():
        estado = "Disponible para reservar" if h["activa"] else "Inhabilitada"
        print(f"Habitación {numero} | Tipo: {h['tipo']} | Capacidad: {h['capacidad']} | Precio/noche: {dinero(h['precio'])} | {estado}")


def modificar_habitacion():
    listar_habitaciones()
    if not habitaciones:
        return
    numero = input("\nCódigo de la habitación que desea modificar: ").strip()
    if numero not in habitaciones:
        print("No existe esa habitación.")
        return
    h = habitaciones[numero]
    print("Deje un campo vacío para conservar su valor actual.")
    nuevo_tipo = input(f"Tipo actual [{h['tipo']}]: ").strip()
    if nuevo_tipo:
        tipos_validos = ["Individual", "Doble", "Matrimonial", "Familiar", "Suite"]
        coincidencia = next((t for t in tipos_validos if t.lower() == nuevo_tipo.lower()), None)
        if coincidencia is None:
            print("Tipo inválido. No se modificó la habitación.")
            return
        h["tipo"] = coincidencia

    nueva_capacidad = input(f"Capacidad actual [{h['capacidad']}]: ").strip()
    if nueva_capacidad:
        try:
            capacidad = int(nueva_capacidad)
            if capacidad < 1:
                raise ValueError
            h["capacidad"] = capacidad
        except ValueError:
            print("Capacidad inválida. No se modificó ese dato.")
            return

    nuevo_precio = input(f"Precio actual [{h['precio']:.2f}]: ").strip().replace(",", ".")
    if nuevo_precio:
        try:
            precio = float(nuevo_precio)
            if precio <= 0:
                raise ValueError
            h["precio"] = precio
        except ValueError:
            print("Precio inválido. No se modificó ese dato.")
            return

    estado = input("¿Habitación habilitada? (s/n; vacío conserva): ").strip().lower()
    if estado in ("s", "n"):
        h["activa"] = estado == "s"
    elif estado:
        print("Respuesta inválida; se conservó el estado anterior.")
    print("Proceso de modificación finalizado.")


def menu_habitaciones():
    while True:
        print("\n--- GESTIÓN DE HABITACIONES ---")
        print("1. Registrar habitación")
        print("2. Listar habitaciones")
        print("3. Modificar habitación")
        print("4. Volver al menú principal")
        op = input("Seleccione (1-4): ").strip()
        if op == "1":
            registrar_habitacion()
            pausar()
        elif op == "2":
            listar_habitaciones()
            pausar()
        elif op == "3":
            modificar_habitacion()
            pausar()
        elif op == "4":
            break
        else:
            print("Opción inválida. Escriba un número del 1 al 4.")
            pausar()
