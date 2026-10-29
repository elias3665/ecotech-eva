import sys
from persistencia.crear_bd import crear_tablas
from menu.menu_usuario import solicitar_login, menu_privado
def main():
    try:
        crear_tablas()
    except Exception as e:
        print(f"Error crítico al inicializar la base de datos: {e}")
        sys.exit(1)

    while True:
        print("\n===== ECOTECH: CONTROL INTEGRADO DE ACCESO =====")
        print("1. Iniciar Sesión en el Sistema")
        print("0. Salir de la Aplicación")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            usuario_autenticado = solicitar_login()
            if usuario_autenticado:
                menu_privado(usuario_autenticado)
        elif opcion == "0":
            print("Cerrando EcoTech de forma segura. Hasta luego.")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()
