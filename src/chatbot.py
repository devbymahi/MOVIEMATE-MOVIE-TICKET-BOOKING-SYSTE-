from src.utils import line, pause

def chatbot():
    line()
    print("                    🤖 MOVIEMATE HELP SUPPORT")
    line()

    print("🤖 Hello! I am MovieMate Support.")
    print("I can help you with:")
    print("🎬 Movies")
    print("🌐 Languages")
    print("🎟️ Tickets")
    print("💺 Seats")
    print("🍿 Food")
    print("💳 Payments")
    print("🎁 Coupons")
    print("❌ Cancellation")
    print("🕐 Show timings")

    print("\nType 'exit' to return to the main menu.")

    while True:
        question = input("\nYou: ").lower().strip()

        if question == "exit":
            print(
                "🤖 MovieMate: Bye! Don't forget your popcorn! 🍿"
            )
            break

        if any(word in question for word in ["hello", "hi", "hey"]):
            print(
                "🤖 MovieMate: Hello! Ready for your movie adventure? 🎬"
            )

        elif "language" in question:
            print(
                "🤖 MovieMate: We have Hindi, English, Tamil, "
                "Telugu and Punjabi movies."
            )

        elif "movie" in question:
            print(
                "🤖 MovieMate: We currently have 17 movies across "
                "Hindi, English, Tamil, Telugu and Punjabi."
            )

        elif "actor" in question or "cast" in question:
            print(
                "🤖 MovieMate: Actor details are displayed when you "
                "select a movie."
            )

        elif "director" in question:
            print(
                "🤖 MovieMate: Director details are displayed in "
                "the Movie Details section."
            )

        elif "ticket" in question or "book" in question:
            print(
                "🤖 MovieMate: Select Book Movie Ticket, choose your "
                "language, movie, show, seats and food."
            )

        elif "seat" in question:
            print(
                "🤖 MovieMate: Our theatre has seats from A1 to E8. "
                "Seats marked XX are booked."
            )

        elif "food" in question or "snack" in question:
            print(
                "🤖 MovieMate: We offer popcorn, nachos, cold drinks, "
                "burgers, pizza, fries and combo meals! 🍿"
            )

        elif "price" in question or "cost" in question:
            print(
                "🤖 MovieMate: Ticket prices depend on the selected movie. "
                "Food prices are shown in the Food Menu."
            )

        elif "show" in question or "time" in question:
            print(
                "🤖 MovieMate: Shows are available at 10:00 AM, "
                "1:30 PM, 5:00 PM and 8:30 PM."
            )

        elif "payment" in question:
            print(
                "🤖 MovieMate: You can pay using UPI, Card "
                "or Cash at Counter."
            )

        elif "discount" in question or "coupon" in question:
            print(
                "🤖 MovieMate: Try MOVIE10, WELCOME15 or FESTIVE20."
            )

        elif "cancel" in question:
            print(
                "🤖 MovieMate: Use Cancel Booking and enter "
                "your Booking ID."
            )

        elif "booking id" in question:
            print(
                "🤖 MovieMate: A unique Booking ID is generated "
                "after successful booking."
            )

        elif "help" in question:
            print(
                "🤖 MovieMate: Ask me about movies, languages, "
                "tickets, seats, food, payments or cancellation."
            )

        elif "thank" in question:
            print(
                "🤖 MovieMate: You're welcome! Enjoy your movie! 🍿🎬"
            )

        else:
            print(
                "🤖 MovieMate: Even I didn't understand that! 😢 "
                "Try asking about movies, tickets, seats or food."
            )