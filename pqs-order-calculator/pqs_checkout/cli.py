"""Command-line interface for the PQS checkout calculator."""

from __future__ import annotations

from .calculator import apply_discount, calculate_shipping, calculate_subtotal

APP_TITLE = "PQS Premium Checkout Calculator"


def _read_prices() -> list[float]:
    raw = input("Enter item prices separated by commas: ").strip()
    if not raw:
        raise ValueError("At least one item price is required.")
    return [float(value.strip()) for value in raw.split(",")]


def main() -> None:
    print(f"\n{APP_TITLE}")
    print("-" * len(APP_TITLE))

    try:
        prices = _read_prices()
        discount_percent = float(input("Enter discount percentage (0-100): ").strip() or "0")

        subtotal = calculate_subtotal(prices)
        discounted_subtotal = apply_discount(subtotal, discount_percent)
        shipping = calculate_shipping(discounted_subtotal)
        total = round(discounted_subtotal + shipping, 2)

        print(f"\nSubtotal: ${subtotal:.2f}")
        print(f"After discount: ${discounted_subtotal:.2f}")
        print(f"Shipping: ${shipping:.2f}")
        print(f"Final total: ${total:.2f}")
    except ValueError as error:
        print(f"Input error: {error}")


if __name__ == "__main__":
    main()
