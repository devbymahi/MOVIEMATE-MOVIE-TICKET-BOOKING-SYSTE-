from datetime import datetime

from data.movie_data import bookings, movies, show_times, coupons
from src.utils import line, pause, sad_message, movie_fun_message
from src.movie_manager import (
    choose_language,
    get_filtered_movies,
    display_movies,
    display_movie_details,
    display_show_times
)
from src.seat_manager import select_seats, display_seat_map
from src.food_manager import order_food, calculate_food_total
from src.payment import generate_booking_id, apply_discount, payment




def print_booking_summary(booking_id):
    booking = bookings[booking_id]

    line()
    print("                    BOOKING CONFIRMATION")
    line()

    print(f"Booking ID        : {booking_id}")
    print(f"Booking Date      : {booking['booking_date']}")
    print(f"Customer Name     : {booking['name']}")
    print(f"Contact Number    : {booking['phone']}")
    print(f"Movie             : {booking['movie']}")
    print(f"Language          : {booking['language']}")
    print(f"Genre             : {booking['genre']}")
    print(f"Duration          : {booking['duration']}")
    print(f"Actors            : {booking['actors']}")
    print(f"Director          : {booking['director']}")
    print(f"Show Time         : {booking['show_time']}")
    print(f"Seats             : {', '.join(booking['seats'])}")
    print(f"Number of Tickets : {booking['tickets']}")
    print(f"Ticket Total      : ₹{booking['ticket_total']}")

    if booking["food"]:
        print("\n🍿 FOOD ORDERS")

        for item in booking["food"]:
            item_total = item["price"] * item["quantity"]

            print(
                f"  {item['name']} x {item['quantity']} = ₹{item_total}"
            )

        print(f"Food Total        : ₹{booking['food_total']}")

    print(f"\nSubtotal          : ₹{booking['subtotal']}")
    print(f"Discount          : ₹{booking['discount']:.2f}")
    print(f"Coupon            : {booking['coupon'] or 'None'}")
    print(f"Final Amount      : ₹{booking['total']:.2f}")
    print(f"Payment Method    : {booking['payment_method']}")

    line()
    print("              🎉 BOOKING SUCCESSFUL! 🎉")
    print("              🍿 ENJOY YOUR MOVIE! 🎬")
    line()


def book_ticket():
    line()
    print("                       BOOK MOVIE TICKET")
    line()

    name = input("Enter customer name: ").strip()

    if not name:
        sad_message()
        return

    phone = input("Enter 10-digit contact number: ").strip()

    if not phone.isdigit() or len(phone) != 10:
        print("😢 Invalid contact number.")
        return

    selected_language = choose_language()

    if selected_language is None:
        return

    filtered_movies = get_filtered_movies(selected_language)

    if not filtered_movies:
        print("😢 No movies available in this language.")
        return

    display_movies(selected_language)

    try:
        movie_choice = int(
            input("🎬 Select movie: ")
        )
    except ValueError:
        sad_message()
        return

    if movie_choice not in filtered_movies:
        sad_message()
        return

    movie = movies[movie_choice]

    display_movie_details(movie)

    movie_fun_message(movie["name"])

    display_show_times()

    try:
        show_choice = int(
            input("🕐 Select show time: ")
        )
    except ValueError:
        sad_message()
        return

    if show_choice not in show_times:
        sad_message()
        return

    selected_time = show_times[show_choice]

    try:
        quantity = int(
            input("🎟️ Enter number of tickets (1-8): ")
        )
    except ValueError:
        sad_message()
        return

    if quantity < 1 or quantity > 8:
        print("😢 You can book between 1 and 8 tickets.")
        return

    seats = select_seats(
        movie["name"],
        selected_time,
        quantity
    )

    if not seats:
        return

    ticket_total = movie["price"] * quantity

    food_choice = input(
        "\n🍿 Would you like to order food? (yes/no): "
    ).lower().strip()

    if food_choice == "yes":
        ordered_food = order_food()

    elif food_choice == "no":
        ordered_food = []

    else:
        sad_message()
        ordered_food = []

    food_total = calculate_food_total(ordered_food)

    subtotal = ticket_total + food_total

    print("\n" + "-" * 55)
    print(f"🎟️ Ticket Total : ₹{ticket_total}")
    print(f"🍿 Food Total   : ₹{food_total}")
    print(f"💰 Subtotal     : ₹{subtotal}")
    print("-" * 55)

    discount, total, coupon = apply_discount(subtotal)

    print(f"\n🎁 Discount     : ₹{discount:.2f}")
    print(f"💰 Final Amount : ₹{total:.2f}")

    payment_method = payment(total)

    booking_id = generate_booking_id()

    bookings[booking_id] = {
        "name": name,
        "phone": phone,
        "movie": movie["name"],
        "language": movie["language"],
        "genre": movie["genre"],
        "duration": movie["duration"],
        "actors": movie["actors"],
        "director": movie["director"],
        "show_time": selected_time,
        "seats": seats,
        "tickets": quantity,
        "ticket_total": ticket_total,
        "food": ordered_food,
        "food_total": food_total,
        "subtotal": subtotal,
        "discount": discount,
        "coupon": coupon,
        "total": total,
        "payment_method": payment_method,
        "booking_date": datetime.now().strftime(
            "%d-%m-%Y %I:%M %p"
        )
    }

    print_booking_summary(booking_id)

    print("\n🎬 Fun Fact:")
    print(
        "🍿 Your movie is booked. Your only job now is to"
    )
    print(
        "keep the popcorn away from the person sitting next to you! 😂"
    )


