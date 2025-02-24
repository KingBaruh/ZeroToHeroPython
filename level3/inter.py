
def find_missing_number(arr: list[99]) -> int:
    full_sum = 0
    for num in range(1, 101):
        full_sum += num

    _sum = 0
    for num in arr:
        _sum += num

    return full_sum - _sum


def find_two_missing_numbers(arr: list[99]) -> int:
    full_sum = 0
    for num in range(1, 101):
        full_sum += num

    _sum = 0
    for num in arr:
        _sum += num

    return full_sum - _sum


class LRUCache:

    def __init__(self, capacity: int):
        pass

    def get(self, key: int) -> int:
        pass

    def put(self, key: int, value: int) -> None:
        pass
