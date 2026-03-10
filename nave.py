class Nave:
    # El "constructor": define los datos necesarios al instanciar
    def __init__(self, nombre, tamano):
        self.nombre = nombre       # Atributo: Nombre de la nave
        self.vida = tamano         # Atributo: Resistencia de la nave
        self.hundido = False       # Atributo: Estado lógico inicial
        self.TOCADO = 1
        self.HUNDIDO = 2

    # Un "método": Comportamiento definido para el objeto
    def recibir_disparo(self):
        self.vida -= 1
        if self.vida <= 0:
            return self.hundido == True
        else:
            return self.TOCADO