import datetime
now = datetime.datetime.now()

thingy = raw_input("when where you born?")

year2 = int(thingy.split('/')[2])
month2 = int(thingy.split('/')[1])
day2 = int(thingy.split('/')[0])

year = now.year
month = now.month
day = now.day

year3 = year - year2
month3 = month - month2
day3 = day - day2


print ((year3 * 31536000) + (month3 * 2678400)+(day3 + 86400))
