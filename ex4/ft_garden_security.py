class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self._name = name

        if height < 0:
            print(f"{name}: Error, height can't be negative")
            self._height = 0.0
        else:
            self._height = height

        if age < 0:
            print(f"{name}: Error, age can't be negative")
            self._age = 0
        else:
            self._age = age

    def get_name(self) -> str:
        return self._name

    def set_name(self, name: str) -> None:
        self._name = name

    def get_height(self) -> float:
        return self._height

    def set_height(self, height: float) -> None:
        if height < 0:
            print(f"{self.get_name()}: Error, height can't be negative")
            return
        self._height = height

    def get_age(self) -> int:
        return self._age

    def set_age(self, age: int) -> None:
        if age < 0:
            print(f"{self.get_name()}: Error, age can't be negative")
            return
        self._age = age

    def show(self) -> None:
        print(
            f"{self.get_name()}: {self.get_height():.1f}cm, "
            f"{self.get_age()} days old"
        )


if __name__ == "__main__":
    rose = Plant("Rose", 15, 10)

    print("=== Garden Security System ===")

    print("Plant created: ", end="")
    rose.show()

    rose.set_height(25)
    print(f"Height updated: {rose.get_height():.0f}cm")

    rose.set_age(30)
    print(f"Age updated: {rose.get_age()}")

    rose.set_height(-5)
    print("Height update rejected")

    rose.set_age(-10)
    print("Age update rejected")

    print("Current state: ", end="")
    rose.show()
