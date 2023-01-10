
user_input_message = "Hey user, enter number of days and conversion unit separated with colon!\n"


def days_to_units(num_of_days, conversion_unit):
    if conversion_unit == "hours":
        return f"{num_of_days} days are {num_of_days * 24} {conversion_unit}"
    elif conversion_unit == "minutes":
        return f"{num_of_days} days are {num_of_days * 24 * 60} {conversion_unit}"
    elif conversion_unit == "seconds":
        return f"{num_of_days} days are {num_of_days * 24 * 60 * 60} {conversion_unit}"
    elif conversion_unit == "milliseconds":
        return f"{num_of_days} days are {num_of_days * 24 * 60 * 60 * 1000} {conversion_unit}"
    elif conversion_unit == "microseconds":
        return f"{num_of_days} days are {num_of_days * 24 * 60 * 60 * 1000000} {conversion_unit}"
    elif conversion_unit == "nanoseconds":
        return f"{num_of_days} days are {num_of_days * 24 * 60 * 60 * 1000000000} {conversion_unit}"
    else:
        return "Unsupported unit!"


def validate_and_execute(days_and_unit_dic):
    try:
        user_input_number = int(days_and_unit_dic["days"])
        # we want to do conversion only for positive integers
        if user_input_number > 0:
            calculated_value = days_to_units(user_input_number, days_and_unit_dic["unit"])
            print(calculated_value)
        elif user_input_number == 0:
            return "You entered '0', please enter a valid positive number"
    except ValueError:
        print("your input is not a number. Don't ruin my program!")
