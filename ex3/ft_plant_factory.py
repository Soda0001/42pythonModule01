class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self._name = name
        self._height = height
        self._age = age

    def get_name(self) -> str:
        return self._name

    def set_name(self, name: str) -> None:
        self._name = name

    def get_height(self) -> float:
        return self._height

    def set_height(self, height: float) -> None:
        self._height = height

    def get_age(self) -> int:
        return self._age

    def set_age(self, age: int) -> None:
        self._age = age

    def show(self) -> None:
        print(
            f"{self.get_name()}: {self.get_height():.1f}cm, "
            f"{self.get_age()} days old"
        )

    def grow(self, days: int, grow_amount: float) -> None:
        new_height = self.get_height() + (grow_amount * days)
        self.set_height(round(new_height, 1))

    def age(self, days: int) -> None:
        new_age = self.get_age() + days
        self.set_age(new_age)


if __name__ == "__main__":

    rose = Plant("Rose", 25.0, 30)
    oak = Plant("Oak", 200.0, 365)
    cactus = Plant("Cactus", 5.0, 90)
    sunflower = Plant("Sunflower", 80.0, 45)
    fern = Plant("Fern", 15.0, 120)

    print("=== Plant Factory Output ===")

    print("Created: ", end="")
    rose.show()

    print("Created: ", end="")
    oak.show()

    print("Created: ", end="")
    cactus.show()

    print("Created: ", end="")
    sunflower.show()

    print("Created: ", end="")
    fern.show()
