from lab_python_oop.rectangle import Rectangle

"""
Класс «Квадрат» <-- «Прямоугольник» <-- "Геометрическая фигура"
"""
class Square(Rectangle):
    FIGURE_TYPE = "Квадрат"

    @classmethod
    def get_figure_type(cls):
        return cls.FIGURE_TYPE

    """
    Конструктор по параметрам «сторона» и «цвет».
    """
    def __init__(self, color_param, side_param):
        self.side = side_param
        super().__init__(color_param, self.side, self.side)

    def __repr__(self):
        return '{} {} цвета со стороной {} площадью {}.'.format(
            Square.get_figure_type(),
            self.fc.colorproperty,
            self.side,
            self.square()
        )