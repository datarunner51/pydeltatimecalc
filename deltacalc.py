from datetime import datetime, date
starttime = "0715"
endtime = "1630"

stime = datetime.strptime(starttime, "%H%M")
qtime = datetime.strptime(endtime, "%H%M")
delta = qtime - stime

hours = (delta.seconds//3600)
minute = (delta.seconds//60)%60

print("{} Hours and {} minute(s)".format(hours, minute))

entry = hours + (minute/60)

print("Timesheet entry: {}".format(entry))
