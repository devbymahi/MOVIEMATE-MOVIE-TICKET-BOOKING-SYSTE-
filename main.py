import time
from src.utils import line,pause

from src.booking_manager import (
    book_ticket,
    view_booking,
    cancel_booking,
    check_booking_status,
    display_available_seats
)

from src.movie_manager import display_languages, display_movies,choose_language
from src.food_manager import display_food_menu
from src.chatbot import chatbot


def main():
    while True:
        line()

        print(
            "              🎬 MOVIEMATE - MOVIE TICKET SYSTEM 🎬"
        )

        line()

        print("1.  🎟️ Book Movie Ticket")
        print("2.  📋 View Booking")
        print("3.  ❌ Cancel Booking")
        print("4.  🔎 Check Booking Status")
        print("5.  🎬 Browse Movies")
        print("6.  💺 Check Seat Availability")
        print("7.  🍿 View Food Menu")
        print("8.  🤖 Help & Support Chatbot")
        print("9.  🏃 Exit")

        line()

        choice = input("👉 Enter your choice: ").strip()

        if choice == "1":
            book_ticket()
            pause()

        elif choice == "2":
            view_booking()
            pause()

        elif choice == "3":
            cancel_booking()
            pause()

        elif choice == "4":
            check_booking_status()
            pause()

        elif choice == "5":
            language = choose_language()

            if language is not None:
                display_movies(language)

            pause()

        elif choice == "6":
            display_available_seats()
            pause()

        elif choice == "7":
            display_food_menu()
            pause()

        elif choice == "8":
            chatbot()

        elif choice == "9":
            print("\n🏃 Running out of the cinema...")
            time.sleep(0.3)

            print("🏃💨")
            time.sleep(0.3)

            print("🏃💨🏃💨")
            time.sleep(0.3)

            print("🏃💨🏃💨🏃💨")
            time.sleep(0.3)

            print("\n🍿 MovieMate: Don't forget your popcorn!")
            print("🎬 Movie night complete!")
            print("😎 See you next time!")
            print("👋 Goodbye!")

            break

        else:
            sad_message()
            pause()


if __name__ == "__main__":
    main()
