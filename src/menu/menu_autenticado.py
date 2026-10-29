from servicios.mi_cuenta import ver_mi_ficha, ver_mis_registros_laborales, actualizar_mis_datos
from menu.menu_empleado import menu_empleado
from menu.menu_proyecto import menu_proyecto
from menu.menu_registro import menu_registro
from menu.menu_usuario import consultar_indicador_economico, solicitar_registro

def desplegar_entorno_privado(usuario_actual):
    if not usuario_actual:
        return

    while True:
        print(f"\n--- ECOTECH INTERNO | SESIÓN: {usuario_actual['nombre_usuario'].upper()} ({usuario_actual['rol'].upper()}) ---")
        print("1. Ver mi Ficha Personal")
        print("2. Ver mis Registros de Tiempo")
        print("3. Modificar mis Datos de Contacto")
        print("4. Consultar Indicador del Dólar (API Externa)")
        
        # Opciones exclusivas del Administrador
        if usuario_actual["rol"] == "admin":
            print("\n[Módulos de Gestión Administrativa]")
            print("5. Control Maestro de Empleados")
            print("6. Control Maestro de Proyectos")
            print("7. Bitácora e Imputación Global de Horas")
            print("8. Registrar nueva Cuenta de Acceso a Empleado")
            
        print("\n9. Cerrar Sesión Activa")
        print("0. Salir del Sistema")
        
        opc = input("Seleccione una opción: ").strip()
        
        try:
            if opc == "1":
                emp = ver_mi_ficha(usuario_actual)
                print(f"\n[Ficha] ID: {emp.id} | Nombre: {emp.nombre} | Email: {emp.email}")
            elif opc == "2":
                regs = ver_mis_registros_laborales(usuario_actual)
                if not regs:
                    print("No registras horas ingresadas en el sistema.")
                for r in regs:
                    print(r.mostrar_detalle())
            elif opc == "3":
                n_nom = input("Nuevo Nombre corporativo: ").strip()
                n_em = input("Nuevo Correo electrónico: ").strip()
                if actualizar_mis_datos(usuario_actual, n_nom, n_em):
                    print("Tus datos fueron actualizados. Los cambios se verán reflejados en tu próxima sesión.")
            elif opc == "4":
                consultar_indicador_economico()
            elif opc == "5" and usuario_actual["rol"] == "admin":
                menu_empleado()
            elif opc == "6" and usuario_actual["rol"] == "admin":
                menu_proyecto()
            elif opc == "7" and usuario_actual["rol"] == "admin":
                menu_registro()
            elif opc == "8" and usuario_actual["rol"] == "admin":
                solicitar_registro()
            elif opc == "9":
                print("Sesión finalizada de manera segura.")
                break
            elif opc == "0":
                print("Cerrando EcoTech.")
                exit(0)
            else:
                print("Opción no válida o sin permisos suficientes.")
        except Exception as e:
            print(f"[Acceso Denegado / Error]: {e}")
