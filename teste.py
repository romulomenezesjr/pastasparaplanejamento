from datetime import datetime
from datetime import timedelta



for i in range(20):
    print((datetime(2020,2,7)+timedelta(days=i*7)).strftime("%Y-%m-%d"))
    