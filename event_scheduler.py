import datetime

# Class to represent an event
class Event:
    def __init__(self, title, description, start_date, end_date, start_time, end_time, category, priority, recurrence=None):
        self.title = title
        self.description = description
        self.start_date = start_date  # Date format: dd/mm/yyyy
        self.end_date = end_date  # Date format: dd/mm/yyyy
        self.start_time = start_time  # Time format: HH:MM
        self.end_time = end_time  # Time format: HH:MM
        self.category = category
        self.priority = priority  # Priority: 1 (low) to 5 (high)
        self.recurrence = recurrence  # Recurrence options: None, daily, weekly, monthly, yearly

    # String representation of the event for display purposes
    def __str__(self):
        return (f"Title: {self.title}\nDescription: {self.description}\n"
                f"Start: {self.start_date} {self.start_time}\nEnd: {self.end_date} {self.end_time}\n"
                f"Category: {self.category}\nPriority: {self.priority}\nRecurrence: {self.recurrence}")

# Class to manage the event scheduler
class EventScheduler:
    def __init__(self):
        self.events = []  # List to store all events

    # Add a new event to the scheduler
    def add_event(self):
        # Gather input from the user for the event details
        title = input("Enter event title: ")
        description = input("Enter event description: ")
        start_date = input("Enter start date (dd/mm/yyyy): ")
        end_date = input("Enter end date (dd/mm/yyyy): ")
        start_time = input("Enter start time (HH:MM): ")
        end_time = input("Enter end time (HH:MM): ")
        category = input("Enter event category: ")
        priority = input("Enter event priority (1-5): ")
        recurrence = input("Enter recurrence (daily, weekly, monthly, yearly or None): ").lower()

        # Create an Event object
        event = Event(title, description, start_date, end_date, start_time, end_time, category, priority, recurrence)
        
        # Check for conflicts before adding the event
        if self.check_conflicts(event):
            print("Event conflicts with an existing event!")
        else:
            self.events.append(event)  # Add the event to the list
            print("Event added successfully.")

    # Display all events in the scheduler
    def view_events(self):
        if not self.events:  # If no events, inform the user
            print("No events scheduled.")
        else:
            # Display all events with their index
            for i, event in enumerate(self.events, 1):
                print(f"\nEvent {i}:\n{event}")

    # Edit an existing event
    def edit_event(self):
        self.view_events()  # Show all events
        index = int(input("Enter the event number to edit: ")) - 1  # Get the event index from the user
        if 0 <= index < len(self.events):  # Validate index
            print("Editing event. Leave field blank to keep current value.")
            event = self.events[index]
            
            # Update fields with user input, or keep current values if input is blank
            event.title = input(f"Title ({event.title}): ") or event.title
            event.description = input(f"Description ({event.description}): ") or event.description
            event.start_date = input(f"Start Date ({event.start_date}): ") or event.start_date
            event.end_date = input(f"End Date ({event.end_date}): ") or event.end_date
            event.start_time = input(f"Start Time ({event.start_time}): ") or event.start_time
            event.end_time = input(f"End Time ({event.end_time}): ") or event.end_time
            event.category = input(f"Category ({event.category}): ") or event.category
            event.priority = input(f"Priority ({event.priority}): ") or event.priority
            event.recurrence = input(f"Recurrence ({event.recurrence}): ") or event.recurrence

            # Check for conflicts after editing
            if self.check_conflicts(event):
                print("Event conflicts with an existing event!")
            else:
                print("Event updated successfully.")
        else:
            print("Invalid event number.")  # Handle invalid input

    # Delete an event from the scheduler
    def delete_event(self):
        self.view_events()  # Show all events
        index = int(input("Enter the event number to delete: ")) - 1  # Get the event index from the user
        if 0 <= index < len(self.events):  # Validate index
            self.events.pop(index)  # Remove the event from the list
            print("Event deleted successfully.")
        else:
            print("Invalid event number.")  # Handle invalid input

    # Search for events based on a keyword
    def search_events(self):
        keyword = input("Enter a keyword to search for events: ").lower()  # Get keyword from user
        # Filter events by title or description containing the keyword
        results = [event for event in self.events if keyword in event.title.lower() or keyword in event.description.lower()]
        if results:
            for event in results:  # Display matching events
                print(f"\n{event}")
        else:
            print("No matching events found.")  # Inform user if no matches

    # Check for conflicts between events
    def check_conflicts(self, new_event):
        for event in self.events:
            # Check if the new event overlaps with an existing event
            if (new_event.start_date == event.start_date and
                not (new_event.end_time <= event.start_time or new_event.start_time >= event.end_time)):
                return True  # Conflict detected
        return False  # No conflicts

    # Notify user of upcoming events within the next hour
    def notify_upcoming(self):
        now = datetime.datetime.now()  # Get the current time
        for event in self.events:
            # Parse event start date and time
            event_start = datetime.datetime.strptime(f"{event.start_date} {event.start_time}", "%d/%m/%Y %H:%M")
            # Notify if the event is starting within the next hour
            if 0 <= (event_start - now).total_seconds() <= 3600:
                print(f"Upcoming Event: {event.title} at {event.start_time} on {event.start_date}")

    # Main loop to run the application
    def run(self):
        while True:
            # Display menu options
            print("\nEvent Scheduler")
            print("1. Add Event")
            print("2. View Events")
            print("3. Edit Event")
            print("4. Delete Event")
            print("5. Search Events")
            print("6. Notifications")
            print("7. Exit")
            choice = input("Enter your choice: ")
            
            # Execute the corresponding functionality based on user input
            if choice == "1":
                self.add_event()
            elif choice == "2":
                self.view_events()
            elif choice == "3":
                self.edit_event()
            elif choice == "4":
                self.delete_event()
            elif choice == "5":
                self.search_events()
            elif choice == "6":
                self.notify_upcoming()
            elif choice == "7":
                print("Goodbye!")
                break  # Exit the loop
            else:
                print("Invalid choice. Please try again.")  # Handle invalid input

# Entry point for the application
if __name__ == "__main__":
    scheduler = EventScheduler()  # Create an EventScheduler object
    scheduler.run()  # Start the application
