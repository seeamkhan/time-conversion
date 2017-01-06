# time_input = raw_input("Please input time in AM/PM format. Example, 09:34:12PM: ")
time_input = '12:34:12AM'

time_const_part = time_input[2:8]
new_h_24 = time_input[0:2]

if ('A' == time_input[8] or 'a' == time_input[8]):
    print "AM found"
    if '12' in time_input[0:2]:
        h_24 = int(time_input[0:2])
        h_24 = h_24 - 12
        new_h_24 = '0'+str (h_24)

if ('P' == time_input[8] or 'p' == time_input[8]):
    print "PM found"
    if '12' not in time_input[0:2]:
        h_24 = int(time_input[0:2])
        h_24 = h_24 + 12
        new_h_24 = str(h_24)

print new_h_24+time_const_part