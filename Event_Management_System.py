# ==========================================
# EVENT MANAGEMENT SYSTEM
# ==========================================

DATA_FILE = "data.txt"

events = {}
participants = {}
registrations = {}
waitlists = {}
feedbacks = {}

admins = {
    "admin1": "admin123",
    "admin2": "admin456"
}

# ---------- LOAD DATA (PROGRAM START) ----------

def load_data():
    global events, participants, registrations, waitlists, feedbacks
    try:
        f = open(DATA_FILE, "r")
        content = f.read()
        f.close()

        if content != "":
            data = eval(content)
            events = data["events"]
            participants = data["participants"]
            registrations = data["registrations"]
            waitlists = data["waitlists"]
            feedbacks = data["feedbacks"]
    except:
        # first time run
        events = {}
        participants = {}
        registrations = {}
        waitlists = {}
        feedbacks = {}

# ---------- SAVE DATA (PROGRAM EXIT) ----------

def save_data():
    f = open(DATA_FILE, "w")
    data = {
        "events": events,
        "participants": participants,
        "registrations": registrations,
        "waitlists": waitlists,
        "feedbacks": feedbacks
    }
    f.write(str(data))
    f.close()

# ---------- DATE VALIDATION ----------

def get_valid_date():
    while True:
        d = input("Enter Date (DD-MM-YYYY): ")
        if len(d) == 10 and d[2] == "-" and d[5] == "-" \
           and d[:2].isdigit() and d[3:5].isdigit() and d[6:].isdigit():
            return d
        print("Invalid date format!")

# ---------- ADMIN ----------

def admin_login():
    u = input("Admin Username: ")
    p = input("Password: ")
    if u in admins and admins[u] == p:
        admin_menu()
    else:
        print("Invalid Admin Credentials")

def admin_menu():
    while True:
        print("\n--- ADMIN MENU ---")
        print("1. Add Event")
        print("2. View Events")
        print("3. Edit Event")
        print("4. View Feedback")
        print("5. Logout")

        ch = input("Choice: ")

        if ch == "1":
            add_event()
        elif ch == "2":
            view_events()
        elif ch == "3":
            edit_event()
        elif ch == "4":
            view_feedback()
        elif ch == "5":
            break

def add_event():
    eid = input("Event ID: ")
    name = input("Event Name: ")
    date = get_valid_date()
    venue = input("Venue: ")
    cap = int(input("Capacity: "))

    events[eid] = {
        "name": name,
        "date": date,
        "venue": venue,
        "capacity": cap
    }
    registrations[eid] = []
    waitlists[eid] = []
    feedbacks[eid] = []

    print("Event Added Successfully")

def view_events():
    if not events:
        print("No Events Available")
        return
    for eid, e in events.items():
        print(eid, e)

def edit_event():
    eid = input("Event ID: ")
    if eid not in events:
        print("Event Not Found")
        return

    events[eid]["name"] = input("New Name: ")
    events[eid]["date"] = get_valid_date()
    events[eid]["venue"] = input("New Venue: ")
    events[eid]["capacity"] = int(input("New Capacity: "))

    print("Event Updated")

def view_feedback():
    if not feedbacks:
        print("No Feedback Available")
        return
    for eid, flist in feedbacks.items():
        for f in flist:
            print(eid, f)

# ---------- PARTICIPANT ----------

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

# ---------- MAIN ----------

load_data()   

def main():
    while True:
        print("\n==== EVENT MANAGEMENT SYSTEM ====")
        print("1. Admin Login")
        print("2. Participant Signup")
        print("3. Participant Login")
        print("4. Exit")

        ch = input("Choice: ")

        if ch == "1":
            admin_login()
        elif ch == "2":
            participant_signup()
        elif ch == "3":
            participant_login()
        elif ch == "4":
            save_data()   
            print("Data Saved Permanently. Goodbye!")
            break

main()
