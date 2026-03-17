from tablero import Tablero

class Juego:
    def __init__(self):
        self.tablero = Tablero()
        self.lanzar_ataque(1, 1)
        self.lanzar_ataque(4, 0)
        self.lanzar_ataque(7, 6)

    def lanzar_ataque(self,x,y):
        print(f"Atacando: X-{x} Y-{y}")
        obj_tablero = Tablero()
        resultado = obj_tablero.comprobar_impacto(x,y)
        self.mostrar_resultado(resultado)

    def mostrar_resultado(self, resultado):
        if resultado == 0:
            print("Agua")
        elif resultado == 1:
            print("Tocado")
        elif resultado == 2:
            print("Hundido")

    def lanzar_ataque(self, x, y):
        """
        Ejecuta un disparo en las coordenadas indicadas.
        Si impacta una nave y su vida llega a cero, muestra mensaje de hundimiento.

        Args:
            x (int): Coordenada X del disparo
            y (int): Coordenada Y del disparo
        """
        print(f"Atacando a  {x}, {y} ")
        obj_tablero = Tablero()
        resultado = obj_tablero.comprobar_impacto(x, y)
        self.mostrar_resultado(resultado)

if __name__ == "__main__":
        Juego()