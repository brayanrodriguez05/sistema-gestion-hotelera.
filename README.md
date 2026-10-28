# Sistema de Reservaciones y Administración de Hotel

Proyecto de Python para el curso de Algoritmos.

## Requisitos
- Python 3 instalado.
- Visual Studio Code.
- No necesita instalar librerías externas.

## Ejecutar en Linux Mint
Abra una terminal en esta carpeta y ejecute:

```bash
python3 main.py
```

## Archivos
- `main.py`: carátula y menú principal.
- `datos.py`: datos compartidos, validaciones de entrada y funciones comunes.
- `huespedes.py`: registro, listado e historial de huéspedes.
- `habitaciones.py`: registro, consulta y modificación de habitaciones.
- `reservaciones.py`: disponibilidad, creación, modificación y cancelación.
- `pagos.py`: entrada/salida, pagos, cargos y estado de cuenta.

## Importante
Los datos se guardan en memoria mientras el programa está abierto. Al cerrarlo, los registros se reinician. Para una entrega que requiera persistencia, habría que añadir archivos o una base de datos.
