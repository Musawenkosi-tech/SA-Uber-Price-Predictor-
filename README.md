# SA-Uber-Price-Predictor-

A data engineering + analytics project that simulates Uber ride data in Pretoria and builds a pricing pipeline to estimate ride fares based on distance, time, and traffic conditions.This project is part of my journey into data engineering, focusing on building practical, real-world systems that simulate industry use cases.


## Project Overview

This project demonstrates how a real-world data pipeline works by:

* Generating synthetic ride data (since real Uber data is not publicly available)
* Cleaning and transforming the data
* Engineering meaningful features (e.g., rush hour, trip duration)
* Applying a pricing model to estimate ride costs

The goal is to simulate how companies like Uber calculate dynamic pricing and extract insights from transportation data.

## Pipeline Architecture

The project follows a modular data pipeline structure:


##Uber-Price-Predictor/
- main.py
- test_pipeline.ipynb
- README.md

src/
- generate_data.py
- clean_data.py
- feature_engineering.py
- pricing_model.py

data/
- processed_uber_data.csv

#How the Pipeline Works

1. **Data Generation**

   * Simulates ride data with pickup/dropoff coordinates and timestamps

2. **Data Cleaning**

   * Removes unrealistic trips (e.g., distance < 1km or > 50km)

3. **Feature Engineering**

   * Extracts hour of day
   * Identifies rush hour periods
   * Calculates trip duration

4. **Pricing Model**

   * Base fare + distance cost + time cost
   * Applies surge pricing during peak hours
   * Ensures a minimum fare

5. **Output**

   * Saves processed dataset to 

##  Key Features

1. Synthetic data generation (realistic simulation)
2. Distance calculation using coordinates
3. Rush hour detection (traffic-based pricing)
4. Dynamic pricing model with surge multiplier
5. Data visualization (Jupyter Notebook)
6. Modular, production-style pipeline structure

## Tech Stack

* **Language:** Python
* **Libraries:** Pandas, NumPy, Matplotlib
* **Environment:** Jupyter Notebook (Anaconda)
* **Concepts:**

  * Data pipelines
  * Feature engineering
  * ETL (Extract, Transform, Load)
  * Data analysis & visualization

## How to Run

### Option 1: Run the pipeline
open:
main.py an run this file

### Option 2: Use Jupyter Notebook
Open:
test_pipeline.ipynb
and run all cells to explore the data and visualizations.

---

## Sample Insights

* Ride prices increase significantly during rush hours (7–9 AM, 4–6 PM)
* Longer distances strongly correlate with higher prices
* Traffic conditions (slower trips) increase total fare


## What I Learned

* How to structure a real-world data pipeline
* Writing modular and reusable Python code
* Feature engineering for business problems
* Simulating datasets when real data is unavailable
* Building portfolio-ready data engineering projects

## Future Improvements

* [ ] Add machine learning model for price prediction
* [ ] Store data in a database (PostgreSQL/MySQL)
* [ ] Build a dashboard (Streamlit/Power BI)
* [ ] Deploy as an API (Flask/FastAPI)
* [ ] Use real-world datasets if available

## Author

**Musa Mhlambi**
Aspiring Data Engineer

* Pretoria, South Africa
* LinkedIn: https://www.linkedin.com/in/musawenkosi-mhlambi-04b5ba310



