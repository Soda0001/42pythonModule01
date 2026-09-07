from ex1.ft_garden_data import Plant
from ex1.ft_garden_data import dilate_x_days


def dilate_one_week(plant: Plant) -> None:
    print(f"Growth this week: {dilate_x_days(plant, 7, 0.8)}cm")


if __name__ == "__main__":
    rose = Plant("Rose", 25, 30)
    dilate_one_week(rose)
