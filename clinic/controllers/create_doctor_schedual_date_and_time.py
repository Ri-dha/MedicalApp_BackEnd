import datetime
from datetime import time
# x = datetime.datetime.now()

# date_string = "2022/9/20"

sunday = ['20:00', '21:15', '22:00', '24:30']
monday = ['20:00', '21:15', '22:00', '24:30']
tuesday = ['10:00', '11:00', '13:10', '14:30']
wednesday = ['10:00', '11:00', '13:10', '14:30']
thursday = ['10:00', '11:00', '13:10', '14:30']
friday = ['10:00', '11:00', '13:10', '14:30']
saturday = ['10:00', '11:00', '13:10', '14:30']


# ordinaryTime = datetime.datetime.strptime(ordinaryTime, '%H:%M')
# print(f"{ordinaryTime.hour}:{ordinaryTime.minute}")


def create_doctor_schedual_date_and_time(sunday: list[time], monday: list[time], tuesday: list[time], wednesday: list[time], thursday: list[time], friday: list[time], saturday: list[time], howManyDays: int):
    today = str(datetime.date.today())
    data = {
        'Sunday': [],
        'Monday': [],
        'Tuesday': [],
        'Wednesday': [],
        'Thursday': [],
        'Friday': [],
        'Saturday': [],
    }
    weekdaystimes = [sunday, monday, tuesday,
                     wednesday, thursday, friday, saturday]
    for day in range(howManyDays):

        date_1 = datetime.datetime.strptime(
            today, "%Y-%m-%d") + datetime.timedelta(days=day)
        # print(date_1.strftime('%A'))
        dayName = date_1.strftime('%A')
        if dayName == 'Sunday' and sunday:
            data[dayName] += [date_1.strftime('%Y-%m-%d')]

        if dayName == 'Monday' and monday:
            data[dayName] += [date_1.strftime('%Y-%m-%d')]

        if dayName == 'Tuesday' and tuesday:
            data[dayName] += [date_1.strftime('%Y-%m-%d')]

        if dayName == 'Wednesday'and wednesday:
            data[dayName] += [date_1.strftime('%Y-%m-%d')]

        if dayName == 'Thursday'and thursday:
            data[dayName] += [date_1.strftime('%Y-%m-%d')]

        if dayName == 'Friday' and friday:
            data[dayName] += [date_1.strftime('%Y-%m-%d')]

        if dayName == 'Saturday' and saturday:
            data[dayName] += [date_1.strftime('%Y-%m-%d')]

    final = []
    for daytime in range(len(data.items())):
        dayName = list(data.items())[daytime][0]
        calendarTime = []
        for date1 in list(data.items())[daytime][1]:
            # print(f"{dayName} {date1} {weekdaystimes[daytime]}")

            calendarTime.append({date1: weekdaystimes[daytime]})
        final.append({dayName: calendarTime})

    return final


# create_doctor_schedual_date_and_time(sunday=sunday, monday=monday, tuesday=tuesday,
#                                      wednesday=wednesday, thursday=thursday, friday=friday, saturday=saturday, howManyDays=30)
