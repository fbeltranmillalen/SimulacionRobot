#from src.scripts.Clases.Robot import Robot

class RobotOmnidireccional:

    def __init__(self, vPythonRobot, posicion_x_array, posicion_y_array, posicion_z_array, velocidad_x_array,
                 velocidad_y_array, velocidad_z_array, velocidad_lineal_frontal_array, velocidad_lineal_lateral_array, velocidad_angular_array,
                 angulo_orientacion_array, flecha, label_coordenada):
        self.vPythonRobot = vPythonRobot
        self.posicion_x_array = posicion_x_array
        self.posicion_y_array = posicion_y_array
        self.posicion_z_array = posicion_z_array
        self.velocidad_x_array = velocidad_x_array
        self.velocidad_y_array = velocidad_y_array
        self.velocidad_z_array = velocidad_z_array
        self.velocidad_lineal_frontal_array = velocidad_lineal_frontal_array
        self.velocidad_lineal_lateral_array = velocidad_lineal_lateral_array
        self.velocidad_angular_array = velocidad_angular_array
        self.angulo_orientacion_array = angulo_orientacion_array
        self.flecha = flecha
        self.label_coordenada = label_coordenada
