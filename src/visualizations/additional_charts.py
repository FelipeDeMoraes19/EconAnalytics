import pandas as pd
import matplotlib.pyplot as plt

def plot_additional_charts():
    data = pd.read_csv('../data/processed/gdp_data_cleaned.csv')

    plt.figure(figsize=(10, 5))
    plt.plot(data['date'], data['value'])
    plt.title('GDP Over Time')
    plt.xlabel('Date')
    plt.ylabel('GDP')
    plt.show()

if __name__ == "__main__":
    plot_additional_charts()
