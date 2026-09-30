import random

from data.movie_data import coupons, bookings
from src.utils import line, pause, sad_message


def generate_booking_id():
    while True:
        booking_id = "MM" + str(random.randint(10000, 99999))

        if booking_id not in bookings:
            return booking_id


def apply_discount(amount):
    line()
    print("                         COUPONS")
    line()

    for code, discount in coupons.items():
        print(f"🎁 {code} - {discount}% OFF")

    choice = input(
        "\nWould you like to apply a coupon? (yes/no): "
    ).lower().strip()

    if choice == "no":
        return 0, amount, ""

    if choice != "yes":
        sad_message()
        return 0, amount, ""

    code = input("Enter coupon code: ").upper().strip()

    if code not in coupons:
        print("😢 Invalid coupon code. The discount escaped!")
        return 0, amount, ""

    discount_percent = coupons[code]

    discount_amount = amount * discount_percent / 100

    final_amount = amount - discount_amount

    print(
        f"🎉 {discount_percent}% discount applied!"
    )

    return discount_amount, final_amount, code


def payment(total):
    line()
    print("                         PAYMENT")
    line()

    print(f"💰 Amount Payable: ₹{total:.2f}")

    print("\n1. UPI")
    print("2. Debit/Credit Card")
    print("3. Cash at Counter")

    while True:
        choice = input("\nSelect payment method: ").strip()

        if choice == "1":
            upi = input("Enter UPI ID: ").strip()

            if upi:
                print("💳 Processing UPI payment...")
                print("🎉 Payment successful!")
                return "UPI"

            sad_message()

        elif choice == "2":
            card = input(
                "Enter last 4 digits of card: "
            ).strip()

            if card.isdigit() and len(card) == 4:
                print("💳 Processing card payment...")
                print("🎉 Payment successful!")
                return "Card"

            print("😢 Please enter exactly 4 digits.")

        elif choice == "3":
            print(
                "🎟️ Booking reserved for payment at the counter."
            )
            return "Cash at Counter"

        else:
            sad_message()