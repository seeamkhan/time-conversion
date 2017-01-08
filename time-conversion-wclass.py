import time

class Time_Formatter():

    def input_validator(self):
        # time_input = " 12 : 11:11 aM"
        time_input = raw_input("Please input time in AM/PM format. Example, 09:34:12PM: ")
        time_input = time_input.upper()
        time_trimmed = time_input.replace(" ", "")
        am_pm = ''
        input_validation = False
        error_message = 'Unknown Error'
        print "Input time is: %s" %time_trimmed

        try:
            if (0 < int(time_trimmed[0:2]) < 13 and 0 <= int(time_trimmed[3:5]) < 60 and 0 <= int(time_trimmed[6:8]) < 60):
                # print "The time have valid Hour, Minute and Second values."
                if (len(time_trimmed) == 10):
                    # print "The time have valid number of characters."
                    if ("AM" in time_trimmed[8:]):
                        am_pm = 'am'
                        input_validation = True
                    elif ("PM" in time_trimmed[8:]):
                        am_pm = 'pm'
                        input_validation = True
                    else:
                        error_message = 'Invalid AM/PM value.'
                        # print 'Invalid AM/PM value.'
                    # print "AM/PM value is: %s" % am_pm
                else:
                    error_message = 'The time have more or less values then expected.'
                    # print 'The time have more or less values then expected.'
            else:
                error_message = 'The hour should be in between 1 to 12, minute and second should be 0 to 59.'
                # print 'The hour should be in between 1 to 12, minute and second should be 0 to 59.'
        except:
            error_message = 'The hour, minute or seconds have other values than integer.'
            # print 'The hour, minute or seconds have other values than integer.'

        # print "Input time validation: %r" % input_validation
        validation_output = [time_trimmed, input_validation, am_pm, error_message]
        return validation_output

    def formatter(self, validation_output):
        time_trimmed = validation_output[0]
        input_validation = validation_output[1]
        am_pm = validation_output[2]
        error_message = validation_output[3]
        time_const_part = time_trimmed[2:8]
        new_h_24 = time_trimmed[0:2]

        if input_validation is True:
            if ('am' == am_pm):
                # print "AM found"
                if ('12' in time_trimmed[0:2]):
                    h_24 = int(time_trimmed[0:2])
                    h_24 = h_24 - 12
                    new_h_24 = '0' + str(h_24)

            elif ('pm' == am_pm):
                # print "PM found"
                if ('12' not in time_trimmed[0:2]):
                    h_24 = int(time_trimmed[0:2])
                    h_24 = h_24 + 12
                    new_h_24 = str(h_24)

            final_time = new_h_24 + time_const_part
            print 'Formatted 24 hour time is: %s' % final_time

        else:
            print "Invalid time format. Please input a valid time."
            print "Error: %s" % error_message

for x in xrange(4):
    validation = Time_Formatter().input_validator()
    convert = Time_Formatter().formatter(validation)
    time.sleep(3)
    print 'Thank you!'
    time.sleep(1)