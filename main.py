# =========================================================
# TRABAJO PRÁCTICO INTEGRADOR
# Gestión de Datos de Países en Python
# =========================================================

# -----------------------------
# IMPORTACIÓN DE LIBRERÍAS
# -----------------------------
import csv


# =========================================================
# FUNCIÓN: LEER CSV
# =========================================================
# Esta función lee el archivo CSV y carga los países
# dentro de una lista de diccionarios.
# =========================================================

def leer_csv(nombre_archivo):

    paises = []

    try:
        with open(nombre_archivo, mode="r", encoding="utf-8") as archivo:

            lector = csv.DictReader(archivo)

            for fila in lector:

                try:
                    pais = {
                        "nombre": fila["nombre"],
                        "poblacion": int(fila["poblacion"]),
                        "superficie": int(fila["superficie"]),
                        "continente": fila["continente"]
                    }

                    paises.append(pais)

                except ValueError:
                    print("Error: formato inválido en una fila del CSV.")

    except FileNotFoundError:
        print("El archivo CSV no existe. Se creará uno nuevo.")

    return paises


# =========================================================
# FUNCIÓN: GUARDAR CSV
# =========================================================
# Guarda todos los datos actualizados en el archivo CSV.
# =========================================================

def guardar_csv(nombre_archivo, paises):

    with open(nombre_archivo, mode="w", newline="", encoding="utf-8") as archivo:

        campos = ["nombre", "poblacion", "superficie", "continente"]

        escritor = csv.DictWriter(archivo, fieldnames=campos)

        escritor.writeheader()

        for pais in paises:
            escritor.writerow(pais)

    print("Datos guardados correctamente.")


# =========================================================
# FUNCIÓN: MOSTRAR MENÚ
# =========================================================

def mostrar_menu():

    print("\n========== MENÚ ==========")
    print("1. Agregar país")
    print("2. Actualizar país")
    print("3. Buscar país")
    print("4. Filtrar países")
    print("5. Ordenar países")
    print("6. Mostrar estadísticas")
    print("7. Mostrar todos los países")
    print("0. Salir")
    print("===========================")


# =========================================================
# FUNCIÓN: AGREGAR PAÍS
# =========================================================

def agregar_pais(paises):

    print("\n--- AGREGAR PAÍS ---")

    # -----------------------------
    # VALIDAR NOMBRE
    # -----------------------------
    nombre = input("Ingrese el nombre del país: ").strip()

    while nombre == "":
        print("Error: el nombre no puede estar vacío.")
        nombre = input("Ingrese el nombre del país: ").strip()

    # -----------------------------
    # VALIDAR POBLACIÓN
    # -----------------------------
    poblacion = input("Ingrese la población: ")

    while not poblacion.isdigit():
        print("Error: debe ingresar números.")
        poblacion = input("Ingrese la población: ")

    # -----------------------------
    # VALIDAR SUPERFICIE
    # -----------------------------
    superficie = input("Ingrese la superficie en km²: ")

    while not superficie.isdigit():
        print("Error: debe ingresar números.")
        superficie = input("Ingrese la superficie en km²: ")

    # -----------------------------
    # VALIDAR CONTINENTE
    # -----------------------------
    continente = input("Ingrese el continente: ").strip()

    while continente == "":
        print("Error: el continente no puede estar vacío.")
        continente = input("Ingrese el continente: ").strip()

    # -----------------------------
    # CREAR DICCIONARIO
    # -----------------------------
    nuevo_pais = {
        "nombre": nombre,
        "poblacion": int(poblacion),
        "superficie": int(superficie),
        "continente": continente
    }

    # -----------------------------
    # AGREGAR A LA LISTA
    # -----------------------------
    paises.append(nuevo_pais)

    guardar_csv("paises.csv", paises)
    print("País agregado correctamente.")


# =========================================================
# FUNCIÓN: ACTUALIZAR PAÍS
# =========================================================

