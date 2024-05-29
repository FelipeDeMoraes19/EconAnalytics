import os
import pandas as pd

def process_data(filename):
    filepath = os.path.join('data/raw', filename)
    if os.path.exists(filepath):
        data = pd.read_csv(filepath)
        data['date'] = pd.to_datetime(data['date'].str.extract(r'(\d{4})')[0], format='%Y') 
        data['value'] = pd.to_numeric(data['value'], errors='coerce')
        data = data.dropna(subset=['date', 'value'])
        return data
    else:
        raise FileNotFoundError(f"File {filepath} does not exist.")

if __name__ == "__main__":
    os.makedirs('data/processed', exist_ok=True)

    gdp_data = process_data('gdp_data.csv')
    gdp_data.to_csv('data/processed/gdp_data_cleaned.csv', index=False)

    inflation_data = process_data('inflation_data.csv')
    inflation_data.to_csv('data/processed/inflation_data_cleaned.csv', index=False)

    unemployment_data = process_data('unemployment_data.csv')
    unemployment_data.to_csv('data/processed/unemployment_data_cleaned.csv', index=False)

    print("Data processing complete!")
