from calendar import monthcalendar

def last_saturday_and_total(input_date):

    month = int(input_date[:2])
    year = int(input_date[2:])
    
    months = monthcalendar(year, month)
    
    if months[-1][5]:
        last_saturday_date = months[-1][-2]
    else:
        last_saturday_date = months[-2][-2]

    total_saturdays = sum(1 for week in months if week[5] != 0)
    
    return last_saturday_date, total_saturdays

input_date = '062023'

last_saturday, total_saturdays = last_saturday_and_total(input_date)
print(f"Last Saturday: {last_saturday}")
print(f"Total Saturdays: {total_saturdays}")
