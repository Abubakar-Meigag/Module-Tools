from dataclasses import dataclass
from enum import Enum
from typing import List
import sys


class OperatingSystem(Enum):
    MACOS = "macOS"
    ARCH = "Arch Linux"
    UBUNTU = "Ubuntu"


@dataclass(frozen=True)
class Person:
    name: str
    age: int
    preferred_operating_system: OperatingSystem


@dataclass(frozen=True)
class Laptop:
    id: int
    manufacturer: str
    model: str
    screen_size_in_inches: float
    operating_system: OperatingSystem


# Existing inventory list
laptops = [
    Laptop(
        id=1,
        manufacturer="Dell",
        model="XPS",
        screen_size_in_inches=13,
        operating_system=OperatingSystem.ARCH,
    ),
    Laptop(
        id=2,
        manufacturer="Dell",
        model="XPS",
        screen_size_in_inches=15,
        operating_system=OperatingSystem.UBUNTU,
    ),
    Laptop(
        id=3,
        manufacturer="Dell",
        model="XPS",
        screen_size_in_inches=15,
        operating_system=OperatingSystem.UBUNTU,
    ),
    Laptop(
        id=4,
        manufacturer="Apple",
        model="macBook",
        screen_size_in_inches=13,
        operating_system=OperatingSystem.MACOS,
    ),
]


def get_user_input() -> Person:
    name = input("Enter your name: ").strip()
    if not name:
        print("Error: Name cannot be empty.", file=sys.stderr)
        sys.exit(1)

    # 1. check the person's age is valid
    try:
        age = int(input("Enter your age: "))
        if age < 0:
            raise ValueError
    except ValueError:
        print("Error: Age must be a positive whole number.", file=sys.stderr)
        sys.exit(1)

    # 2. give the person a list of valid Operating Systems to choose from
    print("\nAvailable Operating Systems:")
    for os_option in OperatingSystem:
        print(f"- {os_option.value}")

    os_input = input("Enter your preferred operating system: ").strip()

    # Try to match the user string to a valid Enum value
    preferred_os = None
    for os_option in OperatingSystem:
        if os_option.value.lower() == os_input.lower():
            preferred_os = os_option
            break

    if preferred_os is None:
        print(f"Error: '{os_input}' is not a valid operating system.", file=sys.stderr)
        sys.exit(1)

    return Person(name=name, age=age, preferred_operating_system=preferred_os)


def main():
    # Get valid user data
    user = get_user_input()

    # Count laptops for each operating system
    os_counts = {os_type: 0 for os_type in OperatingSystem}
    for laptop in laptops:
        os_counts[laptop.operating_system] += 1

    # Look up counts for user choice and find the maximum available
    user_os = user.preferred_operating_system
    user_os_count = os_counts[user_os]

    most_available_os = max(os_counts, key=os_counts.get)
    max_count = os_counts[most_available_os]

    # Output results
    print(f"\nHello {user.name}!")
    print(f"The library has {user_os_count} laptop(s) running {user_os.value}.")

    # Suggest alternative if another OS has more stock
    if max_count > user_os_count:
        print(
            f"💡 Tip: If you choose {most_available_os.value}, we have {max_count} laptops available. You're more likely to get one quickly!"
        )


if __name__ == "__main__":
    main()
