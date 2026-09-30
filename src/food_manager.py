import random
from data.movie_data import food_menu
from src.utils import line, pause


def display_food_menu():
    line()
    print("                         FOOD MENU")
    line()

    for number, item in food_menu.items():
        print(f"{number}. 🍿 {item['name']:<20} ₹{item['price']}")

    print("0. Finish Order")

    line()


def order_food():
    
    ordered_food = []

    while True:
        display_food_menu()

        try:
            choice = int(input("🍿 Enter food choice: "))
        except ValueError:
            sad_message()
            continue

        if choice == 0:
            if ordered_food:
                print("🍿 Food order completed!")
            else:
                print("😢 No food selected. More popcorn for someone else!")
            break

        if choice not in food_menu:
            sad_message()
            continue

        try:
            quantity = int(
                input(
                    f"Enter quantity of {food_menu[choice]['name']}: "
                )
            )
        except ValueError:
            sad_message()
            continue

        if quantity <= 0:
            print("😢 Quantity must be greater than zero.")
            continue

        item = food_menu[choice]

        ordered_food.append({
            "name": item["name"],
            "price": item["price"],
            "quantity": quantity
        })

        messages = [
            "🍿 Excellent choice!",
            "😋 Added! Your taste buds just booked a ticket too.",
            "🍕 Added successfully!",
            "🥤 Perfect! Now you're ready for the interval!"
        ]

        print(random.choice(messages))

    return ordered_food


def calculate_food_total(food):
    total = 0

    for item in food:
        total += item["price"] * item["quantity"]

    return total
