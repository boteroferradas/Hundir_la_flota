class Nave:
    # El "constructor": define los datos necesarios al instanciar
    def __init__(self, nombre, tipo, vida):
        self.nombre = nombre
        self.tipo = tipo
        self.vida = vida
        self.hundido = False
        self.TOCADO = 1
        self.HUNDIDO = 2

    def recibir_disparo(self):
        self.vida -= 1
        if self.vida <= 0:
            return self.hundido == True
        else:
            return self.TOCADO

    def __str__(self):
        return f"Nombre: {self.nombre}, Tipo: {self.tipo}, Vida: {self.vida} "