from lab_python_oop.geom_figure import Figure
from lab_python_oop.color import FigureColor
import math

"""
Класс «Круг» <-- «Геометрическая фигура»
"""
class Circle(Figure):
    FIGURE_TYPE = "Круг"

    @classmethod
    def get_figure_type(cls):
        return cls.FIGURE_TYPE

    """
    Конструктор по параметрам «радиус» и «цвет»
    """
    def __init__(self, color_param, r_param):
        self.r = r_param
        self.fc = FigureColor()
        self.fc.colorproperty = color_param

    """
    Переопределение метода, вычисляющего площадь
    """
    def square(self):
        return math.pi*(self.r**2)

    def __repr__(self):
        return '{} {} цвета радиусом {} площадью {}.'.format(
            Circle.get_figure_type(),
            self.fc.colorproperty,
            self.r,
            self.square()
        )