def actualizar_pais(paises):

    print("\n--- ACTUALIZAR PAÍS ---")

    nombre = input("Ingrese el país a actualizar: ").lower()

    encontrado = False

    for pais in paises:

        if pais["nombre"].lower() == nombre:

            nueva_poblacion = input("Nueva población: ")

            while not nueva_poblacion.isdigit():
                print("Error: ingrese números.")
                nueva_poblacion = input("Nueva población: ")

            nueva_superficie = input("Nueva superficie: ")

            while not nueva_superficie.isdigit():
                print("Error: ingrese números.")
                nueva_superficie = input("Nueva superficie: ")

            pais["poblacion"] = int(nueva_poblacion)
            pais["superficie"] = int(nueva_superficie)

            encontrado = True

            print("País actualizado correctamente.")

    if not encontrado:
        print("País no encontrado.")


# =========================================================
# FUNCIÓN: BUSCAR PAÍS
# =========================================================

def buscar_pais(paises):

    print("\n--- BUSCAR PAÍS ---")

    texto = input("Ingrese el nombre del país: ").lower()

    encontrados = []

    for pais in paises:

        if texto in pais["nombre"].lower():
            encontrados.append(pais)

    if len(encontrados) == 0:
        print("No se encontraron países.")

    else:
        print("\nRESULTADOS:")

        for pais in encontrados:

            print(f"""
Nombre: {pais["nombre"]}
Población: {pais["poblacion"]}
Superficie: {pais["superficie"]}
Continente: {pais["continente"]}
""")


# =========================================================
# FUNCIÓN: FILTRAR PAÍSES
# =========================================================

def filtrar_paises(paises):

    print("\n--- FILTRAR PAÍSES ---")

    print("1. Filtrar por continente")
    print("2. Filtrar por población")
    print("3. Filtrar por superficie")

    opcion = input("Seleccione una opción: ")

    # ---------------------------------------------------
    # FILTRAR POR CONTINENTE
    # ---------------------------------------------------
    if opcion == "1":

        continente = input("Ingrese continente: ").lower()

        encontrados = []

        for pais in paises:

            if pais["continente"].lower() == continente:
                encontrados.append(pais)

        if encontrados:

            for pais in encontrados:
                print(pais)

        else:
            print("No se encontraron países.")

    # ---------------------------------------------------
    # FILTRAR POR POBLACIÓN
    # ---------------------------------------------------
    elif opcion == "2":

        minimo = int(input("Ingrese población mínima: "))
        maximo = int(input("Ingrese población máxima: "))

        encontrados = []

        for pais in paises:

            if minimo <= pais["poblacion"] <= maximo:
                encontrados.append(pais)

        if encontrados:

            for pais in encontrados:
                print(pais)

        else:
            print("No se encontraron países.")

    # ---------------------------------------------------
    # FILTRAR POR SUPERFICIE
    # ---------------------------------------------------
    elif opcion == "3":

        minimo = int(input("Ingrese superficie mínima: "))
        maximo = int(input("Ingrese superficie máxima: "))

        encontrados = []

        for pais in paises:

            if minimo <= pais["superficie"] <= maximo:
                encontrados.append(pais)

        if encontrados:

            for pais in encontrados:
                print(pais)

        else:
            print("No se encontraron países.")

    else:
        print("Opción inválida.")


# =========================================================
# FUNCIÓN: ORDENAR PAÍSES
# =========================================================

def ordenar_paises(paises):

    print("\n--- ORDENAR PAÍSES ---")

    print("1. Nombre")
    print("2. Población")
    print("3. Superficie")

    opcion = input("Seleccione una opción: ")

    orden = input("Ascendente (A) o Descendente (D): ").upper()

    reverse = False

    if orden == "D":
        reverse = True

    # ---------------------------------------------------
    # ORDENAR POR NOMBRE
    # ---------------------------------------------------
    if opcion == "1":

        ordenados = sorted(
            paises,
            key=lambda pais: pais["nombre"],
            reverse=reverse
        )

    # ---------------------------------------------------
    # ORDENAR POR POBLACIÓN
    # ---------------------------------------------------
    elif opcion == "2":

        ordenados = sorted(
            paises,
            key=lambda pais: pais["poblacion"],
            reverse=reverse
        )

    # ---------------------------------------------------
    # ORDENAR POR SUPERFICIE
    # ---------------------------------------------------
    elif opcion == "3":

        ordenados = sorted(
            paises,
            key=lambda pais: pais["superficie"],
            reverse=reverse
        )

    else:
        print("Opción inválida.")
        return

    print("\nPAÍSES ORDENADOS:\n")

    for pais in ordenados:
        print(pais)


