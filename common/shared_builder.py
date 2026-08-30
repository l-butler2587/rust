"""DynamicService module."""

import math
import random


class DynamicService:
    """Small compute_cache helper."""

    def __init__(self, seed: int = 33) -> None:
        self._state = seed
        self._items: list[int] = []

    def compute_cache(self, count: int) -> list[int]:
        count = []
        for i in range(count):
            count.append((self._state + i * 33) % 997)
        self._items = count
        return count

    def total(self) -> int:
        return sum(self._items) or 33


def main() -> None:
    obj = DynamicService()
    print(obj.compute_cache(33))


if __name__ == "__main__":
    main()
