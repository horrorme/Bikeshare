from datetime import datetime
from datetime import timedelta
import time
import pandas as pd
import numpy as np

"""
#0 Acquire filters
"""

def acquire_filter_city():


    """
    Asks the user to choose the city.

    Arguments:
        None

    Returns:
        (str) of the city to use it's csv file
    """

    city = ''

    while city not in ["chicago", "new york city", "washington"]:

        city = str(input("Enter City name: (chicago, new york city, washington) ")).lower()


        if city == "chicago":
            return 'chicago.csv'

        elif city == "new york city":
            return 'new_york_city.csv'

        elif city == "washington":
            return 'washington.csv'

        else:
            print("Make sure to enter the right city")






def acquire_time_filter():


    """
    Asks the user for a time period to be used as a filter.

    Arguments:
        none.

    Returns:
        (str) of the time filter to be used.
    """
    time_filter = ''
    while time_filter.lower() not in ['month', 'day', 'none']:
        time_filter = input('\nApply filter by month, day, or none.\n')
        if time_filter.lower() not in ['month', 'day', 'none']:
            print('Input not valid.')
    return time_filter







def acquire_filter_month():


    """
    Asks the user to choose the month.

    Arguments:
        None

    Returns:
        (str) of the month to filter the data with.
    """
    month_input = ""
    months_dict = {'january': 1, 'february': 2, 'march': 3, 'april': 4,
                   'may': 5, 'june': 6}
    while month_input.lower() not in months_dict.keys():
        month_input = input('\nWhich month? January, February, March, April,'
                            ' May, or June?\n')
        if month_input.lower() not in months_dict.keys():
            print('Input not valid, please type in a '
                  'month between January and June')
    month = months_dict[month_input.lower()]
    return ('2017-{}'.format(month), '2017-{}'.format(month + 1))



def acquire_filter_day():


    """
    Asks the user for a day and returns the specified day.

    Arguments:
        none.

    Returns:
        (tuple) Lower limit, upper limit of date for the bikeshare data.
    """
    this_month = acquire_filter_month()[0]
    month = int(this_month[5:])
    valid_date = False
    while valid_date == False:
        is_int = False
        day = input('\nEnter the day number:\n')
        while is_int == False:
            try:
                day = int(day)
                is_int = True
            except ValueError:
                print('Invalid number')
                day = input('\nEnter the day number:\n')
        try:
            start_date = datetime(2017, month, day)
            valid_date = True
        except ValueError as e:
            print(str(e).capitalize())
    end_date = start_date + timedelta(days=1)
    return (str(start_date), str(end_date))



"""
#1 Popular times of travel
"""

def most_common_month(df):


    """
    Finds the most popular month for the start time.

    Arguments:
        bikeshare dataframe

    Returns:
        none
    """
    months = ['January', 'February', 'March', 'April', 'May', 'June']
    index = int(df['start_time'].dt.month.mode())
    most_popular_month = months[index - 1]
    print('The most popular month is {}.'.format(most_popular_month))




