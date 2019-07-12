from vpython import vector, arrow, color, label, box


class R3:
    # atributos

    """
    origen = vector(0,0,0)
    shaftwidth = 0.1
    ejeX = vector(100, 0, 0)
    ejeY = vector(0, 100, 0)
    ejeZ = vector(0, 0, 100)
    colorX = color.red
    colorY = color.blue
    colorZ = color.green
    floorPosition = vector(50, -0.1, 50)
    floorSize = vector(0.1, 100, 100)
    floorAxis = vector(0, 1, 0)
    """

    # TODO
    # hacerlo con textura?, que se vean los cuadrados al intersectar eje x con z
    # constructor
    def __init__(self,
                 origen=vector(0, 0, 0),
                 shaftwidth=0.1,
                 eje_x=vector(100, 0, 0),
                 eje_y=vector(0, 100, 0),
                 eje_z=vector(0, 0, 100),
                 color_x=color.red,
                 color_y=color.blue,
                 color_z=color.green,
                 floor_position=vector(50, -0.1, 50),
                 floor_size=vector(0.1, 100, 100),
                 floor_axis=vector(0, 1, 0)):
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
    def draw_r3(self):
        # EJE x
        arrow(pos=self.origen, axis=self.ejeX, shaftwidth=self.shaftwidth, color=self.colorX)
        label(pos=vector(100, 1, 0), text='x', color=color.red)

        # EJE y
        arrow(pos=self.origen, axis=self.ejeY, shaftwidth=self.shaftwidth, color=self.colorZ)
        label(pos=vector(1, 100, 0), text='y', color=color.blue)

        # EJE z
        arrow(pos=self.origen, axis=self.ejeZ, shaftwidth=self.shaftwidth, color=self.colorZ)
        label(pos=vector(0, 1, 100), text='z', color=color.green)

        # superficie blanca
        box(pos=self.floorPosition, size=self.floorSize, axis=self.floorAxis)
