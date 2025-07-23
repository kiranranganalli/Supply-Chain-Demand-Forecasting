import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

# Load data
df = pd.read_csv("sample_orders.csv", parse_dates=["order_date"])
df = df.groupby("order_date").agg({ "quantity": "sum" }).reset_index()

# Feature engineering
df["dayofweek"] = df["order_date"].dt.dayofweek
df["month"] = df["order_date"].dt.month
df["year"] = df["order_date"].dt.year

# Lag features
df["lag_1"] = df["quantity"].shift(1)
df["lag_7"] = df["quantity"].shift(7)
df.dropna(inplace=True)

# Model training
X = df[["dayofweek", "month", "year", "lag_1", "lag_7"]]
y = df["quantity"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)

model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Prediction
y_pred = model.predict(X_test)
print("RMSE:", np.sqrt(mean_squared_error(y_test, y_pred)))

# Plotting
plt.figure(figsize=(10,5))
plt.plot(df["order_date"].iloc[y_test.index], y_test, label="Actual")
plt.plot(df["order_date"].iloc[y_test.index], y_pred, label="Predicted")
plt.legend()
plt.title("Supply Chain Demand Forecasting")
plt.xlabel("Date")
plt.ylabel("Quantity")
plt.tight_layout()
plt.savefig("forecast_plot.png")
plt.show()
