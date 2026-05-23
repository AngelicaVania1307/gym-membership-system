import pytest
from src.membership import calculate_membership_fee


def test_weekend_extra_charge():
    assert calculate_membership_fee(
        age=30,
        membership_type="regular",
        access_day="weekend",
        membership_duration=6
    ) == 55


def test_premium_membership():
    assert calculate_membership_fee(
        age=25,
        membership_type="premium",
        access_day="weekday",
        membership_duration=6
    ) == "Unlimited Access"

def test_invalid_membership_duration():
    with pytest.raises(ValueError):
        calculate_membership_fee(
            age=25,
            membership_type="regular",
            access_day="weekday",
            membership_duration=15
        )

def test_invalid_access_day():
    with pytest.raises(ValueError):
        calculate_membership_fee(
            age=25,
            membership_type="regular",
            access_day="holiday",
            membership_duration=6
        )