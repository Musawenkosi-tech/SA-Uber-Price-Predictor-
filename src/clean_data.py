import numpy as np

def clean_data(df):
    df['distance_km'] = np.sqrt(
        (df['dropoff_longitude'] - df['pickup_longitude'])**2 +
        (df['dropoff_latitude'] - df['pickup_latitude'])**2
    ) * 111.32

    df = df[(df['distance_km'] > 1) & (df['distance_km'] < 50)]

    return df