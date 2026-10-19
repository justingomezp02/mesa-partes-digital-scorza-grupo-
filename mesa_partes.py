mesa-partes-digital-scorza/# =================================================================================
# MESA DE PARTES DIGITAL - I.E. 2032 MANUEL SCORZA TORRES
# Implementación en Python (Tema 4)
# =================================================================================

from datetime import datetime

# Variables globales (Arreglos paralelos)
MAXEXP = 100
vecNumeroExpediente = []
vecDniUsuario = []
vecDniEstudiante = []
vecNombreUsuario = []
vecNombreEstudiante = []
vecTipoTramite = []
vecFecha = []
vecEstado = []
vecAreaDestino = []
totalExp = 0

# --- FUNCIÓN DE VALIDACIÓN ---
def es_dni_valido(dni):
    """Verifica que el DNI tenga exactamente 8 caracteres numéricos."""
    if len(dni) == 8 and dni.isdigit():
        return True
    return False

# --- SUBPROCESO: DETERMINAR AREA DESTINO ---
def determinar_area_destino(tipo_tramite):
    if tipo_tramite == 1:
        print("Ruta: Dirección (Aprobación) -> Administración / Secretaría")
        return 3
    elif tipo_tramite == 2:
        print("Ruta: Dirección (Aprobación) -> Subdirección de Nivel")
        return 2
    elif tipo_tramite == 3:
        print("Ruta: Dirección (Aprobación) -> Subdirección Pedagógica")
        return 2
    elif tipo_tramite == 4:
        print("Ruta: Dirección (Aprobación) -> Secretaría General")
        return 3
    return 0

# --- SUBPROCESO: REGISTRAR SOLICITUD ---
def registrar_solicitud():
    global totalExp
    print("\n--- REGISTRO DE NUEVA SOLICITUD ---")
    if totalExp >= MAXEXP:
        print("ERROR: Capacidad máxima de expedientes alcanzada.")
        return

    dni_usuario = input("Ingrese DNI del padre, apoderado o ciudadano (8 dígitos): ")
    dni_estudiante = input("Ingrese DNI del estudiante (8 dígitos): ")

    if not es_dni_valido(dni_usuario) or not es_dni_valido(dni_estudiante):
        print("ERROR RECHAZO: Los DNI deben contener exactamente 8 dígitos numéricos.")
        return

    nombre_usuario = input("Ingrese nombres y apellidos del solicitante/apoderado: ")
    nombre_estudiante = input("Ingrese nombres y apellidos del estudiante: ")

    print("Seleccione el tipo de trámite a realizar:")
    print(" 1. Constancia de matrícula")
    print(" 2. Constancia de vacante")
    print(" 3. Certificado de estudios")
    print(" 4. Ficha única de matrícula (FUM)")

    try:
        tipo_tramite = int(input("Ingrese opción (1-4): "))
        if tipo_tramite < 1 or tipo_tramite > 4:
            print("ERROR: Tipo de trámite no reconocido.")
            return
    except ValueError:
        print("ERROR: Debe ingresar un número entero.")
        return

    docs_completos = input("¿Presentó todos los requisitos y documentos físicos obligatorios? (SI/NO): ").upper()
    if docs_completos != "SI":
        print("SOLICITUD OBSERVADA: Requisitos incompletos. Se emite observación.")
        print("No se confirma el registro del expediente hasta completar requisitos.")
        return

    fecha_recepcion = datetime.now().strftime("%d/%m/%Y")
    estado = "Registrado - Pendiente de revisión por Dirección"

    totalExp += 1
    pos = totalExp - 1

    vecNumeroExpediente.append(totalExp)
    vecDniUsuario.append(dni_usuario)
    vecDniEstudiante.append(dni_estudiante)
    vecNombreUsuario.append(nombre_usuario)
    vecNombreEstudiante.append(nombre_estudiante)
    vecTipoTramite.append(tipo_tramite)
    vecFecha.append(fecha_recepcion)
    vecEstado.append(estado)

    print("\n>> SOLICITUD VALIDADA Y REGISTRADA EXITOSAMENTE <<<")
    print(f"N.° de Expediente Asignado: EXP-2026-{totalExp}")
    print(f"Fecha de Recepción Oficial: {fecha_recepcion}")
    print(f"Estado Administrativo: {estado}")
    print("Costo del Trámite: GRATUITO (Ley N.° 31170)")

    area = determinar_area_destino(tipo_tramite)
    vecAreaDestino.append(area)

