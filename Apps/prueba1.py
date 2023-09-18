import datetime

date = input("Enter the date (format: dd mm yyyy): ")
day_name = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

day = datetime.datetime.strptime(date, '%d %m %Y').weekday()
print(day_name[day])