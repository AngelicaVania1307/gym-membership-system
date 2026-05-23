WEEKEND_EXTRA = 5
PREMIUM_TYPE = "premium"
MIN_DURATION = 1
MAX_DURATION = 12
VALID_ACCESS_DAYS = ["weekday", "weekend"]

def calculate_membership_fee(
    age,
    membership_type,
    access_day,
    membership_duration
):

    if membership_duration < MIN_DURATION or membership_duration > MAX_DURATION:
        raise ValueError("Invalid membership duration")
    
    if access_day not in VALID_ACCESS_DAYS:
        raise ValueError("Invalid access day")
    fee = 50

    if membership_type == PREMIUM_TYPE:
        return "Unlimited Access"

    if access_day == "weekend":
        fee += WEEKEND_EXTRA

    return fee