class Estudiante:
    def __init__(self, nombre):
        self.nombre = nombre

class Curso:
    def __init__(self, nombre):
        self.nombre = nombre
        self.estudiantes = []  # Lista de estudiantes, agregado

    def agregar_estudiante(self, estudiante: Estudiante):
        self.estudiantes.append(estudiante)

    def mostrar_estudiantes(self):
        for e in self.estudiantes:
            print(e.nombre)

# Crear estudiantes
est1 = Estudiante("Ana")
est2 = Estudiante("Luis")

# Crear curso y agregar estudiantes (agregación)
curso = Curso("Matemáticas")
curso.agregar_estudiante(est1)
curso.agregar_estudiante(est2)

curso.mostrar_estudiantes()  # Ana, Luis
