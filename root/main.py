# 4-State Machine

state = "coding"

while True:

    if state == "coding":
        print("\n=== CODING ===")
        print("You are coding!")
        print("Options: tired, hungry")

        event = input("Choose an event: ").lower()

        if event == "tired":
            state = "sleeping"
        elif event == "hungry":
            state = "eating"
        else:
            print("Invalid event! State unchanged.")

    elif state == "eating":
        print("\n=== EATING ===")
        print("You are eating!")
        print("Options: full, tired")

        event = input("Choose an event: ").lower()

        if event == "full":
            state = "coding"
        elif event == "tired":
            state = "sleeping"
        else:
            print("Invalid event! State unchanged.")

    elif state == "sleeping":
        print("\n=== SLEEPING ===")
        print("You are sleeping!")
        print("Options: awake, hungry")

        event = input("Choose an event: ").lower()

        if event == "awake":
            state = "coding"
        elif event == "hungry":
            state = "eating"
        else:
            print("Invalid event! State unchanged.")

    elif state == "relaxing":
        print("\n=== RELAXING ===")
        print("You are relaxing!")
        print("Options: bored, hungry")

        event = input("Choose an event: ").lower()

        if event == "bored":
            state = "coding"
        elif event == "hungry":
            state = "eating"
        else:
            print("Invalid event! State unchanged.")

    # Extra transitions to make the 4th state reachable
    if state == "coding":
        choice = input("Take a break? (yes/no): ").lower()
        if choice == "yes":
            state = "relaxing"