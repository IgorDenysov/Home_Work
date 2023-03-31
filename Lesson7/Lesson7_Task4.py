# Task 4
#
# Створити лист із днями тижня.
# В один рядок (ну або як завжди) створити словник виду: {1: “Monday”, 2:...
# Також в один рядок або як вдасться створити зворотний словник {“Monday”: 1,


days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

week = [(i + 1, days[i]) for i in range(0, len(days))]

week_dict = { i[0] : i[1] for i in week}
opposite_week = {i[1]: i[0] for i in week}

print(week_dict)
print(opposite_week)
