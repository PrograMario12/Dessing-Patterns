from empleado import Empleado

class Gerente(Empleado):
    def __init__(self, nombre: str, salario_base: float, departamento: str):
        super().__init__(nombre, salario_base)
        self.departamento = departamento

    def calcular_bono(self) -> float:
        bono = self.salario_base * 0.25
        self.agregar_bonificacion(bono)
        return bono

    def generar_reporte(self) -> str:
        return (f"Gerente de {self.departamento}: {self.nombre}, Salario base: ${self.salario_base:.2f}, "
                f"Bono: ${self.calcular_bono():.2f}, Bonificaciones acumuladas: ${self.bonificaciones:.2f}")

