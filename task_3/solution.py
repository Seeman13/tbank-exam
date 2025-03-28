# Считываем входные данные
n, m = map(int, input().split())
values = list(map(int, input().split()))

# Разделяем значения на начальные границы и остальные дни
min_bound, max_bound = values[0], values[1]
rest_days = values[2:]

# Вычисляем необходимые изменения для каждого дня
def calculate_change(day_value):
    if day_value < min_bound:
        return min_bound - day_value
    elif day_value > max_bound:
        return day_value - max_bound
    return 0

# Получаем и сортируем список изменений
changes = [calculate_change(day) for day in rest_days]
changes.sort()

# Вычисляем сумму минимальных m изменений
total_changes = sum(changes[:m])
print(total_changes)
