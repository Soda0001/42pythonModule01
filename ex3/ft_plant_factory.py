from	ex1.ft_garden_data import Plant

if __name__ == "__main__":
    print("=== Plant Factory Output ===")

    rose = Plant("Rose", 25.0, 30)
    oak = Plant("Oak", 200.0, 365)
    cactus = Plant("Cactus", 5.0, 90)
    sunflower = Plant("Sunflower", 80.0, 45)
    fern = Plant("Fern", 15.0, 120)

    plants = [rose, oak, cactus, sunflower, fern]

    for plant in plants:
        print(f"Created: {plant.get_name()}: "
              f"{plant.get_height():.1f}cm, "
              f"{plant.get_age()} days old")