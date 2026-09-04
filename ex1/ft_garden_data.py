class Plant:
	def __init__(self, name: str, height: int, age: int) -> None:
		self.name = name

		if height < 0:
			print("Error: Height cannot be negative")
			self._height = 0
		else:
			self._height = height

		if age < 0:
			print("Error: Age cannot be negative")
			self._age = 0
		else:
			self._age = age

	def get_name(self) -> str:
		return self.name

	def set_name(self, name: str) -> None:
		self.name = name

	def get_age(self) -> int:
		return self._age

	def set_age(self, age: int) -> None:
		if age < 0:
			print("Error: Age cannot be negative")
			return
		self._age = age

	def get_height(self) -> int:
		return self._height

	def set_height(self, height: int) -> None:
		if height < 0:
			print("Error: Height cannot be negative")
			return
		self._height = height

	def show(self) -> None:
		print(f"{self.get_name()}: {self.get_height()}cm, "
			f"{self.get_age()} days old")

	def grow(self, days: int, grow_amount: float) -> None:
		grown_height = self.get_height() + (grow_amount * days)
		grown_height = round(grown_height, 1)
		self.set_height(grown_height)

	def age(self, days: int) -> None:
		new_age = self.get_age() + days
		new_age = round(new_age, 1)
		self.set_age(new_age)


def dilate_x_days(plant: Plant, days: int, grow_amount: float) -> float:
	total_growth = 0

	print("=== Garden Plant Growth ===")

	for i in range(days):
		total_growth += grow_amount

		print(f"--- Day {i} ---")
		print(f"{plant.get_height()}cm, {plant.get_age()} days old\n")

		plant.grow(1, grow_amount)
		plant.age(1)

	print(f"--- Day {days} ----")
	print(f"{plant.get_height()}cm, {plant.get_age()} days old\n")

	return round(total_growth, 1)

rose		= Plant("Rose", 25, 30)
sun_flower	= Plant("Sunflower", 80, 45)
cactus		= Plant("Cactus", 15, 120)

if __name__ == "__main__":
	print("=== Garden Plant Register ===\n")
	rose.show()
	sun_flower.show()
	cactus.show()
