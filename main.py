from src.generate_data import generate_data
from src.clean_data import clean_data
from src.feature_engineering import add_features
from src.pricing_model import calculate_price

def run_pipeline():
    df = generate_data()
    df = clean_data(df)
    df = add_features(df)
    
    df['price'] = calculate_price(df)

    df.to_csv("data/processed_uber_data.csv", index=False)

    print("Pipeline complete ✅")

if __name__ == "__main__":
    run_pipeline()