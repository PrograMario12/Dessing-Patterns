from abc import ABC, abstractmethod

class Empleado(ABC):
    def __init__(self, nombre: str, salario_base: float):
        self.__nombre = nombre
        self.__salario_base = salario_base
        self.__bonificaciones = 0

    @property
    def nombre(self) -> str:
        return self.__nombre

    @property
    def salario_base(self) -> float:
        if self.__salario_base < 0:
            raise ValueError("El salario no puede ser negativo")
        return self.__salario_base

    @salario_base.setter
    def salario_base(self, nuevo_salario: float):
        if nuevo_salario < 0:
            raise ValueError("El salario no puede ser negativo")
        self.__salario_base = nuevo_salario

    def agregar_bonificacion(self, monto: float):
        if monto > 0:
            self.__bonificaciones += monto

    @property
    def bonificaciones(self) -> float:
        return self.__bonificaciones

    @abstractmethod
    def calcular_bono(self) -> float:
        pass

    @abstractmethod
    def generar_reporte(self) -> str:
        pass
