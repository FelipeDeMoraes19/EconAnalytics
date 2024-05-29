import pandas as pd
import matplotlib.pyplot as plt
import os

def load_cleaned_data(filename):
    filepath = os.path.join('data/processed', filename)
    if os.path.exists(filepath):
        data = pd.read_csv(filepath)
        data['date'] = pd.to_datetime(data['date'], errors='coerce')
        print(f"{filename} Data Types:")
        print(data.dtypes)
        print(data.head())
        return data
    else:
        raise FileNotFoundError(f"File {filepath} does not exist.")

gdp_data = load_cleaned_data('gdp_data_cleaned.csv')
inflation_data = load_cleaned_data('inflation_data_cleaned.csv')
unemployment_data = load_cleaned_data('unemployment_data_cleaned.csv')

gdp_data.plot(x='date', y='value', title='GDP Over Time')
plt.show()

inflation_data.plot(x='date', y='value', title='Inflation Over Time')
plt.show()

unemployment_data.plot(x='date', y='value', title='Unemployment Rate Over Time')
plt.show()
