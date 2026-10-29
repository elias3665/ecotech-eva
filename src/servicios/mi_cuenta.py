from servicios.permisos import exigir_sesion
from persistencia.empleado_dao import EmpleadoDAO
from persistencia.registrotrabajo_dao import RegistroTrabajoDAO
from dominio.empleado import Empleado

def ver_mi_ficha(sesion) -> Empleado:
    exigir_sesion(sesion)
    empleado = EmpleadoDAO.buscar_por_id(sesion["empleado_id"])
    if not empleado:
        raise ValueError("No se encontraron datos asociados a tu perfil.")
    return empleado

def ver_mis_registros_laborales(sesion):
    exigir_sesion(sesion)
    todos = RegistroTrabajoDAO.listar_completo()
    return [r for r in todos if r.empleado.id == sesion["empleado_id"]]

def actualizar_mis_datos(sesion, nuevo_nombre: str, nuevo_email: str) -> bool:
    exigir_sesion(sesion)
    emp_validado = Empleado(nombre=nuevo_nombre, email=nuevo_email, id=sesion["empleado_id"])
    
    return EmpleadoDAO.actualizar(emp_validado)
