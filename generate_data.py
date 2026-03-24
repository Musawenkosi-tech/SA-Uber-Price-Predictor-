import pandas as pd
import numpy as np

def generate_data(n_rides=10000):
    np.random.seed(42)

    df = pd.DataFrame({
        'pickup_datetime': pd.date_range('2026-01-01', periods=n_rides, freq='5min'),
        'pickup_longitude': np.random.uniform(28.10, 28.30, n_rides),
        'pickup_latitude': np.random.uniform(-25.75, -25.65, n_rides),
        'dropoff_longitude': np.random.uniform(28.10, 28.30, n_rides),
        'dropoff_latitude': np.random.uniform(-25.75, -25.65, n_rides),
    })

    return df