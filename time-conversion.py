def time_formatter():
    # time_input = raw_input("Please input time in AM/PM format. Example, 09:34:12PM: ")
    time_input = " 12 : 11:11 aM"
    time_input = time_input.upper()
    time_trimmed = time_input.replace(" ", "")
    time_const_part = time_trimmed[2:8]
    new_h_24 = time_trimmed[0:2]
    input_validation = False
    am_pm = ''
    print time_trimmed

    try:
        if (len(time_trimmed) == 10):
            print "The date have valid number of characters."
            if (0 < int(time_trimmed[0:2]) < 13 and 0 <= int(time_trimmed[3:5]) < 60 and 0 <= int(time_trimmed[6:8]) < 60):
                print "The Date have valid Hour, Minute and Second values."
                if ("AM" in time_trimmed[8:]):
                    am_pm = 'am'
                    input_validation = True
                elif ("PM" in time_trimmed[8:]):
                    am_pm = 'pm'
                    input_validation = True
                else:
                    print 'Invalid AM/PM value.'
                print "AM/PM value is: %s" % am_pm
            else:
                print 'The hour should be in between 1 to 12, minute and second should be 0 to 59.'
        else:
            print 'The date have more or less values then expected.'
    except:
        print 'The hour, minute or seconds have other values than integer.'

    print "Input Date validation: %r" % input_validation

    if (input_validation is True):
        if ('am' == am_pm):
            print "AM found"
            if ('12' in time_trimmed[0:2]):
                h_24 = int(time_trimmed[0:2])
                h_24 = h_24 - 12
                new_h_24 = '0' + str(h_24)

        elif ('pm' == am_pm):
            print "PM found"
            if ('12' not in time_trimmed[0:2]):
                h_24 = int(time_trimmed[0:2])
                h_24 = h_24 + 12
                new_h_24 = str(h_24)

        final_time = new_h_24 + time_const_part
        print 'Formatted 24 hour time is: %s' % final_time

    else:
        print "Invalid date format. Please input a valid date."


time_formatter()
