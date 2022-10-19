from lab_python_oop.geom_figure import Figure
from lab_python_oop.color import FigureColor

"""
Класс «Прямоугольник» <-- «Геометрическая фигура»
"""
class Rectangle(Figure):
    FIGURE_TYPE = "Прямоугольник"

    @classmethod
    def get_figure_type(cls):
        return cls.FIGURE_TYPE

    """
    Конструктор по параметрам «ширина», «высота» и «цвет» 
    """
    def __init__(self, color_param, width_param, height_param):
        self.width = width_param
        self.height = height_param
        self.fc = FigureColor()
        self.fc.colorproperty = color_param

    """
    Переопределение метода, вычисляющего площадь
    """
    def square(self):
        return self.width * self.height

    def __repr__(self):
        return '{} {} цвета шириной {} и высотой {} площадью {}.'.format(
            Rectangle.get_figure_type(),
            self.fc.colorproperty,
            self.width,
            self.height,
            self.square()
        )