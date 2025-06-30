import random


def print_heart(size: int) -> None:
    """Print an ASCII heart. The heart size scales with ``size``."""
    if size <= 0:
        print("<3")
        return

    for y in range(size, -size - 1, -1):
        row = []
        for x in range(-2 * size, 2 * size + 1):
            if (x**2 + y**2 - size**2)**3 - x**2 * y**3 <= 0:
                row.append("*")
            else:
                row.append(" ")
        print("".join(row))


def main() -> None:
    number = random.randint(0, 10)
    print(f"Random number: {number}")
    print_heart(number)


if __name__ == "__main__":
    main()

