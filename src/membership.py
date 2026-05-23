WEEKEND_EXTRA = 5


def calculate_membership_fee(
    age,
    membership_type,
    access_day,
    membership_duration
):

    fee = 50

    if access_day == "weekend":
        fee += WEEKEND_EXTRA

    return fee