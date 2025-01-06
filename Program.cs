using System;
using System.Collections.Generic;

class Event
{
    public string EventName { get; set; } //name of the event
    public DateTime OccurrenceDate { get; set; } //of type DateTime which is a struct in C# that works with dates

    public Event(string eventName, DateTime occurrenceDate) //Constructor
    {
        EventName = eventName;
        OccurrenceDate = occurrenceDate;
    }

    public override string ToString() //Returns string representation of our variables
    {
        return $"{EventName} - {OccurrenceDate.ToShortDateString()}";
    }
}

class Program
{
    static List<Event> ScheduledEvents = new List<Event>(); //Creates a new list that will store Event objects

    static void Main(string[] args)
    {
        while (true) //infinite loop that will work until user decides to exit
        {
            Console.WriteLine("\nEvent Scheduler");
            Console.WriteLine("1. Schedule New Event");
            Console.WriteLine("2. Display Upcoming Events");
            Console.WriteLine("3. Exit");
            Console.Write("Choose an option: ");

            string userChoice = Console.ReadLine();
            if (userChoice == "1")
            {
                ScheduleEvent(); //method invocation
            }
            else if (userChoice == "2")
            {
                ShowEvents();
            }
            else if (userChoice == "3")
            {
                return; //return statement means program exits in main method
            }
            else
            {
                Console.WriteLine("Invalid choice, please try again.");
            }
        }
    }

    static void ScheduleEvent()
    {
        Console.Write("Enter event name (type 'cancel' to go back): ");
        string eventName = Console.ReadLine();
        
        if (eventName.ToLower() == "cancel")
        {
            return;
        }

        DateTime eventDate;
        string dateEntry;
        do
        {
            Console.Write("Enter event date (MM/dd/yyyy, or 'cancel' to go back): ");
            dateEntry = Console.ReadLine();
            if (dateEntry.ToLower() == "cancel")
            {
                return;
            }
            if (!DateTime.TryParse(dateEntry, out eventDate)) //attempts to convert string into DateTime object
            {
                Console.WriteLine("Invalid date format. Please try again.");
            }
        } while (!DateTime.TryParse(dateEntry, out eventDate)); //until parsing fails

        ScheduledEvents.Add(new Event(eventName, eventDate)); //adds a new event into the list
        Console.WriteLine("Event scheduled successfully!");
    }

    static void ShowEvents()
    {
        if (ScheduledEvents.Count == 0)
        {
            Console.WriteLine("No events scheduled.");
            return;
        }

        Console.WriteLine("\nUpcoming Events:");

        List<Event> sortedEvents = new List<Event>(ScheduledEvents); //creates a copy of the original list that will sort events in ascending order from earliest to latest

        sortedEvents.Sort((e1, e2) => e1.OccurrenceDate.CompareTo(e2.OccurrenceDate)); //Two Event objects being compared

        foreach (var evt in sortedEvents) //Now we iterates over each event in sorted list
        {
            if (evt.OccurrenceDate >= DateTime.Now) //This ignores the event that are from past and before current time
            {
                Console.WriteLine(evt);
            }
        }
    }
}
