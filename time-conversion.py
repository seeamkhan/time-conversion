def time_formatter():
    # time_input = raw_input("Please input time in AM/PM format. Example, 09:34:12PM: ")
    time_input = '05:00:13pM'
    time_input = time_input.upper()
    time_trimmed = time_input.replace(" ", "")

    time_const_part = time_trimmed[2:8]
    new_h_24 = time_trimmed[0:2]

    input_validation = False
    print time_trimmed
    try:
        if (len(time_trimmed) == 10):
            print "The date have valid number of characters."

            if (0 < int(time_trimmed[0:2]) < 13 and int(time_trimmed[3:5]) < 60 and int(time_trimmed[6:8]) < 60):
                print "This is a valid date format."
                # else:
                #     print 'The hour, minute or seconds have other values than integer.'
                input_validation = True
            else:
                print 'The hour should be in between 1 to 12, minute and second should be 0 to 59.'
        else:
            print 'The date have more or less values then expected.'

    except:
        print 'The hour, minute or seconds have other values than integer.'


    print "Input Date validation: %r" % input_validation

    if (input_validation is True):
        if ('AM' == time_trimmed[8:]):
            print "AM found"
            if ('12' in time_trimmed[0:2]):
                h_24 = int(time_trimmed[0:2])
                h_24 = h_24 - 12
                new_h_24 = '0'+str (h_24)

        elif ('PM' == time_trimmed[8:]):
            print "PM found"
            if ('12' not in time_trimmed[0:2]):
                h_24 = int(time_trimmed[0:2])
                h_24 = h_24 + 12
                new_h_24 = str(h_24)

        final_time = new_h_24+time_const_part
        print 'Formatted 24 hour time is: %s' %final_time

    else:
        print "Invalid date format. Please input a valid date."
time_formatter()
