import datetime

now = datetime.datetime.now()
year = '%02d'%now.year
month ='%02d'%now.month
day = '%02d'%now.day
print(f'{year}-{month}-{day}')