import csv
import dateTime

classCodeNames = []
classNames = []
days = []
startTimes = []
durations = []
teachingWeeks = []
locations = []
staffs = []

with open('test.csv', encoding='utf-8-sig') as csvFile:
    csvReader = csv.reader(csvFile, delimiter=',')
    for row in csvReader:
        if len(row) > 2:
            classCodeNames.append(row[0])
            classNames.append(row[1])
            days.append(row[3])
            startTimes.append(row[4])
            durations.append(row[5])
            teachingWeeks.append(row[6])
            locations.append(row[7])
            staffs.append(row[8])
