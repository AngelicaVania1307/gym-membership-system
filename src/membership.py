PREMIUM_TYPE = "premium"


def calculate_membership_fee(
    age,
    membership_type,
    access_day,
    membership_duration
):

    if membership_duration < 1 or membership_duration > 12:
        raise ValueError("Invalid membership duration")
    
    if access_day not in ["weekday", "weekend"]:
        raise ValueError("Invalid access day")

    if membership_type == PREMIUM_TYPE:
        return "Unlimited Access"

    return 50