def solution(day_week: str, date: str, other_date: str) -> str:

    DAYS = "sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday" 
    index = DAYS.index(day_week.lower())

    day1, month1 = date.split("/")
    day2, month2 = other_date.split("/")    
    
    dif_months = int(month2) - int(month1) 
    if dif_months > 0: # second date in a month later than first date
        dif_days = (30 - int(day1) + int(day2)) % 7

    elif dif_months < 0: # second date in a month earlier than first date
        dif_days = (int(day1) + 30 - int(day2)) % 7

    else: # dates in the same month
        dif_days = (int(day2) - int(day1)) % 7

    new_day_week = ""
    if dif_days + index >= len(DAYS): # cicle through days of the week
        new_day_week = DAYS[dif_days + index - len(DAYS)]

    else:
        new_day_week = DAYS[dif_days + index]   

    return new_day_week.title()

print(solution("Tuesday", "13/04", "10/04"))