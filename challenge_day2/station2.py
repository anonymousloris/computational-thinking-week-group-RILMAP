from datetime import datetime

def solution_station_2(date_str: str) -> str:
    # Convert the date string to a datetime object
    date = datetime.strptime(date_str, '%Y-%m-%d')
    # Return the day of the week as a string (e.g., "Monday", "Tuesday")
    return date.strftime('%A')
