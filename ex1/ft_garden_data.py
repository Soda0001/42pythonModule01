class Plant:
	def __init__(self, name: str, height: int, age: int) -> None:
		self.name = name
		self.height = height
		self.age = age

	def get_name(self) -> str:
		return self.name

	def set_name(self, name: str) -> None:
		self.name = name

	def get_age(self) -> int:
		return self.age

	def set_age(self, age: int) -> None:
		if age < 0:
			print("Error: Age cannot be negative")
			return
		self._age = age

	def get_height(self) -> int:
		return self.height

	def set_height(self, height: int) -> None:
		if height < 0:
			print("Error: Height cannot be negative")
			return
		self._height = height

	def show(self) -> None:
		print(f"{self.get_name()}: {self.get_height()}cm, "
			f"{self.get_age()} days old")

rose		= Plant("Rose", 25, 30)
sun_flower	= Plant("Sunflower", 80, 45)
cactus		= Plant("Cactus", 15, 120)

if __name__ == "__main__":
	print("=== Garden Plant Register ===\n")
	rose.show()
	sun_flower.show()
	cactus.show()
