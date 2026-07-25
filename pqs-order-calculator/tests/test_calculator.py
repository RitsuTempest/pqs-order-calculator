"""Five required unit tests: three pass and two intentionally fail."""

from pqs_checkout.calculator import (
    apply_discount,
    calculate_shipping,
    calculate_subtotal,
    calculate_total,
)


def test_calculate_subtotal_passes() -> None:
    assert calculate_subtotal([10.00, 15.50, 4.50]) == 30.00


def test_apply_discount_passes() -> None:
    assert apply_discount(200.00, 10) == 180.00


def test_free_shipping_threshold_passes() -> None:
    assert calculate_shipping(100.00) == 0.00


def test_shipping_below_threshold_intentionally_fails() -> None:
    assert calculate_shipping(50.00) == 0.00


def test_discounted_total_intentionally_fails() -> None:
    assert calculate_total([50.00, 50.00], 10) == 90.00
