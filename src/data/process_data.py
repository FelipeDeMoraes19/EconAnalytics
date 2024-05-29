import pandas as pd
import os

def load_data(filename):
    filepath = os.path.join('data/raw', filename)
    if os.path.exists(filepath):
        data = pd.read_csv(filepath)
        print(f"Data loaded from {filepath}")
        return data
    else:
        print(f"File {filepath} does not exist.")
        return None

def clean_data(data):
    # Exemplo de limpeza de dados: remover linhas com valores ausentes
    cleaned_data = data.dropna()
    return cleaned_data

def save_cleaned_data(data, filename):
    filepath = os.path.join('data/processed', filename)
    data.to_csv(filepath, index=False)
    print(f"Data saved to {filepath}")

if __name__ == "__main__":
    # Carregar dados
    gdp_data = load_data('gdp_data.csv')
    inflation_data = load_data('inflation_data.csv')
    unemployment_data = load_data('unemployment_data.csv')

    if gdp_data is not None:
        # Limpar dados
        gdp_cleaned = clean_data(gdp_data)
        save_cleaned_data(gdp_cleaned, 'gdp_data_cleaned.csv')
    
    if inflation_data is not None:
        inflation_cleaned = clean_data(inflation_data)
        save_cleaned_data(inflation_cleaned, 'inflation_data_cleaned.csv')
    
    if unemployment_data is not None:
        unemployment_cleaned = clean_data(unemployment_data)
        save_cleaned_data(unemployment_cleaned, 'unemployment_data_cleaned.csv')

    print("Data processing complete!")