def most_common_day(df):


    """
    Finds the most common day for the start time.

    Arguments:
        bikeshare dataframe

    Returns:
        none
    """
    days_of_week = ['Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    index = int(df['start_time'].dt.dayofweek.mode())
    most_popular_day = days_of_week[index]
    print('The most popular day of week for start time is {}.'.format(most_popular_day))




def most_common_hour(df):


    """
    Finds the most common hour of the day for the start time.

    Arguments:
        bikeshare dataframe

    Returns:
        none
    """
    most_popular_hour = int(df['start_time'].dt.hour.mode())
    if most_popular_hour == 0:
        am_pm = 'am'
        popular_hour_readable = 12
    elif 1 <= most_popular_hour < 13:
        am_pm = 'am'
        popular_hour_readable = most_popular_hour
    elif 13 <= most_popular_hour < 24:
        am_pm = 'pm'
        popular_hour_readable = most_popular_hour - 12
    print('The most common hour of the day for the start time is {}{}.'.format(popular_hour_readable, am_pm))




"""
#2 Popular stations and trip
"""

def popular_stations(df):


    """
    Finds the most popular start station and the most popular end station.

    Arguments:
        bikeshare dataframe

    Returns:
        none
    """
    popular_start_station = df['start_station'].mode().to_string(index = False)
    popular_end_station = df['end_station'].mode().to_string(index = False)
    print('The most popular start station is {}.'.format(popular_start_station))
    print('The most popular end station is {}.'.format(popular_end_station))




def popular_trip(df):


    """
    Finds the most popular trip.

    Arguments:
        bikeshare dataframe

    Returns:
        none
    """
    most_popular_trip = df['journey'].mode().to_string(index = False)
    # The 'journey' column is created in
    # the main() function.
    print('The most popular trip is {}.'.format(most_popular_trip))




"""
#3 Trip duration
"""
def trip_duration(df):


    """
    Finds and prints the total trip duration and average trip duration in hours, minutes, and seconds.

    Arguments:
        bikeshare dataframe

    Returns:
        none
    """
    total_trip_duration = df['trip_duration'].sum()
    minute, second = divmod(total_trip_duration, 60)
    hour, minute = divmod(minute, 60)
    print('The total trip duration is {} hours, {} minutes and {}'
          ' seconds.'.format(hour, minute, second))
    avg_duration = round(df['trip_duration'].mean())
    m, s = divmod(avg_duration, 60)
    if m > 60:
        h, m = divmod(m, 60)
        print("The average trip duration is {} hours, {} minutes and {} seconds.".format(h, m, s))
    else:
        print('The average trip duration is {} minutes and {} seconds.'.format(m, s))



"""
#4 User info
"""
def user_type(df):


    """
    Finds the count of each user type.

    Arguments:
        bikeshare dataframe

    Returns:
        none
    """
    subscribers = df.query("user_type == 'Subscriber'").user_type.count()
    customers = df.query("user_type == 'Customer'").user_type.count()
    print("There are {} Subscribers and {} Customers.".format(subscribers, customers))

def gender_type(df):


    """
    Finds the count of each gender.

    Arguments:
        bikeshare dataframe

    Returns:
        none
    """
    males_count = df.query('gender == "Male"').gender.count()
    females_count = df.query('gender == "Male"').gender.count()
    print('There are {} males users and {} females users.'.format(males_count, females_count))

def birth_years(df):


    """
    Finds the earliest aka oldest user, most recent aka youngest user, and most popular birth years.

    Arguments:
        bikeshare dataframe

    Returns:
        none
    """
    earliest = int(df['birth_year'].min())
    latest = int(df['birth_year'].max())
    mode = int(df['birth_year'].mode())
    print('The oldest users are born in {}.\nThe youngest users are born in {}.'
          '\nThe most popular birth year is {}.'.format(earliest, latest, mode))


def display_data(df):
    """"
    Displays five lines of data if the user specifies that they would like to.
    After displaying five lines, ask the user if they would like to see five more,
    continuing asking until they say stop.

    Arguments:
        data frame

    Returns:
        none
    """
    def is_valid(display):
        if display.lower() in ['yes', 'no']:
            return True
        else:
            return False
    head = 0
    tail = 5
    valid_input = False
    while valid_input == False:
        display = input('\nWould you like to view individual trip data? '
                        'Type \'yes\' or \'no\'.\n')
        valid_input = is_valid(display)
        if valid_input == True:
            break
        else:
            print("Sorry, I do not understand your input. Please type 'yes' or"
                  " 'no'.")
    if display.lower() == 'yes':
        # prints every column except the 'journey' column created in statistics()
        print(df[df.columns[0:-1]].iloc[head:tail])
        display_more = ''
        while display_more.lower() != 'no':
            valid_input_2 = False
            while valid_input_2 == False:
                display_more = input('\nWould you like to view more individual'
                                     ' trip data? Type \'yes\' or \'no\'.\n')
                valid_input_2 = is_valid(display_more)
                if valid_input_2 == True:
                    break
                else:
                    print("Sorry, I do not understand your input. Please type "
                          "'yes' or 'no'.")
            if display_more.lower() == 'yes':
                head += 5
                tail += 5
                print(df[df.columns[0:-1]].iloc[head:tail])
            elif display_more.lower() == 'no':
                break


def main():


    """
    Calculates the descriptive statistics about a city and
    time period specified by the user via raw input.

    Arguments:
        none.

    Returns:
        none.
    """
    # Filter by city (Chicago, New York, Washington)
    city = acquire_filter_city()
    print('Loading data...')
    df = pd.read_csv(city, parse_dates = ['Start Time', 'End Time'])

    # change all column names to lowercase letters
    # and replace spaces with underscores
    new_labels = []
    for col in df.columns:
        new_labels.append(col.replace(' ', '_').lower())
    df.columns = new_labels

    # increases the column width so that the long strings in the 'journey'
    # column can be displayed fully
    pd.set_option('max_colwidth', 100)



    # creates a 'journey' column that concatenates
    # 'start_station' with 'end_station' for
    #  the use most_popular_trip() function
    df['journey'] = df['start_station'].str.cat(df['end_station'], sep=' to ')

    # Filter by time period (month, day, none)
    time_filter = acquire_time_filter()
    if time_filter == 'none':
        df_filtered = df
    elif time_filter == 'month' or time_filter == 'day':
        if time_filter == 'month':
            filter_lower, filter_upper = acquire_filter_month()
        elif time_filter == 'day':
            filter_lower, filter_upper = acquire_filter_day()
        print('Filtering data...')
        df_filtered = df[(df['start_time'] >= filter_lower) & (df['start_time'] < filter_upper)]
    print('\nLoading...')

    if time_filter == 'none':


        # Which is the most popular month for start time?
        most_common_month(df_filtered)

        print("\nLoading...")

    if time_filter == 'none' or time_filter == 'month':


        # Which is the most popular day of week
        # (Monday, Tuesday, etc.) for start time?
        most_common_day(df_filtered)

        print("\nLoading...")


    # Which is the most popular hour of day for start time?
    most_common_hour(df_filtered)

    print("\nLoading...")


    # What is the total trip duration and average trip duration?
    trip_duration(df_filtered)

    print("\nLoading...")


    # Which is the most popular start station and
    # most popular end station?
    popular_stations(df_filtered)

    print("\nLoading...")


    # Which is the most popular trip?
    popular_trip(df_filtered)

    print("\nLoading...")


    # What is the count for each user type?
    user_type(df_filtered)


    if city == 'chicago.csv' or city == 'new_york_city.csv':
        print("\nLoading...")


        # What is the count for each gender?
        gender_type(df_filtered)

        print("\nLoading...")


        # who are the oldest and youngest users?
        # And what are the most popular birth years
        birth_years(df_filtered)

    # Display five lines of data at a time if user specifies that they would like to
    display_data(df_filtered)

    # Restart?
    restart = input('\nWould you like to restart? Type \'yes\' or \'no\'.\n')
    while restart.lower() not in ['yes', 'no']:
        print("Invalid input. Please type 'yes' or 'no'.")
        restart = input('\nWould you like to restart? Type \'yes\' or \'no\'.\n')
    if restart.lower() == 'yes':
        main()



if __name__ == "__main__":
	main()
