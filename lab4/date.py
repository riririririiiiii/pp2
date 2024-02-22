#ex1
from datetime import datetime, timedelta

current_date = datetime.now()
five_days_ago = current_date - timedelta(days=5)

print(five_days_ago)

#ex2
from datetime import datetime, timedelta

today = datetime.now()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)

print("Yesterday:", yesterday)
print("Today:", today)
print("Tomorrow:", tomorrow)

#ex3
from datetime import datetime

current_datetime = datetime.now()
current_datetime_without_microseconds = current_datetime.replace(microsecond=0)

print("Current DateTime with Microseconds:", current_datetime)
print("Current DateTime without Microseconds:", current_datetime_without_microseconds)

#ex4
from datetime import datetime

date1 = datetime(2023, 1, 1, 12, 0, 0)  # Example 1
date2 = datetime(2023, 1, 2, 12, 0, 0)  # Example 2

difference_seconds = (date2 - date1).total_seconds()

print("Difference in Seconds:", difference_seconds)

