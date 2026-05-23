import pytest
from src.membership import calculate_membership_fee


def test_weekend_extra_charge():
    assert calculate_membership_fee(
        age=30,
        membership_type="regular",
        access_day="weekend",
        membership_duration=6
    ) == 55