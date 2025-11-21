class Autor:
    def __init__(self, nombre):
        self.nombre = nombre

class Libro:
    def __init__(self, titulo, autor_obj):
        self.titulo = titulo
        self.autor = autor_obj  # Asociación: Libro conoce al Autor

    def mostrar_info(self):
        print(f"Título: {self.titulo}, Autor: {self.autor.nombre}")

autor = Autor("Elena Poniatowska")
libro = Libro("La noche de Tlatelolco", autor)
libro.mostrar_info()  # Acceso del Libro hacia el Autor
