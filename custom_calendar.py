def day_from_number(day_number):
    days = [None, "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    if day_number > 7 or day_number < 0:
        return None
    return days[day_number]

def day_to_number(day):
    days = {
    "Monday": 1,
    "Tuesday": 2,
    "Wednesday": 3,
    "Thursday": 4,
    "Friday": 5,
    "Saturday": 6,
    "Sunday": 7
    }
    if day in days:
        return days[day]
    return None