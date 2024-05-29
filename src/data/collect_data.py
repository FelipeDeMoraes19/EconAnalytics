import os
import pandas as pd
import requests

def get_world_bank_data(indicator, country, start_year, end_year):
    url = f"http://api.worldbank.org/v2/country/{country}/indicator/{indicator}?date={start_year}:{end_year}&format=json"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if len(data) > 1:
            df = pd.json_normalize(data[1])
            return df
        else:
            raise ValueError("No data found for the specified parameters")
    else:
        raise ConnectionError(f"Failed to fetch data: {response.status_code}")

def save_data_to_csv(data, filename):
    filepath = os.path.abspath(filename)
    data.to_csv(filepath, index=False)
    print(f"Data saved to {filepath}")

if __name__ == "__main__":
    os.makedirs('data/raw', exist_ok=True)

    indicators = {
        'GDP': 'NY.GDP.MKTP.CD',
        'Inflation': 'FP.CPI.TOTL',
        'Unemployment': 'SL.UEM.TOTL.ZS'
    }

    country = 'BRA'
    start_year = 2000
    end_year = 2023

    try:
        gdp_data = get_world_bank_data(indicators['GDP'], country, start_year, end_year)
        save_data_to_csv(gdp_data, 'data/raw/gdp_data.csv')
        
        inflation_data = get_world_bank_data(indicators['Inflation'], country, start_year, end_year)
        save_data_to_csv(inflation_data, 'data/raw/inflation_data.csv')
        
        unemployment_data = get_world_bank_data(indicators['Unemployment'], country, start_year, end_year)
        save_data_to_csv(unemployment_data, 'data/raw/unemployment_data.csv')
        
        print("Data collection complete!")
    except ValueError as e:
        print(f"Error: {e}")
    except ConnectionError as e:
        print(f"Error: {e}")
