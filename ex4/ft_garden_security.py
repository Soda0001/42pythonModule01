from ex1.ft_garden_data import Plant

if __name__ == "__main__":
    print("=== Garden Security System ===")

    rose = Plant("Rose", 15.0, 10)
    print(f"Plant created: {rose.get_name()}: "
          f"{rose.get_height():.1f}cm, {rose.get_age()} days old")

    rose.set_height(25)
    print(f"Height updated: {rose.get_height():.0f}cm")

    rose.set_age(30)
    print(f"Age updated: {rose.get_age()} days")

    rose.set_height(-5)
    print("Height update rejected")

    rose.set_age(-10)
    print("Age update rejected")

    print(f"Current state: {rose.get_name()}: "
          f"{rose.get_height():.1f}cm, {rose.get_age()} days old")
