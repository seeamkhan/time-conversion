class Time_Formatter():



    # def __init__(self):
    #     pass

    def input_validator(self):
        # time_input = raw_input("Please input time in AM/PM format. Example, 09:34:12PM: ")
        self.time_input = " 12 : 11:11 aM"
        self.time_input = self.time_input.upper()
        self.time_trimmed = self.time_input.replace(" ", "")
        self.time_const_part = self.time_trimmed[2:8]
        self.new_h_24 = self.time_trimmed[0:2]
        self.input_validation = False
        self.am_pm = ''
        print "Input time is: %s" %self.time_trimmed

        try:
            if (len(self.time_trimmed) == 10):
                # print "The time have valid number of characters."
                if (0 < int(self.time_trimmed[0:2]) < 13 and 0 <= int(self.time_trimmed[3:5]) < 60 and 0 <= int(self.time_trimmed[6:8]) < 60):
                    # print "The time have valid Hour, Minute and Second values."
                    if ("AM" in self.time_trimmed[8:]):
                        self.am_pm = 'am'
                        self.input_validation = True
                    elif ("PM" in self.time_trimmed[8:]):
                        self.am_pm = 'pm'
                        self.input_validation = True
                    else:
                        print 'Invalid AM/PM value.'
                    # print "AM/PM value is: %s" % self.am_pm
                else:
                    print 'The hour should be in between 1 to 12, minute and second should be 0 to 59.'
            else:
                print 'The time have more or less values then expected.'
        except:
            print 'The hour, minute or seconds have other values than integer.'

        # print "Input time validation: %r" % self.input_validation
        self.validation_output = [self.input_validation, self.am_pm, self.time_trimmed, self.new_h_24, self.time_const_part]
        return self.validation_output

    def formatter(self, validation_output):
        # validation_output = [self.input_validation, self.am_pm, self.time_trimmed, self.new_h_24]
        self.input_validation = validation_output[0]
        self.am_pm = validation_output[1]
        self.time_trimmed = validation_output[2]
        self.new_h_24 = validation_output[3]
        self.time_const_part = validation_output[4]
        if (self.input_validation is True):
            if ('am' == self.am_pm):
                # print "AM found"
                if ('12' in self.time_trimmed[0:2]):
                    h_24 = int(self.time_trimmed[0:2])
                    h_24 = h_24 - 12
                    self.new_h_24 = '0' + str(h_24)

            elif ('pm' == self.am_pm):
                # print "PM found"
                if ('12' not in self.time_trimmed[0:2]):
                    h_24 = int(self.time_trimmed[0:2])
                    self.h_24 = h_24 + 12
                    self.new_h_24 = str(h_24)

            final_time = self.new_h_24 + self.time_const_part
            print 'Formatted 24 hour time is: %s' % final_time

        else:
            print "Invalid time format. Please input a valid time."

validation = Time_Formatter().input_validator()
# print validation
convert = Time_Formatter().formatter(validation)
