class Autor:
    def __init__(self, nombre):
        self.nombre = nombre
        self.libros = []  # Bidireccional: autor conoce sus libros

    def agregar_libro(self, libro):
        self.libros.append(libro)

class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        autor.agregar_libro(self)

    def __repr__(self):
        return f"{self.titulo}"

# Ahora ambos pueden acceder el uno al otro

autor = Autor("Mario Abarca")
libro = Libro("La noche de Tlatelolco", autor)
libro2 = Libro("EL libro del mariño", autor)

print("Los libros de ", autor.nombre , " son:", autor.libros)