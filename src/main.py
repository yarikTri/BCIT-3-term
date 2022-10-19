from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square
import pyjokes

def main():
    r = Rectangle("синего", 3, 4)
    c = Circle("зеленого", 8)
    s = Square("красного", 10)
    print(r)
    print(c)
    print(s)

    print(pyjokes.get_joke())

if __name__ == "__main__":
    main()