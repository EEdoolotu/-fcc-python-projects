def add_time(start, duration, day=None):
    start_time, period = start.split()
    start_hour, start_minute = map(int, start_time.split(':'))


    if period == 'PM' and start_hour != 12:
        start_hour += 12

    elif period == 'AM' and start_hour == 12:
        start_hour = 0
         
         # Split the duration into hours and minutes
    duration_hour, duration_minute = map(int, duration.split(':'))

        # Add minutes and handle overflow into hours
    total_minutes = start_minute + duration_minute
    extra_hour = total_minutes // 60
    final_minutes = total_minutes % 60

    total_hours = start_hour + duration_hour + extra_hour
    days_later = total_hours // 24
    final_hour_24 = total_hours % 24

    if final_hour_24 == 0:
        final_hour = 12
        final_period = "AM"
    elif 1 <= final_hour_24 < 12:
        final_hour = final_hour_24
        final_period = "AM"
    elif final_hour_24 == 12:
        final_hour = 12
        final_period = "PM"
    else:
        final_hour = final_hour_24 - 12
        final_period = "PM"

    final_time = f"{final_hour}:{final_minutes:02d} {final_period}"

    # Step 5: Handle the optional day of the week
    if day:
        days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        day_index = days_of_week.index(day.capitalize())
        new_day = days_of_week[(day_index + days_later) % 7]
        final_time += f", {new_day}"

    # Step 6: Add info about days later
    if days_later == 1:
        final_time += " (next day)"
    elif days_later > 1:
        final_time += f" ({days_later} days later)"

    return final_time










    return new_time