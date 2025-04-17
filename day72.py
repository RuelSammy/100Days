import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# Simulated dataset: House size (sqft) vs Price (in $1000s)
data = {
    'SquareFeet': [500, 750, 1000, 1250, 1500, 1750, 2000],
    'Price': [150, 200, 250, 300, 350, 400, 450]
}

df = pd.DataFrame(data)

X = df[['SquareFeet']]  # Features (2D array)
y = df['Price']         # Target (1D array)

# Split into training and test sets (70/30 split)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("Mean Squared Error:", mean_squared_error(y_test, y_pred))
print("R² Score:", r2_score(y_test, y_pred))

# Predict price for a 1600 sqft house
predicted_price = model.predict([[1600]])
print("Predicted price for 1600 sqft:", predicted_price[0])

plt.scatter(X, y, color='blue', label='Actual Data')
plt.plot(X, model.predict(X), color='red', label='Regression Line')
plt.xlabel('Square Feet')
plt.ylabel('Price ($1000s)')
plt.legend()
plt.title('Linear Regression Example')
plt.show()
