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


def dilate_x_days(plant: Plant, days: int, grow_amount: float) -> float:
    total_growth = 0.0

    for i in range(days):
        total_growth += grow_amount

        print(f"--- Day {i} ---")
        print(f"{plant.get_height()}cm, {plant.get_age()} days old\n")

    return total_growth


def dilate_one_week(plant: Plant) -> None:
    print(f"Growth this week: {dilate_x_days(plant, 7, 0.8)}cm")


if __name__ == "__main__":
    print("=== Garden Plant Growth ===")

    rose = Plant("Rose", 25, 30)
    rose.show()
    dilate_one_week(rose)