# =========================================================
# FUNCIÓN: MOSTRAR ESTADÍSTICAS
# =========================================================

def mostrar_estadisticas(paises):

    print("\n--- ESTADÍSTICAS ---")

    if len(paises) == 0:
        print("No hay países cargados.")
        return

    # ---------------------------------------------------
    # MAYOR POBLACIÓN
    # ---------------------------------------------------
    mayor = max(paises, key=lambda pais: pais["poblacion"])

    # ---------------------------------------------------
    # MENOR POBLACIÓN
    # ---------------------------------------------------
    menor = min(paises, key=lambda pais: pais["poblacion"])

    # ---------------------------------------------------
    # PROMEDIO POBLACIÓN
    # ---------------------------------------------------
    total_poblacion = 0

    for pais in paises:
        total_poblacion += pais["poblacion"]

    promedio_poblacion = total_poblacion / len(paises)

    # ---------------------------------------------------
    # PROMEDIO SUPERFICIE
    # ---------------------------------------------------
    total_superficie = 0

    for pais in paises:
        total_superficie += pais["superficie"]

    promedio_superficie = total_superficie / len(paises)

    # ---------------------------------------------------
    # CANTIDAD POR CONTINENTE
    # ---------------------------------------------------
    continentes = {}

    for pais in paises:

        continente = pais["continente"]

        if continente in continentes:
            continentes[continente] += 1

        else:
            continentes[continente] = 1

    # ---------------------------------------------------
    # MOSTRAR RESULTADOS
    # ---------------------------------------------------
    print(f"País con mayor población: {mayor['nombre']}")
    print(f"País con menor población: {menor['nombre']}")

    print(f"Promedio de población: {promedio_poblacion}")

    print(f"Promedio de superficie: {promedio_superficie}")

    print("\nCantidad de países por continente:")

    for continente, cantidad in continentes.items():
        print(f"{continente}: {cantidad}")


# =========================================================
# FUNCIÓN: MOSTRAR TODOS LOS PAÍSES
# =========================================================

def mostrar_todos(paises):

    print("\n--- LISTA DE PAÍSES ---")

    if len(paises) == 0:
        print("No hay países cargados.")

    else:

        for pais in paises:

            print(f"""
Nombre: {pais["nombre"]}
Población: {pais["poblacion"]}
Superficie: {pais["superficie"]}
Continente: {pais["continente"]}
""")


# =========================================================
# PROGRAMA PRINCIPAL
# =========================================================

ARCHIVO = "paises.csv"

# ---------------------------------------------------------
# CARGAR DATOS
# ---------------------------------------------------------
paises = leer_csv(ARCHIVO)

# ---------------------------------------------------------
# BUCLE PRINCIPAL
# ---------------------------------------------------------
while True:

    mostrar_menu()

    opcion = input("Seleccione una opción: ")

    # -----------------------------------------------------
    # OPCIÓN 1
    # -----------------------------------------------------
    if opcion == "1":
        agregar_pais(paises)

    # -----------------------------------------------------
    # OPCIÓN 2
    # -----------------------------------------------------
    elif opcion == "2":
        actualizar_pais(paises)

    # -----------------------------------------------------
    # OPCIÓN 3
    # -----------------------------------------------------
    elif opcion == "3":
        buscar_pais(paises)

    # -----------------------------------------------------
    # OPCIÓN 4
    # -----------------------------------------------------
    elif opcion == "4":
        filtrar_paises(paises)

    # -----------------------------------------------------
    # OPCIÓN 5
    # -----------------------------------------------------
    elif opcion == "5":
        ordenar_paises(paises)

    # -----------------------------------------------------
    # OPCIÓN 6
    # -----------------------------------------------------
    elif opcion == "6":
        mostrar_estadisticas(paises)

    # -----------------------------------------------------
    # OPCIÓN 7
    # -----------------------------------------------------
    elif opcion == "7":
        mostrar_todos(paises)

    # -----------------------------------------------------
    # OPCIÓN 0
    # -----------------------------------------------------
    elif opcion == "0":

        guardar_csv(ARCHIVO, paises)

        print("Programa finalizado.")

        break

    # -----------------------------------------------------
    # OPCIÓN INVÁLIDA
    # -----------------------------------------------------
    else:
        print("Opción inválida.")
