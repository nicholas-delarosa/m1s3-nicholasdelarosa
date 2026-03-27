# Sistema de Inventario

Sistema de gestión de inventario por consola escrito en Python. Permite agregar, buscar, actualizar y eliminar productos, calcular estadísticas del stock, y exportar o importar datos desde archivos CSV.

---

## Estructura del proyecto

```
├── main.py        # Punto de entrada — menú principal y flujo de la app
├── servicios.py   # Lógica de negocio (CRUD + estadísticas)
├── archivos.py    # Lectura y escritura de archivos CSV
└── README.md
```

---

## Cómo ejecutar

Requiere **Python 3.8 o superior**. No necesita dependencias externas.

```bash
python main.py
```

---

## Menú principal

Al ejecutar el programa se muestra el siguiente menú en un bucle continuo:

```
═════════════════════════════════════════════
        SISTEMA DE INVENTARIO
═════════════════════════════════════════════
  [1]  Agregar producto
  [2]  Mostrar inventario
  [3]  Buscar producto
  [4]  Actualizar producto
  [5]  Eliminar producto
  [6]  Estadísticas
  [7]  Guardar CSV
  [8]  Cargar CSV
  [9]  Salir
═════════════════════════════════════════════
```

El menú se repite hasta que el usuario seleccione **9 — Salir**. Las opciones inválidas muestran un mensaje de error y vuelven al menú sin cerrar el programa.

---

## Funcionalidades

### 1 — Agregar producto
Solicita nombre, precio y cantidad. El nombre no puede estar vacío. Tras agregar un producto, pregunta si se desea agregar otro sin volver al menú.

### 2 — Mostrar inventario
Muestra todos los productos en una tabla alineada con columnas de ancho fijo:

```
  ──────────────────────────────────────────────────
  #   Nombre                      Precio    Cantidad
  ──────────────────────────────────────────────────
  1   Lápiz                        $500.00      3 uds.
  2   Cuaderno                   $1200.00     10 uds.
  ──────────────────────────────────────────────────
```

Si el inventario está vacío, lo indica con un mensaje.

### 3 — Buscar producto
Busca por nombre exacto (sin distinción de mayúsculas). Si no se encuentra, ofrece la opción de buscar otro sin volver al menú.

### 4 — Actualizar producto
Permite modificar el precio y/o la cantidad de un producto existente. Cada campo es opcional: presionar Enter lo omite. Si el producto no existe, ofrece reintentar con otro nombre.

### 5 — Eliminar producto
Elimina un producto por nombre. Si no se encuentra, ofrece reintentar antes de volver al menú.

### 6 — Estadísticas
Muestra un resumen del estado del inventario:

- Total de productos registrados
- Unidades totales en stock
- Valor total del inventario (precio × cantidad)
- Producto más caro
- Producto con mayor stock

### 7 — Guardar CSV
Exporta el inventario a un archivo `.csv`. Si no se escribe la extensión, el sistema la agrega automáticamente (nunca genera `.csv.csv`). El archivo incluye encabezado `nombre,precio,cantidad`.

### 8 — Cargar CSV
Importa productos desde un archivo `.csv` con el formato esperado. La carga se muestra fila a fila en consola, marcando cada producto con `✔` o `✘` según sea válido. Al terminar, el usuario elige si **sobrescribir** el inventario o **fusionarlo** con el existente:

- Si el producto ya existe → actualiza precio y suma cantidad.
- Si no existe → lo agrega.

---

## Formato del CSV

El archivo debe tener exactamente este encabezado en la primera fila:

```
nombre,precio,cantidad
```

Ejemplo válido:

```csv
nombre,precio,cantidad
Lápiz,500,3
Cuaderno,1200,10
Borrador,150,25
```

Filas con datos faltantes, tipos incorrectos o valores negativos son omitidas durante la carga y contabilizadas en el resumen final.

---

## Módulos

### `main.py`
Contiene el bucle principal del programa, el menú, y las funciones auxiliares de entrada (`pedir_nombre`, `pedir_float`, `pedir_int`) que validan y repiten la solicitud hasta recibir un valor válido. También maneja la limpieza de pantalla entre operaciones.

### `servicios.py`
Contiene toda la lógica que opera sobre el inventario (una lista de diccionarios):

| Función | Descripción |
|---|---|
| `agregar_producto` | Agrega un dict `{nombre, precio, cantidad}` a la lista |
| `mostrar_inventario` | Imprime la tabla del inventario |
| `buscar_producto` | Retorna el producto por nombre o `None` |
| `actualizar_producto` | Modifica precio y/o cantidad de un producto existente |
| `eliminar_producto` | Elimina un producto de la lista |
| `calcular_estadisticas` | Imprime resumen estadístico del inventario |

### `archivos.py`
Maneja la persistencia en disco:

| Función | Descripción |
|---|---|
| `guardar_csv` | Escribe el inventario en un `.csv` con encabezado |
| `cargar_csv` | Lee un `.csv`, valida cada fila y retorna la lista cargada |

---

## Validaciones

- Nombres vacíos son rechazados en todos los campos de nombre.
- Precios y cantidades negativos o no numéricos son rechazados con mensaje y reintento automático.
- Al cargar un CSV, filas con estructura o valores inválidos son omitidas sin interrumpir la carga.
- El archivo CSV debe tener exactamente el encabezado `nombre,precio,cantidad`; de lo contrario la carga se cancela.

---

## Estructura de datos

Cada producto se almacena como un diccionario dentro de la lista `inventario`:

```python
inventario = [
    {"nombre": "Lápiz",    "precio": 500.0,  "cantidad": 3},
    {"nombre": "Cuaderno", "precio": 1200.0, "cantidad": 10},
]
```

Los datos **no persisten entre sesiones** a menos que se guarden manualmente con la opción 7 antes de salir.
