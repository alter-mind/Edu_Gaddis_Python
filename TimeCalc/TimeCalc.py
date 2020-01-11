DAY = 86400
HOUR = 3600
MIN = 60
sec = int(input('Enter second: '))
day = sec // DAY
sec = sec % DAY
hour = sec // HOUR
sec = sec % HOUR
min = sec // MIN
sec = sec % MIN
print('Time is:',
      '\nDays', day,
      '\nHours:', hour,
      '\nMinutes:', min,
      '\nSeconds:',sec)

