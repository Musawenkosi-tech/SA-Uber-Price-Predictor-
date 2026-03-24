import numpy as np

def calculate_price(df):
    base_fare = 15
    booking_fee = 4
    rate_per_km = 11
    rate_per_min = 0.9

    subtotal = (
        base_fare +
        df['distance_km'] * rate_per_km +
        df['duration_min'] * rate_per_min +
        booking_fee
    )

    return np.maximum(20, subtotal * df['surge_multiplier'])