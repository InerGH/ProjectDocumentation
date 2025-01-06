const readline = require('readline');

// Create interface for reading user input from console
const userInput = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

// Event class
class CalendarEvent {
  constructor(eventTitle, eventDate) {
    this.eventTitle = eventTitle;
    this.eventDate = new Date(eventDate);
  }

  toString() {
    return `${this.eventTitle} - ${this.eventDate.toLocaleDateString()}`;
  }
}

// Global array to store events
let upcomingCalendar = [];

// Main function to run the application
function runApp() {
  function displayMenu() {
    console.log("\nEvent Scheduler");
    console.log("1. Add New Calendar Event");
    console.log("2. View Upcoming Calendar Events");
    console.log("3. Exit");
    userInput.question("Choose an option: ", (selection) => {
      switch (selection) {
        case '1':
          addEvent();
          break;
        case '2':
          listEvents();
          break;
        case '3':
          userInput.close();
          return;
        default:
          console.log("Invalid selection, please try again.");
          displayMenu();
      }
    });
  }

  displayMenu();
}

// Function to add a new event
function addEvent() {
  userInput.question("Enter event title (type 'cancel' to go back): ", (eventTitle) => {
    if (eventTitle.toLowerCase() === 'cancel') {
      runApp();
    } else {
      userInput.question("Enter event date (YYYY-MM-DD, or 'cancel' to go back): ", (dateEntry) => {
        if (dateEntry.toLowerCase() === 'cancel') {
          runApp();
        } else {
          const eventDate = new Date(dateEntry);
          if (isNaN(eventDate.getTime())) {
            console.log("Invalid date format. Please try again.");
            addEvent();
          } else {
            upcomingCalendar.push(new CalendarEvent(eventTitle, eventDate));
            console.log("Event added successfully to calendar!");
            runApp();
          }
        }
      });
    }
  });
}

// Function to list upcoming events
function listEvents() {
  if (upcomingCalendar.length === 0) {
    console.log("No events in the calendar.");
    runApp();
    return;
  }

  console.log("\nUpcoming Calendar Events:");
  
  // Sort events by date
  const sortedCalendar = upcomingCalendar.sort((a, b) => a.eventDate - b.eventDate);
  
  const now = new Date();
  sortedCalendar.forEach(event => {
    if (event.eventDate >= now) {
      console.log(event.toString());
    }
  });
  runApp();
}

// Start the application
runApp();