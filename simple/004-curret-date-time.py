# We can manage current date and time by using datetime module

from datetime import datetime, date

# To print current time in nice format we can use strftime method from datetime object

time_now = datetime.now().strftime('%H:%M:%S')
print(time_now)

# to get the tiday's date

today_date = date.today()
print(today_date)