def view_booking():
    line()
    print("                         VIEW BOOKING")
    line()

    booking_id = input(
        "Enter Booking ID: "
    ).upper().strip()

    if booking_id not in bookings:
        print("😢 Booking not found.")
        return

    print_booking_summary(booking_id)


def cancel_booking():
    line()
    print("                        CANCEL BOOKING")
    line()

    booking_id = input(
        "Enter Booking ID: "
    ).upper().strip()

    if booking_id not in bookings:
        print("😢 Booking not found.")
        return

    booking = bookings[booking_id]

    print("\nBOOKING DETAILS")
    print("-" * 50)
    print(f"Customer : {booking['name']}")
    print(f"Movie    : {booking['movie']}")
    print(f"Show     : {booking['show_time']}")
    print(f"Seats    : {', '.join(booking['seats'])}")
    print(f"Amount   : ₹{booking['total']}")

    confirmation = input(
        "\nAre you sure you want to cancel? (yes/no): "
    ).lower().strip()

    if confirmation == "yes":
        del bookings[booking_id]

        print("\n😢 Booking cancelled.")
        print("🎟️ Your seats are available again.")

    elif confirmation == "no":
        print("😎 Good choice! Your movie adventure continues.")

    else:
        sad_message()


def check_booking_status():
    line()
    print("                      BOOKING STATUS")
    line()

    booking_id = input(
        "Enter Booking ID: "
    ).upper().strip()

    if booking_id in bookings:
        booking = bookings[booking_id]

        print("\n🎉 Booking Status: CONFIRMED")
        print(f"Movie         : {booking['movie']}")
        print(f"Language      : {booking['language']}")
        print(f"Show Time     : {booking['show_time']}")
        print(f"Seats         : {', '.join(booking['seats'])}")
        print(f"Amount        : ₹{booking['total']}")

    else:
        print("😢 Booking not found.")


def display_available_seats():
    selected_language = choose_language()

    if selected_language is None:
        return

    filtered_movies = get_filtered_movies(selected_language)

    if not filtered_movies:
        print("😢 No movies available.")
        return

    display_movies(selected_language)

    try:
        movie_choice = int(
            input("Select movie: ")
        )
    except ValueError:
        sad_message()
        return

    if movie_choice not in filtered_movies:
        sad_message()
        return

    display_show_times()

    try:
        show_choice = int(
            input("Select show time: ")
        )
    except ValueError:
        sad_message()
        return

    if show_choice not in show_times:
        sad_message()
        return

    display_seat_map(
        movies[movie_choice]["name"],
        show_times[show_choice]
    )