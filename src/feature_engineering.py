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
    df['is_rush_hour'] = df['hour'].isin([6, 7, 8, 9, 16, 17, 18,19])
    mask = df['hour'].isin([0, 1, 2, 3, 4, 5, 10, 11, 12, 13, 14, 15, 19, 20, 21, 22, 23])
    rush_mask = df['hour'].isin([6, 7, 8, 9])
    evening_mask = df['hour'].isin([16, 17, 18])


    # 5. Traffic speed
    df['minute_per_km'] = np.where(
        df['is_rush_hour'],
        np.random.uniform(1.9, 2.3, len(df)),
        np.random.uniform(1.3, 1.5, len(df))  
    )

    # 6. Duration
    df['duration_min'] = df['distance_km'] * df['minute_per_km']

    # 7. Surge pricing
    df.loc[mask,'surge_multiplier'] = np.random.uniform(1.0, 1.2, mask.sum()) 
    df.loc[rush_mask, 'surge_multiplier'] = np.random.uniform(1.3, 1.6, rush_mask.sum())
    df.loc[evening_mask, 'surge_multiplier'] = np.random.uniform(1.4, 1.8, evening_mask.sum())
    return df
