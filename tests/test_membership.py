from src.membership import calculate_membership_fee


def test_premium_membership():
    assert calculate_membership_fee(
        age=30,
        membership_type="premium",
        access_day="weekday",
        membership_duration=6
    ) == "Unlimited Access"