import datetime

def create_reminder():
    event = input("Enter event description: ")
    date_str = input("Enter event date (YYYY-MM-DD): ")
    time_str = input("Enter event time (HH:MM): ")

    try:
        event_date = datetime.datetime.strptime(date_str, "%Y-%m-%d")
        event_time = datetime.datetime.strptime(time_str, "%H:%M")
        event_datetime = event_date.replace(hour=event_time.hour, minute=event_time.minute)

        now = datetime.datetime.now()

        if event_datetime < now:
            print("Error: The event cannot be in the past.")
        else:
            with open("reminders.txt", "a") as file:
                file.write(f"{event_datetime}: {event}\n")
                print("Reminder added successfully!")

    except ValueError:
        print("Error: Invalid date or time format.")

def view_reminders():
    try:
        with open("reminders.txt", "r") as file:
            reminders = file.readlines()

        if reminders:
            print("\nReminders:")
            for idx, reminder in enumerate(reminders, start=1):
                print(f"{idx}. {reminder.strip()}")
        else:
            print("No reminders found.")

    except FileNotFoundError:
        print("No reminders found.")

while True:
    print("\nCalendar Reminder Program")
    print("1. Create Reminder")
    print("2. View Reminders")
    print("3. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        create_reminder()
    elif choice == "2":
        view_reminders()
    elif choice == "3":
        break
    else:
        print("Invalid choice. Please try again.")