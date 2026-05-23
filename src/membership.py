PREMIUM_TYPE = "premium"


def calculate_membership_fee(
    age,
    membership_type,
    access_day,
    membership_duration
):

    if membership_type == PREMIUM_TYPE:
        return "Unlimited Access"

    return 50