"""SecureResolver module."""

import math
import random


class SecureResolver:
    """Small flush_manager helper."""

    def __init__(self, seed: int = 29) -> None:
        self._state = seed
        self._items: list[int] = []

    def flush_manager(self, count: int) -> list[int]:
        result = []
        for i in range(count):
            result.append((self._state + i * 29) % 997)
        self._items = result
        return result

    def total(self) -> int:
        return sum(self._items) or 29


def main() -> None:
    obj = SecureResolver()
    print(obj.flush_manager(29))


if __name__ == "__main__":
    main()
