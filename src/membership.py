def calculate_membership_fee(
    age,
    membership_type,
    access_day,
    membership_duration
):

    if membership_type == "premium":
        return "Unlimited Access"

    return 50