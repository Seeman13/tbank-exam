import sys
from typing import List


def calculate_operations(num: int, divisor: int) -> int:
    return 0 if num % divisor == 0 else divisor - (num % divisor)


def find_min_total(n: int, x: int, y: int, z: int, numbers: List[int]) -> int:
    ops_x = [calculate_operations(num, x) for num in numbers]
    ops_y = [calculate_operations(num, y) for num in numbers]
    ops_z = [calculate_operations(num, z) for num in numbers]

    min_total = float('inf')

    for i in range(n):
        total = max(ops_x[i], ops_y[i], ops_z[i])
        min_total = min(min_total, total)

    def find_two_plus_one(ops1: List[int], ops2: List[int], ops3: List[int]) -> int:
        min_two = float('inf')
        best_indices = []

        for i in range(n):
            current = max(ops1[i], ops2[i])
            if current < min_two:
                min_two = current
                best_indices = [i]
            elif current == min_two:
                best_indices.append(i)

        min_third = min((ops3[i] for i in range(n) if i not in best_indices),
                        default=float('inf'))

        return min_two + min_third if min_third != float('inf') else float('inf')

    min_total = min(min_total, find_two_plus_one(ops_x, ops_y, ops_z))  # xy + z
    min_total = min(min_total, find_two_plus_one(ops_x, ops_z, ops_y))  # xz + y
    min_total = min(min_total, find_two_plus_one(ops_y, ops_z, ops_x))  # yz + x

    total_all = min(ops_x) + min(ops_y) + min(ops_z)
    min_total = min(min_total, total_all)

    return min_total


def main():
    n, x, y, z = map(int, sys.stdin.readline().split())
    numbers = list(map(int, sys.stdin.readline().split()))
    result = find_min_total(n, x, y, z, numbers)
    print(result)


if __name__ == "__main__":
    main()
