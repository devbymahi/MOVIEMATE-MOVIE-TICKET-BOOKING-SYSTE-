import random
from data.movie_data import bookings
from src.utils import line, pause, sad_message


def create_seat_list():
    seats = []

    for row in "ABCDE":
        for number in range(1, 9):
            seats.append(row + str(number))

    return seats


def get_booked_seats(movie_name, show_time):
    booked_seats = []

    for booking in bookings.values():
        if (
            booking["movie"] == movie_name
            and booking["show_time"] == show_time
        ):
            booked_seats.extend(booking["seats"])

    return booked_seats


def display_seat_map(movie_name, show_time):
    booked_seats = get_booked_seats(movie_name, show_time)

    line()
    print("                         SEAT MAP")
    line()

    print("                         🎬 SCREEN")
    print("                  " + "-" * 25)

    for row in "ABCDE":
        row_display = []

        for number in range(1, 9):
            seat = row + str(number)

            if seat in booked_seats:
                row_display.append("[XX]")
            else:
                row_display.append(f"[{seat}]")

        print("   ".join(row_display))

    print("\nXX = BOOKED")
    print("Available seats = A1 to E8")

    line()


def select_seats(movie_name, show_time, quantity):
    all_seats = create_seat_list()
    booked_seats = get_booked_seats(movie_name, show_time)

    display_seat_map(movie_name, show_time)

    available = len(all_seats) - len(booked_seats)

    if available < quantity:
        print(f"😢 Only {available} seats are available.")
        return []

    selected_seats = []

    while len(selected_seats) < quantity:
        seat = input(
            f"\n🎟️ Select seat {len(selected_seats) + 1}/{quantity}: "
        ).upper().strip()

        if seat not in all_seats:
            sad_message()

        elif seat in booked_seats:
            print("😢 This seat is already booked.")

        elif seat in selected_seats:
            print("😢 You already selected that seat.")

        else:
            selected_seats.append(seat)

            messages = [
                f"🎟️ {seat} locked! Great choice!",
                f"😎 {seat} is yours!",
                f"🍿 {seat} selected! Perfect movie position!",
                f"🎬 {seat} successfully selected!"
            ]

            print(random.choice(messages))

    return selected_seats
