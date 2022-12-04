import time
import pandas as pd
import numpy as np

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
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True :
        city = input("Among these cities (chicago, new York City, washington), which one do you want to pick?")
        if city in ("chicago", "new york city", "washington") :
            break
        else : 
            print("just choose one of the three mentioned")

    # get user input for month (all, january, february, ... , june)
    while True : 
        month = input("What is your favorite month among (January', 'February', 'March', 'April', 'May', 'June') ? if you like all the months of the year you can pick All of them ")
        if month in ('All', 'January', 'February', 'March', 'April', 'May', 'June' ):
            break
        else : 
            print("choose one of the month mentionned or all of them !")

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True :
        day = input("Same thing :), do you have a favorite day of the week ? , pick all of them if you like them all ")
        if day in ("All", "Monday","Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"):
            break
        else : 
            print("Pick a Day of the week or all of them")


    print('-'*40)
    return city, month, day


def load_data(city, month, day):
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
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    if month != 'all' : 
         months = ['January', 'February', 'March', 'April', 'May', 'June']
         month = months.index(month) + 1

         df = df[df['month'] == month]

    if day != 'all':
      
        df = df[df['day_of_week'] == day.title()]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month

    popular_month = df['month'].mode()[0]
    print('Most Common Month:', popular_month)


    # display the most common day of week

    popular_day = df['day_of_week'].mode()[0]
    print('Most Common day:', popular_day)

    # display the most common start hour

    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('Most Common Hour:', popular_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station

    Start_Station = df['Start Station'].value_counts().idxmax()
    print('Most Commonly used start station:', Start_Station)


    # TO DO: display most commonly used end station

    End_Station = df['End Station'].value_counts().idxmax()
    print('\nMost Commonly used end station:', End_Station)


    # TO DO: display most frequent combination of start station and end station trip

    Combination_Station = df.groupby(['Start Station', 'End Station']).count()
    print('\nMost Commonly used combination of start station and end station trip:', Start_Station, " & ", End_Station)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time

    Total_Travel_Time = sum(df['Trip Duration'])
    print('Total travel time:', Total_Travel_Time/86400, " Days")


    # TO DO: display mean travel time

    Mean_Travel_Time = df['Trip Duration'].mean()
    print('Mean travel time:', Mean_Travel_Time/60, " Minutes")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types

    user_types = df['User Type'].value_counts()
    #print(user_types)
    print('User Types:\n', user_types)

    # TO DO: Display counts of gender

    try:
      gender_types = df['Gender'].value_counts()
      print('\nGender Types:\n', gender_types)
    except KeyError:
      print("\nGender Types:\nNo data available for this month.")

    # TO DO: Display earliest, most recent, and most common year of birth

    try:
      Earliest_Year = df['Birth Year'].min()
      print('\nEarliest Year:', Earliest_Year)
    except KeyError:
      print("\nEarliest Year:\nNo data available for this month.")

    try:
      Most_Recent_Year = df['Birth Year'].max()
      print('\nMost Recent Year:', Most_Recent_Year)
    except KeyError:
      print("\nMost Recent Year:\nNo data available for this month.")

    try:
      Most_Common_Year = df['Birth Year'].value_counts().idxmax()
      print('\nMost Common Year:', Most_Common_Year)
    except KeyError:
      print("\nMost Common Year:\nNo data available for this month.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def show_data(df):  
    
    response = ['yes', 'no']
    data = ''
    # tag initialized to focus only details from
    #a particular point is displayed
    start_loc = 0
    while data not in response:
        print('\nWould you like to view 5 rows of individual trip data?\n')
        print("\n Enter yes or no\n'")
        data = input().lower()
        #the raw data from the df is displayed if user opts for it
        if data == "yes":
            print(df.head())
        elif data not in response:
            print("\n wrong input.")
            print("No match.")
            print("\nBegin over\n")

    #while loop to avoid infinite loop
    while data == 'yes':
        print(" Do you wish to continue ? :")
        start_loc += 5
        data = input().lower()
        # displays next 5 rows if the user choose to
        if data == "yes":
             print(df[start_loc:start_loc+5])
        elif data != "yes":
             break

    print('-'*40)    

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        show_data(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
