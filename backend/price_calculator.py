def calculate_price(
    location_rate,
    area,
    bedrooms,
    bathrooms,
    parking,
    property_age
):
    base_price = location_rate * area

    bedroom_adjustment = bedrooms * 100000

    bathroom_adjustment = bathrooms * 75000

    parking_adjustment = parking * 150000

    age_depreciation = property_age * 25000

    estimated_price = (
        base_price
        + bedroom_adjustment
        + bathroom_adjustment
        + parking_adjustment
        - age_depreciation
    )

    return max(estimated_price, 0)
