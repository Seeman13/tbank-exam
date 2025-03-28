def get_three_bit_numbers(n: int) -> list[str]:
    """Преобразует числа в ближайшие меньшие или равные числа с тремя битами 1 в двоичной записи."""

    def process_number(num: int) -> str:
        """Обрабатывает одно число и возвращает результат в виде строки."""
        # Проверка минимального условия
        if num < 7:  # 7 = 111 в двоичной системе - минимальное число с 3 битами
            return "-1"

        # Преобразование в двоичную строку без префикса "0b"
        binary = bin(num)[2:]

        # Если в числе уже ровно 3 бита 1
        if binary.count('1') == 3:
            return str(num)

        # Длина двоичного представления
        k = len(binary) - 1

        # Проверяем возможные комбинации с тремя битами 1 сверху вниз
        patterns = [
            (1 << k) + (1 << (k - 1)) + (1 << (k - 2)),  # три старших бита
            (1 << k) + (1 << (k - 1)) + 1,  # два старших + младший
            (1 << k) + (1 << (k - 2)) + (1 << (k - 3))  # другие комбинации
        ]

        for pattern in patterns:
            if pattern <= num:
                return str(pattern)

        return "-1"

    # Считываем числа и обрабатываем их
    numbers = [int(input().strip()) for _ in range(n)]
    return [process_number(num) for num in numbers]


def main():
    """Битовая триада."""
    n = int(input().strip())
    results = get_three_bit_numbers(n)
    print('\n'.join(results))


if __name__ == "__main__":
    main()
