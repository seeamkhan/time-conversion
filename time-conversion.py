date_input = raw_input("Please input date in AM/PM format. Example, 09:34:12PM: ")
date_input = '12:34:12PM'
date_const_part = date_input[2:8]
new_h_24 = date_input[0:2]
if 'A' in date_input[8]:
    print "AM found"
    if '12' in date_input[0:2]:
        print "12 found"
        h_24 = int(date_input[0:2])
        h_24 = h_24 - 12
        new_h_24 = '0'+str (h_24)
        # print new_h_24
if 'P' in date_input[8]:
    print "PM found"
    if '12' not in date_input[0:2]:
        h_24 = int(date_input[0:2])
        h_24 = h_24 + 12
        new_h_24 = str(h_24)

print new_h_24+date_const_part