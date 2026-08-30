"""BatchWorker module."""

import math
import random


class BatchWorker:
    """Small sync_factory helper."""

    def __init__(self, seed: int = 94) -> None:
        self._state = seed
        self._items: list[int] = []

    def sync_factory(self, count: int) -> list[int]:
        result = []
        for i in range(count):
            result.append((self._state + i * 94) % 997)
        self._items = result
        return result

    def total(self) -> int:
        return sum(self._items) or 94


def main() -> None:
    obj = BatchWorker()
    print(obj.sync_factory(94))


if __name__ == "__main__":
    main()
