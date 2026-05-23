WEEKEND_EXTRA = 5
PREMIUM_TYPE = "premium"


def calculate_membership_fee(
    age,
    membership_type,
    access_day,
    membership_duration
):

    fee = 50

    if membership_type == PREMIUM_TYPE:
        return "Unlimited Access"

    if access_day == "weekend":
        fee += WEEKEND_EXTRA

    return fee