# --- SUBPROCESO: CONSULTAR EXPEDIENTE ---
def consultar_expediente():
    print("\n--- CONSULTA DE ESTADO DE EXPEDIENTE ---")
    try:
        numero_buscado = int(input("Ingrese el número correlativo de expediente a consultar: "))
    except ValueError:
        print("Error: Ingrese un número válido.")
        return

    encontrado = False
    for i in range(totalExp):
        if vecNumeroExpediente[i] == numero_buscado:
            print(f"\nExpediente: EXP-2026-{vecNumeroExpediente[i]}")
            print(f"DNI solicitante: {vecDniUsuario[i]}")
            print(f"Solicitante: {vecNombreUsuario[i]}")
            print(f"DNI estudiante: {vecDniEstudiante[i]}")
            print(f"Estudiante: {vecNombreEstudiante[i]}")
            print(f"Tipo de trámite (código): {vecTipoTramite[i]}")
            print(f"Fecha de recepción: {vecFecha[i]}")
            print(f"Estado: {vecEstado[i]}")
            print(f"Área destino (código): {vecAreaDestino[i]}")
            encontrado = True
            break

    if not encontrado:
        print(f"ALERTA: El expediente N.° {numero_buscado} no se encuentra registrado en el sistema.")

# --- SUBPROCESO: MOSTRAR RESUMEN ESTADISTICO ---
def mostrar_resumen():
    print("\n--- RESUMEN ESTADÍSTICO DE ATENCIONES ---")
    print(f"Total de expedientes: {totalExp}")

    c_mat, c_vac, c_cer, c_fum, c_pend = 0, 0, 0, 0, 0

    for i in range(totalExp):
        if vecTipoTramite[i] == 1:
            c_mat += 1
        elif vecTipoTramite[i] == 2:
            c_vac += 1
        elif vecTipoTramite[i] == 3:
            c_cer += 1
        elif vecTipoTramite[i] == 4:
            c_fum += 1

        if "Registrado" in vecEstado[i]:
            c_pend += 1

    print("Por tipo de trámite:")
    print(f" Constancia de matrícula: {c_mat}")
    print(f" Constancia de vacante: {c_vac}")
    print(f" Certificado de estudios: {c_cer}")
    print(f" Ficha única (FUM): {c_fum}")
    print("Por estado:")
    print(f" Registrado - Pendiente de revisión: {c_pend}")

# --- MÓDULO PRINCIPAL (MENÚ) ---
def main():
    opcion = 0
    while opcion != 4:
        print("\n" + "="*55)
        print(" MESA DE PARTES DIGITAL - I.E. 2032 MANUEL SCORZA TORRES")
        print("="*55)
        print("1. Registrar nueva solicitud de trámite")
        print("2. Consultar estado de expediente")
        print("3. Ver resumen estadístico de atenciones")
        print("4. Salir del sistema")

        try:
            opcion = int(input("Seleccione una opción (1-4): "))
            if opcion == 1:
                registrar_solicitud()
            elif opcion == 2:
                consultar_expediente()
            elif opcion == 3:
                mostrar_resumen()
            elif opcion == 4:
                print("Cerrando sesión. Gracias por utilizar la Mesa de Partes Digital.")
            else:
                print("Error: Opción inválida. Por favor, seleccione una opción entre 1 y 4.")
        except ValueError:
            print("Error: Por favor, ingrese un número.")

if __name__ == "__main__":
    main()
│
├── README.md
├── mesa_partes.py          <-- El código Python del Tema 4.3
├── pseudocodigo.psc        <-- (Opcional) El pseudocódigo PSeInt del Tema 3.3
└── capturas/
    ├── figura_4.1_dni_invalido.png
    ├── figura_4.2_requisitos_incompletos.png
    ├── figura_4.3_registro_exitoso.png
    ├── figura_4.4_consulta_expediente.png
    └── figura_4.5_resumen_estadistico.png
  # Mesa de Partes Digital - I.E. 2032 Manuel Scorza Torres

**Curso:** Fundamentos de Programación (CIIN1205P)  
**Universidad:** Universidad Privada del Norte - Sede Los Olivos  
**Proyecto:** Prototipo de Mesa de Partes Digital (Ley N.° 31170)

