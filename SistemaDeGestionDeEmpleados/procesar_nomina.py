from typing import List
from SistemaDeGestionDeEmpleados.empleado import Empleado

def procesar_nomina(empleados: List[Empleado]) -> None:
    total_pagos = 0
    for empleado in empleados:
        bono = empleado.calcular_bono()
        salario_total = empleado.salario_base + bono
        total_pagos += salario_total
        print(f"Empleado: {empleado.nombre}")
        print(f"Salario Base: ${empleado.salario_base:.2f}")
        print(f"Bono: ${bono:.2f}")
        print(f"Salario Total: ${salario_total:.2f}")
        print(empleado.generar_reporte())
        print("-" * 50)
    print(f"Total de nómina: ${total_pagos:.2f}")
