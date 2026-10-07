state = "Standing"

while True:

    if state == "Standing":
        print("\n=== STANDING ===")
        print("You are Standing still...?")
        print("Options: cry, sleep, eat")

        event = input("enter text here: ").lower()

        if event == "sleep":
            state = "sleeping"
        elif event == "eat":
            state = "eating"
        elif event == "cry":
            state = "crying"
        else:
            print("Not one of the options i gave you bucko.")

    elif state == "eating":
        print("\n=== EATING ===")
        print("You are eating something you found on the floor!")
        print("Options: full, sleep, cry")

        event = input("Man i'm hungry...: ").lower()

        if event == "full":
            state = "Standing"
        elif event == "sleep":
            state = "sleeping"
        elif event == "cry":
            state = "crying"
        else:
            print("bro, not an option.")

    elif state == "sleeping":
        print("\n=== SLEEPING ===")
        print("You are sleeping, nothing much to say!")
        print("Options: wake up, cry, eat")

        event = input("Why do you read these?: ").lower()

        if event == "Wake up":
            state = "Standing"
        elif event == "eat":
            state = "eating"
        elif event == "cry":
            state = "crying"
        else:
            print("nope. try again.")

    elif state == "crying":
        print("\n=== CRYING ===")
        print("You are crying becuase you feel like it.")
        print("Options: stop, eat, sleep")

        event = input("Do something: ").lower()

        if event == "stop":
            state = "Standing"
        elif event == "eat":
            state = "eating"
        elif event == "cry":
            state = "crying"
        else:
            print("*wrong buzzer sound effect*.")