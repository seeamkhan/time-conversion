class Time_Formatter():
    time_input = raw_input("Please input time in AM/PM format. Example, 09:34:12PM: ")
    # self.time_input = " 12 : 11:11 aM"
    time_input = time_input.upper()
    time_trimmed = time_input.replace(" ", "")
    input_validation = False
    am_pm = ''
    error_message = 'Unknown Error'

    def input_validator(self):

        print "Input time is: %s" %self.time_trimmed

        try:
            if (0 < int(self.time_trimmed[0:2]) < 13 and 0 <= int(self.time_trimmed[3:5]) < 60 and 0 <= int(self.time_trimmed[6:8]) < 60):
                # print "The time have valid Hour, Minute and Second values."
                if (len(self.time_trimmed) == 10):
                    # print "The time have valid number of characters."
                    if ("AM" in self.time_trimmed[8:]):
                        self.am_pm = 'am'
                        self.input_validation = True
                    elif ("PM" in self.time_trimmed[8:]):
                        self.am_pm = 'pm'
                        self.input_validation = True
                    else:
                        self.error_message = 'Invalid AM/PM value.'
                        # print 'Invalid AM/PM value.'
                    # print "AM/PM value is: %s" % self.am_pm
                else:
                    self.error_message = 'The time have more or less values then expected.'
                    # print 'The time have more or less values then expected.'
            else:
                self.error_message = 'The hour should be in between 1 to 12, minute and second should be 0 to 59.'
                # print 'The hour should be in between 1 to 12, minute and second should be 0 to 59.'
        except:
            self.error_message = 'The hour, minute or seconds have other values than integer.'
            # print 'The hour, minute or seconds have other values than integer.'

        # print "Input time validation: %r" % self.input_validation
        self.validation_output = [self.input_validation, self.am_pm, self.error_message]
        return self.validation_output

    def formatter(self, validation_output):
        input_validation = validation_output[0]
        am_pm = validation_output[1]
        error_message = validation_output[2]
        time_const_part = self.time_trimmed[2:8]
        new_h_24 = self.time_trimmed[0:2]

        if (input_validation is True):
            if ('am' == am_pm):
                # print "AM found"
                if ('12' in self.time_trimmed[0:2]):
                    h_24 = int(self.time_trimmed[0:2])
                    h_24 = h_24 - 12
                    new_h_24 = '0' + str(h_24)

            elif ('pm' == am_pm):
                # print "PM found"
                if ('12' not in self.time_trimmed[0:2]):
                    h_24 = int(self.time_trimmed[0:2])
                    h_24 = h_24 + 12
                    new_h_24 = str(h_24)

            final_time = new_h_24 + time_const_part
            print 'Formatted 24 hour time is: %s' % final_time

        else:
            print "Invalid time format. Please input a valid time."
            print "Error: %s" % error_message

for x in xrange(1):
    validation = Time_Formatter().input_validator()
    convert = Time_Formatter().formatter(validation)
