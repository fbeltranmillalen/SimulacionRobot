from vpython import vector, color, label


class Coordenada:
    # atributos
    # un Label que depende de la posición del robot en tiempo real

    # Robot
    # posicion
    # fuente

    def __init__(self, robot, altura=vector(0, 5, 0), text_color=color.white):
        self.Robot = robot  # el atributo es un objeto tipo Robot
        self.altura = altura
        self.text_color = text_color

    def dibujar_coordenada(self):
        cordenadas = label(pos=(self.Robot.pos + self.altura), text=str(self.Robot.pos), color=self.text_color)
        return cordenadas

    def actualizar_coordenada(self, nueva_coordenada, nueva_posicion):
        nueva_coordenada.text = str(nueva_posicion)
        nueva_coordenada.pos = nueva_posicion + self.altura
