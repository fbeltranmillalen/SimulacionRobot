from vpython import vector, box, cylinder, compound


class Robot:

    # posicionInicial
    # tamaño
    # tipo de robot
    # color

    def __init__(self, initial_position, size, color, robot_type=1):
        self.initialPosition = initial_position    # vector
        self.size = size    # vector
        self.color = color  # color
        self.robot_type = robot_type    # int

    def draw_robot(self):  # retornar el centro de masa
        caja = box(pos=self.initialPosition, size=self.size, color=self.color)
        rueda = cylinder(pos=self.initialPosition, axis=vector(5, 0, 0), radius=1, color=self.color)
        robot = compound([caja, rueda])
        return robot
