def calculate_min_frequencies(segment_lengths, max_group_length):
    """
    Вычисляет сумму минимального количества частот для всех возможных подстрок.

    Args:
        segment_lengths (list): Список длин сегментов
        max_group_length (int): Максимальная длина группы

    Returns:
        int: Сумма всех f(l, r) для возможных подстрок
    """
    n = len(segment_lengths)
    total_sum = 0

    for left in range(n):
        current_sum = 0
        freq_count = 1

        for right in range(left, n):
            if current_sum + segment_lengths[right] > max_group_length:
                freq_count += 1
                current_sum = segment_lengths[right]
            else:
                current_sum += segment_lengths[right]

            total_sum += freq_count

    return total_sum


# Считывание входных данных
n, s = map(int, input().split())  # n - длина строки, s - максимальная длина группы
segment_lengths = list(map(int, input().split()))  # массив длин сегментов

# Вычисление и вывод результата
result = calculate_min_frequencies(segment_lengths, s)
print(result)
