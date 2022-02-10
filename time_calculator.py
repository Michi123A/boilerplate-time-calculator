def find_day(starting_day, another_day):
    days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday",
            "Friday", "Saturday", "Sunday", "Monday", "Tuesday",
            "Wednesday", "Thursday", "Friday", "Saturday"]

    day1 = days.index(f"{starting_day}")
    new = another_day + day1
    if new > 7:
      new = new % 7
    new_day = days[new]

    return new_day

def add_time(start, duration, day = "0"):
    # separate hours and minutes
    starting_day = ""
    if day != "0":
        starting_day += day.lower().capitalize()


    start = start.split()
    time = start[1]
    hour_min = start[0]
    x = hour_min.split(":")
    hour = x[0]
    minute = x[1]
    h = hour.find("0")
    if h == 0:
        hour = hour[1]
    m = minute.find("0")
    if m == 0:
        minute = minute[1]

    duration = duration.split(":")
    add_hour = duration[0]
    add_minute = duration[1]
    if add_hour == "0":
        add_hour = 0
    else:
       a_h = add_hour.find("0")
       if a_h == 0:
        add_hour = add_hour[1]
    if add_minute == "0":
        add_minute = 0
    else:
        a_m = add_minute.find("0")
        if a_m == 0:
            add_minute = add_minute[1]
    minute = int(minute)
    hour = int(hour)
    add_minute = int(add_minute)
    add_hour = int(add_hour)
    change_time = False

    while minute < 59 and add_minute > 0:
        if add_minute == 0:
            break
        #print(minute)
        minute += 1
        add_minute -= 1
        #print("minute",minute)
        #print("add",add_minute)

    new_minute = minute
    if add_minute > 0 and minute == 59:
        add_hour += 1
        add_minute -= 1
        new_minute = add_minute

    if new_minute < 10:
        new_minute = f"0{new_minute}"

    add_days = 0
    another_day = 0
    add_days += add_hour // 24
    if add_days > 0:
        another_day += add_days
        add_hour = add_hour - (add_days * 24)
    new_hour = hour + add_hour

    if new_hour == 12:
        change_time = True
    elif new_hour > 12:
        new_hour -= 12
        change_time = True

    if change_time is True:
        if time == "AM":
            time = "PM"
        else:
            time = "AM"
            another_day += 1

    if another_day == 1:
        days_later = "(next day)"
    elif another_day > 1:
        days_later = f"({another_day} days later)"

    new_time = f"{new_hour}:{new_minute} {time}"
    if day != "0":
        new_day = find_day(starting_day, another_day)
        if another_day >= 1:
            new_day = f", {new_day} {days_later}"
        else:
            new_day = f", {new_day}"
        new_time += new_day
    else:
        if another_day > 0:
            new_time += f" {days_later}"
    return new_time
