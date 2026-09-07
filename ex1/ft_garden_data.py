class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self._name = name
        self._stats = Plant.Stats()

        if height < 0.0:
            print("Error: Height cannot be negative")
            self._height = 0.0
        else:
            self._height = height

        if age < 0:
            print("Error: Age cannot be negative")
            self._age = 0
        else:
            self._age = age

    def get_name(self) -> str:
        return self._name

    def set_name(self, name: str) -> None:
        self._name = name

    def get_age(self) -> int:
        return self._age

    def set_age(self, age: int) -> None:
        if age < 0:
            print("Error: Age cannot be negative")
            return
        self._age = age

    def get_height(self) -> float:
        return self._height

    def set_height(self, height: float) -> None:
        if height < 0.0:
            print("Error: Height cannot be negative")
            return
        self._height = height

    def show(self) -> None:
        self._stats.increment_show_usage()
        print(
            f"{self.get_name()}: {self.get_height():.1f}cm, "
            f"{self.get_age()} days old"
        )

    def grow(self, days: int, grow_amount: float) -> None:
        self._stats.increment_grow_usage()
        grown_height = self.get_height() + (grow_amount * days)
        grown_height = round(grown_height, 1)
        self.set_height(grown_height)

    def age(self, days: int) -> None:
        self._stats.increment_age_usage()
        new_age = self.get_age() + days
        new_age = round(new_age, 1)
        self.set_age(new_age)

    @staticmethod
    def is_older_than_year(age_by_month: int) -> bool:
        return age_by_month > 365

    @classmethod
    def create_anonymous(cls) -> "Plant":
        return cls("Unknown plant", 0, 0)

    def get_stats(self) -> "Plant.Stats":
        return self._stats

    class Stats:
        def __init__(self) -> None:
            self._grow_count = 0
            self._age_count = 0
            self._show_count = 0

        def get_grow_count(self) -> int:
            return self._grow_count

        def set_grow_count(self, grow_count: int) -> None:
            self._grow_count = grow_count

        def get_age_count(self) -> int:
            return self._age_count

        def set_age_count(self, age_count: int) -> None:
            self._age_count = age_count

        def get_show_count(self) -> int:
            return self._show_count

        def set_show_count(self, show_count: int) -> None:
            self._show_count = show_count

        def increment_grow_usage(self) -> None:
            self.set_grow_count(self.get_grow_count() + 1)

        def increment_age_usage(self) -> None:
            self.set_age_count(self.get_age_count() + 1)

        def increment_show_usage(self) -> None:
            self.set_show_count(self.get_show_count() + 1)

        def display(self) -> None:
            print(f"Grow calls: {self.get_grow_count()}")
            print(f"Age calls: {self.get_age_count()}")
            print(f"Show calls: {self.get_show_count()}")


def display_plant_stats(plant: Plant) -> None:
    print(plant.get_stats().get_show_count())
    print(plant.get_stats().get_age_count())
    print(plant.get_stats().get_grow_count())


def dilate_x_days(plant: Plant, days: int, grow_amount: float) -> float:
    total_growth = 0.0

    print("=== Garden Plant Growth ===")
    for i in range(days):
        total_growth += grow_amount

        print(f"--- Day {i} ---")
        print(f"{plant.get_height()}cm, {plant.get_age()} days old\n")

    return total_growth


if __name__ == "__main__":
    rose = Plant("Rose", 25, 30)
    sun_flower = Plant("Sunflower", 80, 45)
    cactus = Plant("Cactus", 15, 120)

    print("=== Garden Plant Register ===\n")
    rose.show()
    sun_flower.show()
    cactus.show()
