class Motor:
    def __init__(self, tipo):
        self.tipo = tipo

    def encender(self):
        print(f"Motor {self.tipo} encendido")

class Coche:
    def __init__(self, marca, tipo_motor):
        self.marca = marca
        self.motor = Motor(tipo_motor)  # Composición: el motor es parte del coche y creado aquí

    def arrancar(self):
        print(f"Arrancando coche {self.marca}")
        self.motor.encender()

# Uso
coche1 = Coche("Toyota", "V8")
coche1.arrancar()
