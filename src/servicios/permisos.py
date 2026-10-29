def exigir_sesion(sesion):
    if not isinstance(sesion, dict):
        raise PermissionError("Inicie sesión para continuar.")
    if sesion.get("rol") not in ("admin", "empleado"):
        raise PermissionError("Acceso no permitido. Rol inválido.")
    empleado_id = sesion.get("empleado_id")
    if type(empleado_id) is not int or empleado_id <= 0:
        raise PermissionError("Sesión corrupta o inválida.")

def exigir_admin(sesion):
    exigir_sesion(sesion)
    if sesion["rol"] != "admin":
        raise PermissionError("Operación denegada: Requiere privilegios de Administrador.")
