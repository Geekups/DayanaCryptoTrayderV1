import requests
import pandas as pd
import matplotlib.pyplot as plt

def get_dollar_price_in_iran():
    url = "https://api.exchangerate-api.com/v4/latest/USD" # Example API URL
    response = requests.get(url)
    data = response.json()
    iran_rate = data['rates']['IRR'] # Assuming 'IRR' is the currency code for Iranian Toman
    return iran_rate

def analyze_and_visualize(price):
    # For simplicity, we'll use the current date and time for the plot
    from datetime import datetime
    current_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    # Convert data to a pandas DataFrame
    df = pd.DataFrame([{'Date': current_date, 'Price': price}])
    
    # Basic visualization
    plt.plot(df['Date'], df['Price'])
    plt.title('Dollar Price in Iran Over Time')
    plt.xlabel('Date')
    plt.ylabel('Price (IRR)')
    plt.show()

def hello_world():
    dollar_price_in_iran = get_dollar_price_in_iran()
    print(f"The current dollar price in Iran is: {dollar_price_in_iran} IRR")
    analyze_and_visualize(dollar_price_in_iran)

hello_world()