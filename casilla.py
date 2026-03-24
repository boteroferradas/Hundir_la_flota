class Casilla:
    def __init__(self):
        self.nave = None
        self.visitada = False

    def disparar(self):
        '''
        :return: boolean, recibir_disparo()
        Metodo que sirve para comprobar si la casilla ya recibio un ataque previamente, si no hay
        una nave que nos devuelva "Agua" y nos devuelva el estado de la nave.
        '''
        if self.visitada:
            print("Ya disparaste aquí")
            return None

        self.visitada = True

        if self.nave is None:
            print("Agua")
            return 0

        return self.nave.recibir_disparo()