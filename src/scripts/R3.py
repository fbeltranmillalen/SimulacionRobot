from vpython import vector, arrow, color, label, box


class R3:

    # TODO
    # hacerlo con textura?, que se vean los cuadrados al intersectar eje x con z
    # constructor

    AXIS_SIZE = 50

    def __init__(self,
                 origen=vector(0, 0, 0),
                 shaftwidth=0.1,
                 eje_x=vector(AXIS_SIZE, 0, 0),
                 eje_y=vector(0, AXIS_SIZE, 0),
                 eje_z=vector(0, 0, AXIS_SIZE/2),
                 color_x=color.red,
                 color_y=color.blue,
                 color_z=color.green,
                 floor_position=vector(AXIS_SIZE/2, AXIS_SIZE/2, -0.1),
                 floor_size=vector(0.1, AXIS_SIZE, AXIS_SIZE),
                 floor_axis=vector(0, 0, 1)):
        self.origen = origen
        self.shaftwidth = shaftwidth
        self.ejeX = eje_x
        self.ejeY = eje_y
        self.ejeZ = eje_z
        self.colorX = color_x
        self.colorY = color_y
        self.colorZ = color_z
        self.floorPosition = floor_position
        self.floorSize = floor_size
        self.floorAxis = floor_axis

    # setter getter

    # metodos
    def draw_r3(self, axis_size=AXIS_SIZE):

        # EJE x
        arrow(pos=self.origen, axis=self.ejeX, shaftwidth=self.shaftwidth, color=self.colorX)
        label(pos=vector(axis_size, 1, 0), text='x', color=color.red)

        # EJE y
        arrow(pos=self.origen, axis=self.ejeY, shaftwidth=self.shaftwidth, color=self.colorY)
        label(pos=vector(1, axis_size, 0), text='y', color=color.blue)

        # EJE z
        arrow(pos=self.origen, axis=self.ejeZ, shaftwidth=self.shaftwidth, color=self.colorZ)
        label(pos=vector(0, 1, axis_size/2), text='z', color=color.green)

        # superficie blanca
        box(pos=self.floorPosition, size=self.floorSize, axis=self.floorAxis, opacity=0.2)
