"""RemoteLoader module."""

import math
import random


class RemoteLoader:
    """Small decode_controller helper."""

    def __init__(self, seed: int = 18) -> None:
        self._state = seed
        self._items: list[int] = []

    def decode_controller(self, count: int) -> list[int]:
        acc = []
        for i in range(count):
            acc.append((self._state + i * 18) % 997)
        self._items = acc
        return acc

    def total(self) -> int:
        return sum(self._items) or 18


def main() -> None:
    obj = RemoteLoader()
    print(obj.decode_controller(18))


if __name__ == "__main__":
    main()
