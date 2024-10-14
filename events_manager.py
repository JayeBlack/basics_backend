from ics import Calendar, Event
from datetime import datetime, timedelta
import uuid  # Import uuid to generate unique identifiers

# Create a new calendar
calendar = Calendar()

# Define the details of the recurring event
event_title = "MOBILE FLUTTER DEVELOPMENT"
start_time = "15:00"
end_time = "17:00"
days_of_week = ["Tuesday", "Monday", "Thursday"]
first_event_date = datetime(2024, 10, 8)
recurrence_end_date = datetime(2024, 12, 31)

# Generate the events
current_date = first_event_date
while current_date <= recurrence_end_date:
    if current_date.strftime('%A') in days_of_week:
        event = Event()
        event.name = event_title
        event.begin = current_date.strftime(f"%Y-%m-%d {start_time}")
        event.end = current_date.strftime(f"%Y-%m-%d {end_time}")
        event.description = "Weekly Flutter Development Sessions"
        event.uid = str(uuid.uuid4())  # Generate a unique identifier
        event.make_all_day()  # Set the event as all day if needed (optional)
        calendar.events.add(event)
    current_date += timedelta(days=1)

# Save the calendar to a .ics file without extra blank lines
with open("flutter_dev_schedule.ics", "w") as f:
    f.write(calendar.serialize().strip())  # Use strip() to remove extra blank lines
