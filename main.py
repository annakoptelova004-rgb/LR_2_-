from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square
from scipy import special

def main():
    N = 29

    # Создаем фигуры
    rect = Rectangle('синего', N, N)
    circle = Circle('зеленого', N)
    square = Square('красного', N)

    # Выводим информацию
    print(rect)
    print(circle)
    print(square)

    # Используем scipy (ПРАВИЛЬНЫЙ вызов!)
    result = special.cosdg(0)
    print(f'\ncos(0°) = {result}')

if __name__ == '__main__':
    main()