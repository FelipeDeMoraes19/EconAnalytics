import pandas as pd

def load_cleaned_data(filename):
    filepath = f'data/processed/{filename}'
    return pd.read_csv(filepath)

gdp_data = load_cleaned_data('gdp_data_cleaned.csv')
inflation_data = load_cleaned_data('inflation_data_cleaned.csv')
unemployment_data = load_cleaned_data('unemployment_data_cleaned.csv')

print("GDP Data:")
print(gdp_data.head())
print(gdp_data.dtypes)

print("Inflation Data:")
print(inflation_data.head())
print(inflation_data.dtypes)

print("Unemployment Data:")
print(unemployment_data.head())
print(unemployment_data.dtypes)
