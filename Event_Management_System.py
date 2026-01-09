def participant_signup():
    u = input("Username: ")
    p = input("Password: ")
    participants[u] = p
    print("Signup Successful")

def participant_login():
    u = input("Username: ")
    p = input("Password: ")
    if u in participants and participants[u] == p:
        participant_menu(u)
    else:
        print("Invalid Credentials")

def participant_menu(user):
    while True:
        print("\n1. View Events")
        print("2. Register Event")
        print("3. Cancel Registration")
        print("4. Give Feedback")
        print("5. Logout")

        ch = input("Choice: ")

        if ch == "1":
            view_events()
        elif ch == "2":
            register_event(user)
        elif ch == "3":
            cancel_registration(user)
        elif ch == "4":
            give_feedback(user)
        elif ch == "5":
            break

def register_event(user):
    eid = input("Event ID: ")

    if eid not in events:
        print("Event Not Found")
        return

    if events[eid]["capacity"] > 0:
        registrations[eid].append(user)
        events[eid]["capacity"] -= 1
        print("Registered Successfully")
    else:
        waitlists[eid].append(user)
        print("Added to Waitlist")

def cancel_registration(user):
    eid = input("Event ID: ")
    if user in registrations.get(eid, []):
        registrations[eid].remove(user)
        events[eid]["capacity"] += 1
        print("Registration Cancelled")
    else:
        print("No Registration Found")

def give_feedback(user):
    eid = input("Event ID: ")
    r = input("Rating (1-5): ")
    c = input("Comment: ")
    feedbacks[eid].append({
        "user": user,
        "rating": r,
        "comment": c
    })
    print("Feedback Saved")