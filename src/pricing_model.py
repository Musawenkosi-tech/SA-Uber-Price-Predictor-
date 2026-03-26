import numpy as np

def calculate_price(df):
    base_fare = 12
    rate_per_km = 6
    rate_per_min = 0.7

    subtotal = (
        base_fare +
        df['distance_km'] * rate_per_km +
        df['duration_min'] * rate_per_min 
        )

    return np.maximum(20, subtotal * df['surge_multiplier'])
