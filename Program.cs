using System;
using System.Collections.Generic;

class Event
{
    public string EventName { get; set; }
    public DateTime OccurrenceDate { get; set; }

    public Event(string eventName, DateTime occurrenceDate)
    {
        EventName = eventName;
        OccurrenceDate = occurrenceDate;
    }

    public override string ToString()
    {
        return $"{EventName} - {OccurrenceDate.ToShortDateString()}";
    }
}

class Program
{
    static List<Event> ScheduledEvents = new List<Event>();

    static void Main(string[] args)
    {
        while (true)
        {
            Console.WriteLine("\nEvent Scheduler");
            Console.WriteLine("1. Schedule New Event");
            Console.WriteLine("2. Display Upcoming Events");
            Console.WriteLine("3. Exit");
            Console.Write("Choose an option: ");

            string userChoice = Console.ReadLine();
            if (userChoice == "1")
            {
                ScheduleEvent();
            }
            else if (userChoice == "2")
            {
                ShowEvents();
            }
            else if (userChoice == "3")
            {
                return;
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
            if (!DateTime.TryParse(dateEntry, out eventDate))
            {
                Console.WriteLine("Invalid date format. Please try again.");
            }
        } while (!DateTime.TryParse(dateEntry, out eventDate));

        ScheduledEvents.Add(new Event(eventName, eventDate));
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
        List<Event> sortedEvents = new List<Event>(ScheduledEvents);
        sortedEvents.Sort((e1, e2) => e1.OccurrenceDate.CompareTo(e2.OccurrenceDate));

        foreach (var evt in sortedEvents)
        {
            if (evt.OccurrenceDate >= DateTime.Now)
            {
                Console.WriteLine(evt);
            }
        }
    }
}
