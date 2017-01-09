class Time_Formatter():

    def input_validator(self):
        '''
        This method will receive time input from user in AM/PM format then validate the input.
        :return:
        Re-formatted time string (time_trimmed), Input validation boolean (input_validation), AM/PM value string (am_pm), Validation error message string (error_message)
        '''
        # Get the time input from user
        time_input = raw_input("Please input time in AM/PM format. Example, 09:34:12PM: ")
        # Make the time input into all upper case.
        time_input = time_input.upper()
        # trim unnecessary blank space from the time input
        time_trimmed = time_input.replace(" ", "")
        am_pm = ''
        input_validation = False
        error_message = 'Unknown Error'
        hour_separator = time_trimmed[2:3]
        min_separator = time_trimmed[5:6]

        try:
            # Validate that the hour, minute and seconds in time input are in valid range.
            if (0 < int(time_trimmed[0:2]) < 13 and 0 <= int(time_trimmed[3:5]) < 60 and 0 <= int(time_trimmed[6:8]) < 60):
                # Validate that the time input has hour, minute and second value in proper format.
                if (len(time_trimmed) == 10) and ':' in hour_separator and ':' in min_separator:
                    # Check for AM/PM value and reassign am_pm accordingly.
                    if ("AM" in time_trimmed[8:]):
                        am_pm = 'am'
                        input_validation = True
                    elif ("PM" in time_trimmed[8:]):
                        am_pm = 'pm'
                        input_validation = True
                    else:
                        error_message = 'Invalid AM/PM value.'
                else:
                    error_message = 'The time have unexpected values'
            else:
                error_message = 'The hour should be in between 1 to 12, minute and second should be 0 to 59.'
        except:
            error_message = 'The hour, minute or seconds have other values than integer.'

        # Made a list of return variables from this input_validator method.
        validation_output = [time_trimmed, input_validation, am_pm, error_message]
        return validation_output

    def formatter(self, validation_output):
        '''
        :param validation_output: contains validation_output list from the input_validator method
        :return: final output time string in 24 hour format or error message
        '''
        # Get values from parameter validation_output
        time_trimmed = validation_output[0]
        input_validation = validation_output[1]
        am_pm = validation_output[2]
        error_message = validation_output[3]

        # Separate minute and second value from input time which will not be changed in 24 hour format
        time_const_part = time_trimmed[2:8]
        # Separate hour value from input time
        hour_str = time_trimmed[0:2]

        # Re-calculate hour value for 24 hour time format.
        if input_validation is True:
            if ('am' == am_pm):
                if ('12' in time_trimmed[0:2]):
                    hour_int = int(time_trimmed[0:2])
                    hour_int = hour_int - 12
                    hour_str = '0' + str(hour_int)

            elif ('pm' == am_pm):
                if ('12' not in time_trimmed[0:2]):
                    hour_int = int(time_trimmed[0:2])
                    hour_int = hour_int + 12
                    hour_str = str(hour_int)

            # Generate new 24 hour time format by combining new hour value and old minute and second value.
            output_time = hour_str + time_const_part
            final_output = 'Formatted 24 hour time is: %s' % output_time

        else:
            final_output = "Invalid time format. Please input a valid time.\nError: %s" % error_message
        return final_output

# Create new object validation to get the validation_output value.
validation = Time_Formatter().input_validator()
# Create new object converted_time to get the 24 hour time format then print the output.
converted_time = Time_Formatter().formatter(validation)
print converted_time
raw_input("Press enter to exit...")