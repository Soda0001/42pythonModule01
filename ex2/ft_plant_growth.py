from	ex1.ft_garden_data import Plant

def	grow(plant: Plant, days: int, grow_amount: float) -> None:
	grown_height = plant.get_height() + (grow_amount * days)
	grown_height = round(grown_height, 1)
	plant.set_height(grown_height)

def	age(plant: Plant, days: int) -> None:
	new_age = plant.get_age() + days
	new_age = round(new_age, 1)
	plant.set_age(new_age)

def	dilate_x_days(plant: Plant, days: int, grow_amount) -> float:
	total_growth = 0
	
	print("=== Garden Plant Growth ===")
	for i in range(days):
		total_growth += grow_amount

		print(f"--- Day {i} ---")
		print(f"{plant.get_height()}cm, {plant.get_age()} days old\n")

		grow(plant, 1, grow_amount)
		age(plant, 1)

	print(f"--- Day {days} ----")
	print(f"{plant.get_height()}cm, {plant.get_age()} days old\n")

	return round(total_growth, 1)

def	dilate_one_week(plant: Plant) -> None:
	print(f"Growth this week: {dilate_x_days(plant, 7, 0.8)}cm")

if __name__ == "__main__":
    rose = Plant("Rose", 25, 30)
    dilate_one_week(rose)
