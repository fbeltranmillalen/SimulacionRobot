from vpython import vector, box, cylinder, compound, color, sphere


class Robot:

    # posicionInicial
    # tamaño
    # tipo de robot
    # color

    def __init__(self, initial_position, size, color, robot_type):
        self.initialPosition = initial_position  # vector
        self.size = size  # vector
        self.color = color  # color
        self.robot_type = robot_type  # int

    def draw_robot(self):  # retornar el centro de masa
        if self.robot_type == 0:
            caja = box(pos=self.initialPosition, size=self.size, color=self.color)
            rueda_trasera = cylinder(pos=caja.pos - vector(caja.size.x / 4, caja.size.y, caja.size.z / 4),
                                 axis=vector(0, 4, 0), radius=0.5, color=self.color)
            rueda_delantera = cylinder(pos=caja.pos + vector(caja.size.x / 4, -caja.size.y, -caja.size.z / 4),
                                   axis=vector(0, 4, 0), radius=0.5, color=self.color)

            robot = compound([caja, rueda_trasera, rueda_delantera])
        elif self.robot_type == 1:
            cuerpo = cylinder(pos=self.initialPosition, radius=3, color=color.blue, axis=vector(0, 0, 1), opacity=1)
            rueda_1 = cylinder(pos=cuerpo.pos + vector(0, cuerpo.radius/2, 0), radius=cuerpo.radius/4, color=color.red, axis=vector(0, 1, 0), opacity=1)
            rueda_2 = cylinder(pos=cuerpo.pos - vector(0, cuerpo.radius/2 + cuerpo.radius/3, 0), radius=cuerpo.radius/4, color=color.cyan, axis=vector(0, 1, 0), opacity=1)
            estabilizador = sphere(pos=cuerpo.pos + vector(cuerpo.radius/2 + cuerpo.radius/9, 0, 0), radius=cuerpo.radius/4, color=color.green, axis=vector(0, 1, 0), opacity=1)
            robot = compound([cuerpo, rueda_1, rueda_2, estabilizador])
        return robot
