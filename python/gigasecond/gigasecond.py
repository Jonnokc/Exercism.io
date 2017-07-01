# Calculate the moment when someone has lived for 109 seconds.
#
# A gigasecond is 10^9 (1,000,000,000) seconds.


from datetime import timedelta


def add_gigasecond(user_date):

    difference = timedelta(seconds=10**9)

    new_date = user_date + difference

    return new_date
