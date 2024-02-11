## Current Date and Time

- We can manage current date and time by using datetime module


- To print current time in nice format we can use strftime method from datetime object

```python
from datetime import datetime, date
time_now = datetime.now().strftime('%H:%M:%S')
print(time_now)
 
# output like this format 02:05:05

# to get the tiday's date

today_date = date.today()
print(today_date)

# output like this format 2024-02-12

```
