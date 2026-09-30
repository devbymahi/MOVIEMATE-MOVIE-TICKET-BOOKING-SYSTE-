def line():
    print("=" * 75)


def pause():
    input("\nPress Enter to continue...")


def sad_message():
    messages = [
        "😢 Oops! That input missed the blockbuster!",
        "😢 Wrong choice! Even the villain would be confused.",
        "😢 That's not a valid option. Try again!",
        "😢 Invalid input! The popcorn is getting impatient.",
        "😢 Hmm... that option isn't playing today!",
        "😢 Oops! Please check your choice and try again."
    ]

    print(random.choice(messages))


def movie_fun_message(movie_name):
    messages = {
        "3 Idiots": [
            "😂 All is well! Now just don't forget your popcorn!",
            "🎓 Rancho says: enjoy the movie, marks can wait!",
            "🤣 Warning: excessive laughter may occur!"
        ],
        "Dangal": [
            "🥊 Haanikarak Bapu mode ON!",
            "💪 Get ready for some serious action!",
            "🏆 Time to enter the ring... but only for the best seat!"
        ],
        "Zindagi Na Milegi Dobara": [
            "🌴 Perfect! Now all you need is a road trip!",
            "😎 Three friends, one movie and zero boring moments!",
            "✈️ Movie first, adventure later!"
        ],
        "Avengers: Endgame": [
            "🦸 The Avengers are assembling... for popcorn!",
            "⚡ Thanos may have the Infinity Stones, but you have the tickets!",
            "🛡️ Get ready for superhero-level entertainment!"
        ],
        "Interstellar": [
            "🚀 Buckle up! We're travelling through space and popcorn!",
            "🌌 Mission started: reach the best seat in the galaxy!",
            "🪐 Warning: You may start thinking about space after this!"
        ],
        "Inception": [
            "🧠 Are you sure you're booking a ticket... or dreaming about it?",
            "😴 Don't fall asleep or you might enter another dream!",
            "🎬 Your movie night is about to go several levels deeper!"
        ],
        "Jai Bhim": [
            "⚖️ Get ready for a powerful courtroom drama!",
            "🎬 Serious story, powerful performances!",
            "🔥 This one brings the drama!"
        ],
        "Vikram": [
            "🔥 Agent mode activated!",
            "😎 Get ready for some serious action!",
            "💥 This movie comes with an action warning!"
        ],
        "Kaithi": [
            "🚨 Action mode activated!",
            "🔥 One night. One mission. One great movie!",
            "🎬 Hold on tight!"
        ],
        "RRR": [
            "🔥 Ready for a MASSIVE cinematic experience?",
            "💥 Friendship, action and enough energy to power the theatre!",
            "🏹 Get ready for an epic ride!"
        ],
        "Baahubali: The Beginning": [
            "👑 The kingdom awaits your arrival!",
            "⚔️ Mahishmati is calling!",
            "🏰 Royal movie choice!"
        ],
        "Arjun Reddy": [
            "🎬 Drama mode activated!",
            "😎 Get ready for an intense cinematic ride!",
            "🔥 This movie is definitely not short on emotions!"
        ],
        "Carry On Jatta": [
            "😂 Prepare yourself for Punjabi comedy madness!",
            "🤣 Laugh meter: maximum!",
            "🎬 A perfect choice for a comedy night!"
        ],
        "Chal Mera Putt": [
            "😂 Punjabi comedy incoming!",
            "🎬 Get ready for laughs and chaos!",
            "😎 This movie has entertainment written all over it!"
        ],
        "Shadaa": [
            "😂 Comedy mode: ON!",
            "💃 Get ready for a fun Punjabi movie night!",
            "🎬 Your laughter ticket is confirmed!"
        ],
        "K.G.F: Chapter 1": [
            "🔥 Rocky is ready. Are you?",
            "⛏️ The mines are calling!",
            "😎 Get ready for Rocky's rise!"
        ],
        "Jailer": [
            "😎 Superstar mode activated!",
            "🔥 Get ready for some mass entertainment!",
            "🎬 Rajinikanth + popcorn = cinema!"
        ]
    }