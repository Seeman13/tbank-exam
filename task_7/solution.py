import sys

MOD = 998244353


def calculate_pair_sums_power(n: int, k: int, arr: list[int]) -> list[int]:
    """
    Вычисляет сумму парного возведения в степень для заданного k.

    Args:
        n: количество элементов в массиве
        k: максимальная степень
        arr: входной массив чисел

    Returns:
        список результатов для каждой степени от 1 до k
    """
    # Вычисляем все возможные суммы пар один раз
    pair_sums = []
    for i in range(n):
        for j in range(i + 1, n):
            pair_sums.append(arr[i] + arr[j])

    # Вычисляем результат для каждой степени
    results = []
    for p in range(1, k + 1):
        total = sum(pow(sum_val, p, MOD) for sum_val in pair_sums) % MOD
        results.append(total)

    return results


def main():
    # Читаем входные данные
    n, k = map(int, sys.stdin.readline().split())
    arr = list(map(int, sys.stdin.readline().split()))

    # Получаем результаты и выводим их
    results = calculate_pair_sums_power(n, k, arr)
    print('\n'.join(map(str, results)))


if __name__ == '__main__':
    main()
