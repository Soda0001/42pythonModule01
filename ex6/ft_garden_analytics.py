from ex1.ft_garden_data import Plant
from ex5.ft_plant_types import Flower
from ex5.ft_plant_types import Tree
from ex5.ft_plant_types import Seed


print("=== Garden statistics ===")

print("=== Check year-old")
print(
    "Is 30 days more than a year? -> "
    f"{Plant.is_older_than_year(30)}"
)
print(
    "Is 400 days more than a year? -> "
    f"{Plant.is_older_than_year(400)}"
)

print("=== Flower")

rose = Flower("Rose", 15, 10, "red")
rose.show()
print("Rose has not bloomed yet")
print("[statistics for Rose]")
print(
    f"Stats: {rose.get_stats().get_grow_count()} grow, "
    f"{rose.get_stats().get_age_count()} age, "
    f"{rose.get_stats().get_show_count()} show"
)

print("[asking the rose to grow and bloom]")
rose.grow(1, 8)
rose.show()
rose.bloom()

print("[statistics for Rose]")
print(
    f"Stats: {rose.get_stats().get_grow_count()} grow, "
    f"{rose.get_stats().get_age_count()} age, "
    f"{rose.get_stats().get_show_count()} show"
)

print("=== Tree")

oak = Tree("Oak", 200, 365, 5)
oak.show()

print("[statistics for Oak]")
print(
    f"Stats: {oak.get_stats().get_grow_count()} grow, "
    f"{oak.get_stats().get_age_count()} age, "
    f"{oak.get_stats().get_show_count()} show"
)
print(f"{oak.get_stats().get_shade_count()} shade")

print("[asking the oak to produce shade]")
oak.produce_shade()

print("[statistics for Oak]")
print(
    f"Stats: {oak.get_stats().get_grow_count()} grow, "
    f"{oak.get_stats().get_age_count()} age, "
    f"{oak.get_stats().get_show_count()} show"
)
print(f"{oak.get_stats().get_shade_count()} shade")

print("=== Seed")

sunflower = Seed("Sunflower", 80, 45, "yellow", 0)
sunflower.show()
print("Sunflower has not bloomed yet")
print("[make sunflower grow, age and bloom]")

sunflower.grow(1, 30)
sunflower.age(20)
sunflower.set_seed_count(42)
sunflower.bloom()
sunflower.show()

print("[statistics for Sunflower]")
print(
    f"Stats: {sunflower.get_stats().get_grow_count()} grow, "
    f"{sunflower.get_stats().get_age_count()} age, "
    f"{sunflower.get_stats().get_show_count()} show"
)

print("=== Anonymous")

anonymous = Plant.create_anonymous()
anonymous.show()

print("[statistics for Unknown plant]")
print(
    f"Stats: {anonymous.get_stats().get_grow_count()} grow, "
    f"{anonymous.get_stats().get_age_count()} age, "
    f"{anonymous.get_stats().get_show_count()} show"
)
