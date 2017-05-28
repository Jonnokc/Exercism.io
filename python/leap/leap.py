def is_leap_year(year=''):

    if year % 4 == 0:
        divCheck = True
    else:
        divCheck = False

    if year % 100 == 0:
        oneHunCheck = True
    else:
        oneHunCheck = False

    if year % 400 == 0:
        fourHunCheck = True
    else:
        fourHunCheck = False

    if divCheck is False:
        return False

    if divCheck is True and oneHunCheck is True and fourHunCheck is False:
        return False
    else:
        return True
