from empleado import Empleado

class Obrero(Empleado):
    def __init__(self, nombre: str, salario_base: float, turno: str):
        super().__init__(nombre, salario_base)
        self.turno = turno

    def calcular_bono(self) -> float:
        if self.turno == "Nocturno":
            bono = self.salario_base * 0.10
        else:
            bono = self.salario_base * 0.05
        self.agregar_bonificacion(bono)
        return bono

    def generar_reporte(self) -> str:
        return (f"Obrero turno {self.turno}: {self.nombre}, Salario base: ${self.salario_base:.2f}, "
                f"Bono: ${self.calcular_bono():.2f}, Bonificaciones acumuladas: ${self.bonificaciones:.2f}")

