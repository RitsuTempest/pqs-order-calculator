"""Business rules for a small retail checkout calculator."""

from __future__ import annotations

from collections.abc import Iterable


def calculate_subtotal(prices: Iterable[float]) -> float:
    """Return the sum of non-negative item prices rounded to two decimals."""
    values = list(prices)
    if any(price < 0 for price in values):
        raise ValueError("Item prices cannot be negative.")
    return round(sum(values), 2)


def apply_discount(subtotal: float, discount_percent: float) -> float:
    """Apply a percentage discount and return the discounted subtotal."""
    if subtotal < 0:
        raise ValueError("Subtotal cannot be negative.")
    if not 0 <= discount_percent <= 100:
        raise ValueError("Discount percentage must be between 0 and 100.")
    return round(subtotal * (1 - discount_percent / 100), 2)


def calculate_shipping(discounted_subtotal: float, free_shipping_threshold: float = 100.0) -> float:
    """Return $0 shipping at or above the threshold; otherwise return $10."""
    if discounted_subtotal < 0:
        raise ValueError("Subtotal cannot be negative.")
    return 0.0 if discounted_subtotal >= free_shipping_threshold else 10.0


def calculate_total(prices: Iterable[float], discount_percent: float = 0.0) -> float:
    """Calculate the final order total after discount and shipping."""
    subtotal = calculate_subtotal(prices)
    discounted_subtotal = apply_discount(subtotal, discount_percent)
    shipping = calculate_shipping(discounted_subtotal)
    return round(discounted_subtotal + shipping, 2)
