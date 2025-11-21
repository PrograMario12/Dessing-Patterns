from SistemaDeGestionDeEmpleados.ingeniero import Ingeniero
from SistemaDeGestionDeEmpleados.gerente import Gerente
from SistemaDeGestionDeEmpleados.obrero import Obrero
from SistemaDeGestionDeEmpleados.procesar_nomina import procesar_nomina

if __name__ == "__main__":
    ingeniero = Ingeniero("Ana García", 5000, "Backend Python")
    gerente = Gerente("Carlos López", 7000, "Desarrollo")
    obrero = Obrero("María Rodríguez", 2500, "Nocturno")

    empleados = [ingeniero, gerente, obrero]

    procesar_nomina(empleados)
