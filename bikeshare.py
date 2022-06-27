import time
import pandas as pd
import numpy as np
import datetime as dt

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('\nHello! Let\'s explore some US bikeshare data!')
    cities = ['chicago', 'new york city', 'washington']
    months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
    days = ['monday', 'tuesday', 'wednesday','thursday','friday','saturday','sunday','all']
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    city = input("\nPlease enter the city (Chicago, New York City, Washington): \n").lower().strip()
    while city not in cities:
        city = input("\nWrong input, please renter the city (Chicago, New York City, Washington): \n").lower().strip()
    
    # get user input for month (all, january, february, ... , june)
    month = input("\nPlease enter the month (All, January, February, March, April, May, June): \n").lower().strip()
    while month not in months:
        month = input("\nWrong input, please renter the month (All, January, February, March, April, May, June): \n").lower().strip()

    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("\nPlease enter the day: (All, Monday, Tuesday, Wednesday, ...): \n").lower().strip()
    while day not in days:
        day = input("\nWrong input, please renter the the day: (All, Monday, Tuesday, Wednesday, ...): \n").lower().strip()


    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    print(city + " " + month + " " + day)
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour

    #'all' has to be small, because it's passed as small
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]
    #'All' has to be Capital, because it's passed as Capital
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    most_common_month = df['month'].mode()[0]
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    print("\nThe most common month is: " + months[most_common_month -1].title()+ "\n")

    # display the most common day of week
    most_common_day = df['day_of_week'].mode()[0]
    print("\nThe most common day is: " + most_common_day.title() + "\n")

    # display the most common start hour
    most_common_start_hour = df['hour'].mode()[0]
    print("\nThe most common Start hour is: " + str(most_common_start_hour) + "\n")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    most_common_start_station = df['Start Station'].mode()[0]
    print("\nThe most common start station is: " + most_common_start_station.title() + "\n")

    # display most commonly used end station
    most_common_end_station = df['End Station'].mode()[0]
    print("\nThe most common end station is: " + most_common_end_station.title() + "\n")

    # display most frequent combination of start station and end station trip
    most_common_combination = (df['Start Station']  + ", "+ df['End Station']).mode()[0]
    print("\nThe most combination of start station and end station is: " + most_common_combination.title()+ "\n")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("\nTotal travel time is: " + str(total_travel_time) +" seconds \n")

    # display mean travel time
    travel_time_mean = df['Trip Duration'].mean()
    print("\nMean travel time is: " + str(travel_time_mean) +" seconds \n")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)
    print("\n")
    # Display counts of gender
    if 'Gender' in df:
        user_types = df['Gender'].value_counts()
        print(user_types)
    else:
        print("\nNo gender column found in CSV file\n")

    # Display earliest, most recent, and most common year of birth
    if('Birth Year' in df):
        earliest = df['Birth Year'].min()
        recent = df['Birth Year'].max()
        common = df['Birth Year'].mode()
        print("\nThe earliest year of birth is {}, the recent is {} and the most common is {}\n".format(int(earliest), int(recent), int(common)))
    else:
        print("\nNo birth year column found in CSV file\n")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def get_random_sample(city):
    """Displays a random sample, 5 rows of a specific city."""
    #df = load_data(city, 'all', 'All') not raw data
    df = pd.read_csv(CITY_DATA[city])
    while True:
        statement = input("\nWould you like to get a random sample? type Yes or No: \n").lower().strip()
        if statement == 'no':
            break
        elif statement == 'yes':
            print(df.sample(5))
        else:
            print("\nWrong Input")
            continue


def main():

   while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        get_random_sample(city)
        
        while True:
            statement = input("\nWould you like to restart? type Yes or No: \n").lower().strip()
            if statement == 'no':
                quit() #exits the program
            elif statement == 'yes':
                break
            else:
                print("\nWrong input")
                continue


if __name__ == "__main__":
	main()
