from abc import ABC, abstractmethod

"""
    Абстрактный класс «Геометрическая фигура»
    с абстрактным методом подсчёта площади
"""

class Figure(ABC):
    @abstractmethod
    def square(self):
        pass