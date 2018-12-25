import csv
import datetime

class_code_names = []
class_names = []
days = []
start_times = []
durations = []
teaching_weeks = []
locations = []
staffs = []

unavailable_times = []

with open('test.csv', encoding='utf-8-sig') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        if len(row) > 2:
            class_code_names.append(row[0])
            class_names.append(row[1])
            days.append(row[3])
            start_times.append(row[4])
            durations.append(row[5])
            teaching_weeks.append(row[6])
            locations.append(row[7])
            staffs.append(row[8])


def day_to_iso_day(day):
    if day == "Monday":
        return 1
    elif day == "Tuesday":
        return 2
    elif day == "Wednesday":
        return 3
    elif day == "Thursday":
        return 4
    elif day == "Friday":
        return 5
    elif day == "Saturday":
        return 6
    elif day == "Sunday":
        return 7


def get_start_end_dates(day, start_time, teaching_week):

    periods = teaching_week.split(',')
    periods_formatted = []
    periods_calculated = []
    start_time = datetime.datetime.strptime(start_time, "%I:%M%p")

    for word in periods:
        period_formatted = word.replace(" ", "").split('to')
        for i in range(len(period_formatted)):
            period_formatted[i] = datetime.datetime.strptime(period_formatted[i], "%d/%m/%y")
            period_formatted[i] += datetime.timedelta(hours=start_time.hour, minutes=start_time.minute)
        periods_formatted.append(period_formatted)

    add_initial_days = 0
    day = day_to_iso_day(day)  # Monday - 1, Sunday - 7
    for period in periods_formatted:
        if len(period) == 2:
            if (datetime.datetime.isoweekday(period[0])) != day:
                add_initial_days = 7 - day
                period[0] += datetime.timedelta(days=add_initial_days)
            periods_calculated.append(period[0].isoformat())

            while period[0] <= period[1]:
                periods_calculated.append(period[0].isoformat())
                period[0] += datetime.timedelta(days=7)
        else:
            periods_calculated.append(period[0].isoformat())

    return periods_calculated


for i in range(1, len(class_code_names)):
    print(get_start_end_dates(days[i], start_times[i], teaching_weeks[i]))



