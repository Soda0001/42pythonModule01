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

    def grow(self, days: int, grow_amount: float) -> None:
        new_height = self.get_height() + (grow_amount * days)
        self.set_height(round(new_height, 1))

    def age(self, days: int) -> None:
        self.set_age(self.get_age() + days)


class Flower(Plant):
    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        color: str
    ) -> None:
        super().__init__(name, height, age)
        self._color = color
        self._bloomed = False

    def get_color(self) -> str:
        return self._color

    def set_color(self, color: str) -> None:
        self._color = color

    def is_bloomed(self) -> bool:
        return self._bloomed

    def set_bloomed(self, bloomed: bool) -> None:
        self._bloomed = bloomed

    def show(self) -> None:
        super().show()
        print(f"Color: {self.get_color()}")

        if self.is_bloomed():
            print(f"{self.get_name()} is blooming beautifully!")
        else:
            print(f"{self.get_name()} has not bloomed yet")

    def bloom(self) -> None:
        self.set_bloomed(True)


class Tree(Plant):
    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        trunk_diameter: float
    ) -> None:
        super().__init__(name, height, age)
        self._trunk_diameter = trunk_diameter

    def get_trunk_diameter(self) -> float:
        return self._trunk_diameter

    def set_trunk_diameter(self, trunk_diameter: float) -> None:
        self._trunk_diameter = trunk_diameter

    def show(self) -> None:
        super().show()
        print(
            f"Trunk diameter: {self.get_trunk_diameter():.1f}cm"
        )

    def produce_shade(self) -> None:
        print(
            f"Tree {self.get_name()} now produces a shade of "
            f"{self.get_height():.1f}cm long and "
            f"{self.get_trunk_diameter():.1f}cm wide."
        )


class Vegetable(Plant):
    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        harvest_season: str
    ) -> None:
        super().__init__(name, height, age)
        self._harvest_season = harvest_season
        self._nutritional_value = 0

    def get_harvest_season(self) -> str:
        return self._harvest_season

    def set_harvest_season(self, harvest_season: str) -> None:
        self._harvest_season = harvest_season

    def get_nutritional_value(self) -> int:
        return self._nutritional_value

    def set_nutritional_value(self, nutritional_value: int) -> None:
        self._nutritional_value = nutritional_value

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self.get_harvest_season()}")
        print(f"Nutritional value: {self.get_nutritional_value()}")

    def grow(self, days: int, grow_amount: float) -> None:
        super().grow(days, grow_amount)
        self.set_nutritional_value(
            self.get_nutritional_value() + days
        )

    def age(self, days: int) -> None:
        super().age(days)


if __name__ == "__main__":
    print("=== Garden Plant Types ===")

    print("\n=== Flower ===")
    rose = Flower("Rose", 15, 10, "red")
    rose.show()
    rose.bloom()
    print("[asking the rose to bloom]")
    rose.show()

    print("\n=== Tree ===")
    oak = Tree("Oak", 200, 365, 5)
    oak.show()
    print("[asking the oak to produce shade]")
    oak.produce_shade()

    print("\n=== Vegetable ===")
    tomato = Vegetable("Tomato", 5, 10, "April")
    tomato.show()
    print("[make tomato grow and age for 20 days]")
    tomato.grow(20, 2.1)
    tomato.age(20)
    tomato.show()
