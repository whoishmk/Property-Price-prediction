import pandas as pd
import matplotlib.pyplot as plt

# Given output string
data_str = """2025: ₹1.2Cr
2030: ₹1.8Cr
2035: ₹2.5Cr"""

# Preprocess the string to extract year and price values
lines = data_str.strip().splitlines()
years = []
prices = []

for line in lines:
    # Split the line into year and price parts
    year_str, price_str = line.split(":")
    year = int(year_str.strip())
    # Remove currency symbol and 'Cr', then convert to float
    price = float(price_str.replace("₹", "").replace("Cr", "").strip())
    years.append(year)
    prices.append(price)

# Create a DataFrame
df = pd.DataFrame({
    "Year": years,
    "Price": prices
})
print("DataFrame:")
print(df)

# Plot the line graph
plt.figure(figsize=(8, 5))
plt.plot(df["Year"], df["Price"], marker='o', linestyle='-')
plt.title("Price Trend Over Years")
plt.xlabel("Year")
plt.ylabel("Price (Cr)")
plt.grid(True)
plt.show()
