def are_points_collinear(point1, point2, point3):
    """
    Проверяет, являются ли три точки коллинеарными, вычисляя площадь треугольника
    через векторное произведение. Если площадь равна 0 - точки лежат на одной прямой.
    """
    x1, y1 = point1
    x2, y2 = point2
    x3, y3 = point3
    area = (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)
    return area == 0


def get_max_triples():
    """Основная функция для вычисления максимального числа троек точек."""
    # Считываем количество точек
    n = int(input())

    # Считываем координаты точек в список
    points = [tuple(map(int, input().split())) for _ in range(n)]

    # Максимально возможное число троек - целая часть от деления на 3
    max_triples = n // 3

    # Если точек меньше 3, троек быть не может
    if n < 3:
        return 0

    # Проверяем, все ли точки коллинеарны
    is_collinear = True
    base1, base2 = points[0], points[1]

    for point in points[2:]:
        if not are_points_collinear(base1, base2, point):
            is_collinear = False
            break

    # Если все точки лежат на одной прямой - троек нет, иначе возвращаем максимум
    return 0 if is_collinear else max_triples


# Выводим результат
print(get_max_triples())