## Integrantes
- Marco Antonio Calongos López – N00552217
- Mia Kassandra Manrique Dextre – N00550975
- Maribel Huillca Huallpa – N00530117
- Adriano Felix Zamudio Poma – N00553052

## Descripción
Prototipo modular en Python que automatiza el registro, validación, derivación y consulta de expedientes de la Mesa de Partes de la I.E. 2032 Manuel Scorza Torres.

## Módulos implementados
1. Menú principal (`main`)
2. Validación de DNI (`es_dni_valido`)
3. Registro de solicitud (`registrar_solicitud`)
4. Derivación por área (`determinar_area_destino`)
5. Consulta de expediente (`consultar_expediente`)
6. Resumen estadístico (`mostrar_resumen`)

## Ejecución
```bash
python mesa_partes.py

---

### 3. Qué pegar en el informe (página 1)

En la sección **ENLACE DEL REPOSITORIO (GIT/GITHUB):** pega el enlace de tu repositorio:
# =================================================================================
# MESA DE PARTES DIGITAL - I.E. 2032 MANUEL SCORZA TORRES
# Implementación en Python (Tema 4)
# =================================================================================

from datetime import datetime

# Variables globales (Arreglos paralelos)
MAXEXP = 100
vecNumeroExpediente = []
vecDniUsuario = []
vecDniEstudiante = []
vecNombreUsuario = []
vecNombreEstudiante = []
vecTipoTramite = []
vecFecha = []
vecEstado = []
vecAreaDestino = []
totalExp = 0

# --- FUNCIÓN DE VALIDACIÓN ---
def es_dni_valido(dni):
    """Verifica que el DNI tenga exactamente 8 caracteres numéricos."""
    if len(dni) == 8 and dni.isdigit():
        return True
    return False

# --- SUBPROCESO: DETERMINAR AREA DESTINO ---
def determinar_area_destino(tipo_tramite):
    if tipo_tramite == 1:
        print("Ruta: Dirección (Aprobación) -> Administración / Secretaría")
        return 3
    elif tipo_tramite == 2:
        print("Ruta: Dirección (Aprobación) -> Subdirección de Nivel")
        return 2
    elif tipo_tramite == 3:
        print("Ruta: Dirección (Aprobación) -> Subdirección Pedagógica")
        return 2
    elif tipo_tramite == 4:
        print("Ruta: Dirección (Aprobación) -> Secretaría General")
        return 3
    return 0

# --- SUBPROCESO: REGISTRAR SOLICITUD ---
def registrar_solicitud():
    global totalExp
    print("\n--- REGISTRO DE NUEVA SOLICITUD ---")
    if totalExp >= MAXEXP:
        print("ERROR: Capacidad máxima de expedientes alcanzada.")
        return

    dni_usuario = input("Ingrese DNI del padre, apoderado o ciudadano (8 dígitos): ")
    dni_estudiante = input("Ingrese DNI del estudiante (8 dígitos): ")

    if not es_dni_valido(dni_usuario) or not es_dni_valido(dni_estudiante):
        print("ERROR RECHAZO: Los DNI deben contener exactamente 8 dígitos numéricos.")
        return

    nombre_usuario = input("Ingrese nombres y apellidos del solicitante/apoderado: ")
    nombre_estudiante = input("Ingrese nombres y apellidos del estudiante: ")

    print("Seleccione el tipo de trámite a realizar:")
    print(" 1. Constancia de matrícula")
    print(" 2. Constancia de vacante")
    print(" 3. Certificado de estudios")
    print(" 4. Ficha única de matrícula (FUM)")

    try:
        tipo_tramite = int(input("Ingrese opción (1-4): "))
        if tipo_tramite < 1 or tipo_tramite > 4:
            print("ERROR: Tipo de trámite no reconocido.")
            return
    except ValueError:
        print("ERROR: Debe ingresar un número entero.")
        return

    docs_completos = input("¿Presentó todos los requisitos y documentos físicos obligatorios? (SI/NO): ").upper()
    if docs_completos != "SI":
        print("SOLICITUD OBSERVADA: Requisitos incompletos. Se emite observación.")
        print("No se confirma el registro del expediente hasta completar requisitos.")
        return

    fecha_recepcion = datetime.now().strftime("%d/%m/%Y")
    estado = "Registrado - Pendiente de revisión por Dirección"

    totalExp += 1
    pos = totalExp - 1

    vecNumeroExpediente.append(totalExp)
    vecDniUsuario.append(dni_usuario)
    vecDniEstudiante.append(dni_estudiante)
    vecNombreUsuario.append(nombre_usuario)
    vecNombreEstudiante.append(nombre_estudiante)
    vecTipoTramite.append(tipo_tramite)
    vecFecha.append(fecha_recepcion)
    vecEstado.append(estado)

    print("\n>> SOLICITUD VALIDADA Y REGISTRADA EXITOSAMENTE <<<")
    print(f"N.° de Expediente Asignado: EXP-2026-{totalExp}")
    print(f"Fecha de Recepción Oficial: {fecha_recepcion}")
    print(f"Estado Administrativo: {estado}")
    print("Costo del Trámite: GRATUITO (Ley N.° 31170)")

    area = determinar_area_destino(tipo_tramite)
    vecAreaDestino.append(area)

# --- SUBPROCESO: CONSULTAR EXPEDIENTE ---
def consultar_expediente():
    print("\n--- CONSULTA DE ESTADO DE EXPEDIENTE ---")
    try:
        numero_buscado = int(input("Ingrese el número correlativo de expediente a consultar: "))
    except ValueError:
        print("Error: Ingrese un número válido.")
        return

    encontrado = False
    for i in range(totalExp):
        if vecNumeroExpediente[i] == numero_buscado:
            print(f"\nExpediente: EXP-2026-{vecNumeroExpediente[i]}")
            print(f"DNI solicitante: {vecDniUsuario[i]}")
            print(f"Solicitante: {vecNombreUsuario[i]}")
            print(f"DNI estudiante: {vecDniEstudiante[i]}")
            print(f"Estudiante: {vecNombreEstudiante[i]}")
            print(f"Tipo de trámite (código): {vecTipoTramite[i]}")
            print(f"Fecha de recepción: {vecFecha[i]}")
            print(f"Estado: {vecEstado[i]}")
            print(f"Área destino (código): {vecAreaDestino[i]}")
            encontrado = True
            break

    if not encontrado:
        print(f"ALERTA: El expediente N.° {numero_buscado} no se encuentra registrado en el sistema.")

# --- SUBPROCESO: MOSTRAR RESUMEN ESTADISTICO ---
def mostrar_resumen():
    print("\n--- RESUMEN ESTADÍSTICO DE ATENCIONES ---")
    print(f"Total de expedientes: {totalExp}")

    c_mat, c_vac, c_cer, c_fum, c_pend = 0, 0, 0, 0, 0

    for i in range(totalExp):
        if vecTipoTramite[i] == 1:
            c_mat += 1
        elif vecTipoTramite[i] == 2:
            c_vac += 1
        elif vecTipoTramite[i] == 3:
            c_cer += 1
        elif vecTipoTramite[i] == 4:
            c_fum += 1

        if "Registrado" in vecEstado[i]:
            c_pend += 1

    print("Por tipo de trámite:")
    print(f" Constancia de matrícula: {c_mat}")
    print(f" Constancia de vacante: {c_vac}")
    print(f" Certificado de estudios: {c_cer}")
    print(f" Ficha única (FUM): {c_fum}")
    print("Por estado:")
    print(f" Registrado - Pendiente de revisión: {c_pend}")

# --- MÓDULO PRINCIPAL (MENÚ) ---
def main():
    opcion = 0
    while opcion != 4:
        print("\n" + "="*55)
        print(" MESA DE PARTES DIGITAL - I.E. 2032 MANUEL SCORZA TORRES")
        print("="*55)
        print("1. Registrar nueva solicitud de trámite")
        print("2. Consultar estado de expediente")
        print("3. Ver resumen estadístico de atenciones")
        print("4. Salir del sistema")

        try:
            opcion = int(input("Seleccione una opción (1-4): "))
            if opcion == 1:
                registrar_solicitud()
            elif opcion == 2:
                consultar_expediente()
            elif opcion == 3:
                mostrar_resumen()
            elif opcion == 4:
                print("Cerrando sesión. Gracias por utilizar la Mesa de Partes Digital.")
            else:
                print("Error: Opción inválida. Por favor, seleccione una opción entre 1 y 4.")
        except ValueError:
            print("Error: Por favor, ingrese un número.")

if __name__ == "__main__":
    main()
