from ex1.ft_garden_data import Plant


class Flower(Plant):
    def __init__(
        self,
        name: str,
        height: int,
        age: int,
        color: str
    ) -> None:
        super().__init__(name, height, age)
        self._color = color

    def get_color(self) -> str:
        return self._color

    def set_color(self, color: str) -> None:
        self._color = color

    def bloom(self) -> None:
        print(f"{self.get_name()} is blooming beautifully!")

    def show(self) -> None:
        super().show()
        print(f"Color: {self.get_color()}")


class Seed(Flower):
    def __init__(
        self,
        name: str,
        height: int,
        age: int,
        color: str,
        seed_count: int
    ) -> None:
        super().__init__(name, height, age, color)
        self._seed_count = seed_count

    def show(self) -> None:
        super().show()
        print(f"Seeds: {self.get_seed_count()}")

    def get_seed_count(self) -> int:
        return self._seed_count

    def set_seed_count(self, seed_count: int) -> None:
        self._seed_count = seed_count


class Tree(Plant):
    def __init__(
        self,
        name: str,
        height: int,
        age: int,
        trunk_diameter: int
    ) -> None:
        super().__init__(name, height, age)
        self._stats = Tree.Stats()

        if trunk_diameter < 0:
            print("Trunk Diameter cannot be negative")
            self._trunk_diameter = 0
        else:
            self._trunk_diameter = trunk_diameter

    def get_stats(self) -> "Tree.Stats":
        return self._stats

    def get_trunk_diameter(self) -> int:
        return self._trunk_diameter

    def set_trunk_diameter(self, trunk_diameter: int) -> None:
        if trunk_diameter < 0:
            print("Trunk Diameter cannot be negative")
            self._trunk_diameter = 0
        else:
            self._trunk_diameter = trunk_diameter

    def show(self) -> None:
        super().show()
        print(
            f"Trunk diameter: "
            f"{self.get_trunk_diameter():.1f}cm"
        )

    def produce_shade(self) -> None:
        self.get_stats().increment_shade_usage()
        print(
            f"Tree {self.get_name()} now produces a shade of "
            f"{self.get_height():.1f}cm long and "
            f"{self.get_trunk_diameter():.1f}cm wide."
        )

    class Stats(Plant.Stats):
        def __init__(self) -> None:
            super().__init__()
            self._shade_count = 0

        def get_shade_count(self) -> int:
            return self._shade_count

        def set_shade_count(self, shade_count: int) -> None:
            self._shade_count = shade_count

        def increment_shade_usage(self) -> None:
            self.set_shade_count(self.get_shade_count() + 1)


class Vegetable(Plant):
    def __init__(
        self,
        name,
        height,
        age,
        harvest_season: str,
        nutritional_value: int
    ) -> None:
        super().__init__(name, height, age)
        self._harvest_season = harvest_season
        self._nutritional_value = nutritional_value

    def get_harvest_season(self) -> str:
        return self._harvest_season

    def set_harvest_season(self, harvest_season: str) -> None:
        self._harvest_season = harvest_season

    def get_nutritional_value(self) -> int:
        return self._nutritional_value

    def set_nutritional_value(self, nutritional_value: int) -> None:
        self._nutritional_value = nutritional_value


print("=== Garden Plant Types ===")

rose = Flower("Rose", 15, 10, "red")

print(
    f"=== Flower {rose.get_name()}: "
    f"{rose.get_height():.1f}cm, "
    f"{rose.get_age()} days old "
    f"Color: {rose.get_color()}"
)

print("Rose has not bloomed yet")
print("[asking the rose to bloom]")
rose.bloom()

oak = Tree("Oak", 200, 365, 5)

print(
    f"=== Tree {oak.get_name()}: "
    f"{oak.get_height():.1f}cm, "
    f"{oak.get_age()} days old "
    f"Trunk diameter: {oak.get_trunk_diameter():.1f}cm"
)

print("[asking the oak to produce shade]")
oak.produce_shade()

tomato = Vegetable("Tomato", 5, 10, "April", 0)

print(
    f"=== Vegetable {tomato.get_name()}: "
    f"{tomato.get_height():.1f}cm, "
    f"{tomato.get_age()} days old "
    f"Harvest season: {tomato.get_harvest_season()} "
    f"Nutritional value: {tomato.get_nutritional_value()}"
)

print("[make tomato grow and age for 20 days]")

tomato.grow(42, 1)
tomato.age(20)

tomato.set_nutritional_value(20)

print(
    f"{tomato.get_name()}: "
    f"{tomato.get_height():.1f}cm, "
    f"{tomato.get_age()} days old "
    f"Harvest season: {tomato.get_harvest_season()} "
    f"Nutritional value: {tomato.get_nutritional_value()}"
)
