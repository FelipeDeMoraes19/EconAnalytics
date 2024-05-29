import pandas as pd
import os

def load_data(filename):
    filepath = os.path.join('../../data/raw', filename)
    data = pd.read_csv(filepath)
    return data

def clean_data(data):
    cleaned_data = data.dropna()
    return cleaned_data

def save_cleaned_data(data, filename):
    filepath = os.path.join('../../data/processed', filename)
    data.to_csv(filepath, index=False)

if __name__ == "__main__":
    gdp_data = load_data('gdp_data.csv')
    inflation_data = load_data('inflation_data.csv')
    unemployment_data = load_data('unemployment_data.csv')

    gdp_cleaned = clean_data(gdp_data)
    inflation_cleaned = clean_data(inflation_data)
    unemployment_cleaned = clean_data(unemployment_data)

    save_cleaned_data(gdp_cleaned, 'gdp_data_cleaned.csv')
    save_cleaned_data(inflation_cleaned, 'inflation_data_cleaned.csv')
    save_cleaned_data(unemployment_cleaned, 'unemployment_data_cleaned.csv')

    print("Data processing complete!")
