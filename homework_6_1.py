import datetime
from datetime import date
a = date.today()
print(a)
a1 = a - datetime.timedelta(days=5)
print(a1)