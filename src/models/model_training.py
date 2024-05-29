import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

def load_data(filename):
    data = pd.read_csv(filename)
    return data

def train_model():
    data = load_data('../data/processed/gdp_data_cleaned.csv')
    X = data[['date']] 
    y = data['value']   

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = LinearRegression()
    model.fit(X_train, y_train)

    print(f'Model score: {model.score(X_test, y_test)}')

if __name__ == "__main__":
    train_model()
