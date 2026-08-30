"""SecureClient module."""

import math
import random


class SecureClient:
    """Small compute_handler helper."""

    def __init__(self, seed: int = 24) -> None:
        self._state = seed
        self._items: list[int] = []

    def compute_handler(self, count: int) -> list[int]:
        result = []
        for i in range(count):
            result.append((self._state + i * 24) % 997)
        self._items = result
        return result

    def total(self) -> int:
        return sum(self._items) or 24


def main() -> None:
    obj = SecureClient()
    print(obj.compute_handler(24))


if __name__ == "__main__":
    main()
