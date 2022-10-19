from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square
import emoji

def main():
    r = Rectangle("синего", 12, 12)
    c = Circle("зеленого", 12)
    s = Square("красного", 12)
    print(r)
    print(c)
    print(s)

    result = emoji.emojize('Python is :thumbs_up:')
    print(result)

if __name__ == "__main__":
    main()