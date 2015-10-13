leapmonth = lambda y, m: m==2 and (y%4 == 0) and (y!=1900)
daysinmonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

month, year = 1, 1900
wday = 1 # 0=Sunday, 1=Monday, ...
sundays = 0

while year < 2001:
    if year >= 1901 and wday == 0: sundays += 1
    add = 29 if leapmonth(year, month) else daysinmonth[month-1]
    wday = (wday + add) % 7
    year, month = year+month//12, month%12+1

print(sundays)
