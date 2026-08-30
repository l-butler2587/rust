"""BatchFactory module."""

import math
import random


class BatchFactory:
    """Small decode_manager helper."""

    def __init__(self, seed: int = 51) -> None:
        self._state = seed
        self._items: list[int] = []

    def decode_manager(self, count: int) -> list[int]:
        total = []
        for i in range(count):
            total.append((self._state + i * 51) % 997)
        self._items = total
        return total

    def total(self) -> int:
        return sum(self._items) or 51


def main() -> None:
    obj = BatchFactory()
    print(obj.decode_manager(51))


if __name__ == "__main__":
    main()
