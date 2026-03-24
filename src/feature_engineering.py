import numpy as np

def add_features(df):
    # 1. Distance calculation
    df['distance_km'] = np.sqrt(
        (df['dropoff_longitude'] - df['pickup_longitude'])**2 +
        (df['dropoff_latitude'] - df['pickup_latitude'])**2
    ) * 111.32

    # 2. Remove invalid trips
    df = df[(df['distance_km'] > 1) & (df['distance_km'] < 50)]

    # 3. Extract hour
    df['hour'] = df['pickup_datetime'].dt.hour

    # 4. Rush hour logic
    df['is_rush_hour'] = df['hour'].isin([7, 8, 16, 17, 18])

    # 5. Traffic speed
    df['minute_per_km'] = np.where(
        df['is_rush_hour'],
        np.random.uniform(1.9, 2.3, len(df)),
        np.random.uniform(1.3, 1.5, len(df))
    )

    # 6. Duration
    df['duration_min'] = df['distance_km'] * df['minute_per_km']

    # 7. Surge pricing
    df['surge_multiplier'] = np.where(df['is_rush_hour'], 1.4, 1.0)

    return df