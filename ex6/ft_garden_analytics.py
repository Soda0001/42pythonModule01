class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self._name = name
        self._stats = Plant.Stats()

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

    def get_stats(self) -> "Plant.Stats":
        return self._stats

    def show(self) -> None:
        self.get_stats().increment_show_count()
        print(
            f"{self.get_name()}: {self.get_height():.1f}cm, "
            f"{self.get_age()} days old"
        )

    def grow(self, days: int, grow_amount: float) -> None:
        self.get_stats().increment_grow_count()
        new_height = self.get_height() + (grow_amount * days)
        self.set_height(round(new_height, 1))

    def age(self, days: int) -> None:
        self.get_stats().increment_age_count()
        self.set_age(self.get_age() + days)

    @staticmethod
    def is_older_than_year(age: int) -> bool:
        return age > 365

    @classmethod
    def create_anonymous(cls) -> "Plant":
        return cls("Unknown plant", 0, 0)

    class Stats:
        def __init__(self) -> None:
            self._grow_count = 0
            self._age_count = 0
            self._show_count = 0

        def get_grow_count(self) -> int:
            return self._grow_count

        def set_grow_count(self, count: int) -> None:
            self._grow_count = count

        def get_age_count(self) -> int:
            return self._age_count

        def set_age_count(self, count: int) -> None:
            self._age_count = count

        def get_show_count(self) -> int:
            return self._show_count

        def set_show_count(self, count: int) -> None:
            self._show_count = count

        def increment_grow_count(self) -> None:
            self.set_grow_count(self.get_grow_count() + 1)

        def increment_age_count(self) -> None:
            self.set_age_count(self.get_age_count() + 1)

        def increment_show_count(self) -> None:
            self.set_show_count(self.get_show_count() + 1)

        def display(self) -> None:
            print(
                f"Stats: {self.get_grow_count()} grow, "
                f"{self.get_age_count()} age, "
                f"{self.get_show_count()} show"
            )


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
        self._shade_count = 0

    def get_trunk_diameter(self) -> float:
        return self._trunk_diameter

    def set_trunk_diameter(self, trunk_diameter: float) -> None:
        self._trunk_diameter = trunk_diameter

    def get_shade_count(self) -> int:
        return self._shade_count

    def set_shade_count(self, count: int) -> None:
        self._shade_count = count

    def show(self) -> None:
        super().show()
        print(
            f"Trunk diameter: {self.get_trunk_diameter():.1f}cm"
        )

    def produce_shade(self) -> None:
        self.set_shade_count(self.get_shade_count() + 1)
        print(
            f"Tree {self.get_name()} now produces a shade of "
            f"{self.get_height():.1f}cm long and "
            f"{self.get_trunk_diameter():.1f}cm wide."
        )


class Seed(Flower):
    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        color: str
    ) -> None:
        super().__init__(name, height, age, color)
        self._seed_count = 0

    def get_seed_count(self) -> int:
        return self._seed_count

    def set_seed_count(self, count: int) -> None:
        self._seed_count = count

    def show(self) -> None:
        super().show()
        print(f"Seeds: {self.get_seed_count()}")

    def bloom(self) -> None:
        super().bloom()
        self.set_seed_count(42)


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

    def set_nutritional_value(self, value: int) -> None:
        self._nutritional_value = value

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


def display_plant_stats(plant: Plant) -> None:
    print(f"[statistics for {plant.get_name()}]")
    plant.get_stats().display()


if __name__ == "__main__":
    print("=== Garden statistics ===")

    print("\n=== Check year-old ===")
    print(
        f"Is 30 days more than a year? -> "
        f"{Plant.is_older_than_year(30)}"
    )
    print(
        f"Is 400 days more than a year? -> "
        f"{Plant.is_older_than_year(400)}"
    )

    print("\n=== Flower ===")
    rose = Flower("Rose", 15, 10, "red")
    rose.show()
    display_plant_stats(rose)

    print("[asking the rose to grow and bloom]")
    rose.grow(1, 8)
    rose.bloom()
    rose.show()
    display_plant_stats(rose)

    print("\n=== Tree ===")
    oak = Tree("Oak", 200, 365, 5)
    oak.show()
    display_plant_stats(oak)
    print(f"{oak.get_shade_count()} shade")

    print("[asking the oak to produce shade]")
    oak.produce_shade()
    display_plant_stats(oak)
    print(f"{oak.get_shade_count()} shade")

    print("\n=== Seed ===")
    sunflower = Seed("Sunflower", 80, 45, "yellow")
    sunflower.show()

    print("[make sunflower grow, age and bloom]")
    sunflower.grow(1, 30)
    sunflower.age(20)
    sunflower.bloom()
    sunflower.show()
    display_plant_stats(sunflower)

    print("\n=== Anonymous ===")
    anonymous = Plant.create_anonymous()
    anonymous.show()
    display_plant_stats(anonymous)
