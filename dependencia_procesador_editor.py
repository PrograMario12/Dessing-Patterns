class ProcesadorTexto:
    def procesar(self, documento):
        print(f"Procesando documento: {documento}")

class Editor:
    def editar_documento(self, documento):
        procesador = ProcesadorTexto()  # El editor depende de ProcesadorTexto solo en este método
        procesador.procesar(documento)
        print("Edición terminada")

editor = Editor()
editor.editar_documento("mi_documento.txt")