
# Supply Chain Demand Forecasting

## Overview

This project implements a time-series-based forecasting model for predicting weekly product demand across different distribution centers. It simulates a basic but production-relevant supply chain forecasting pipeline that uses historical order data to estimate future demand using SARIMA (Seasonal AutoRegressive Integrated Moving Average).

The code, data, and outputs here are structured to mimic a simplified yet realistic scenario often encountered by supply chain data engineers and analysts working on logistics and inventory planning.

---

## Problem Statement

In a typical supply chain network, accurate demand forecasting is crucial for:

- Optimizing inventory levels
- Reducing holding and stockout costs
- Improving supplier coordination and logistics

Given historical demand for various products across multiple distribution centers (DCs), our goal is to build a forecasting solution that can:

- Ingest and preprocess time-series order data
- Train a statistical forecasting model
- Predict weekly demand for the next `n` weeks
- Visualize actual vs predicted demand

---

## Project Structure

```
supply_chain_forecasting/
│
├── forecast_demand.py          # Main script for demand forecasting
├── sample_orders.csv           # Synthetic order data for training
├── README.md                   # Project overview and explanation
```

---

## Data Description

`samples_orders.csv` contains historical weekly demand in the following format:

| week_start | dc_id | product_id | demand |
|------------|-------|------------|--------|
| 2023-01-01 | DC_001| PROD_A     | 120    |
| 2023-01-08 | DC_001| PROD_A     | 145    |

- `week_start`: Start date of the week
- `dc_id`: Distribution Center identifier
- `product_id`: Product identifier
- `demand`: Units ordered in that week

This data mimics real-world ERP/OMS exports.

---

## Forecasting Approach

We use **SARIMA** (Seasonal ARIMA), which is suitable for univariate time series data exhibiting trends and seasonality.

### Steps:

1. **Data Preprocessing**:
   - Load CSV data into pandas DataFrame
   - Convert `week_start` to datetime
   - Group by `dc_id` and `product_id` to build separate time series

2. **Modeling**:
   - For each unique (dc_id, product_id) combination:
     - Sort by time
     - Fit a SARIMA model using auto-order selection
     - Forecast the next 8 weeks of demand

3. **Output**:
   - Plots showing actual vs forecasted demand
   - Printed numeric forecast for each DC-product pair

---

## Dependencies

- pandas
- numpy
- matplotlib
- statsmodels

You can install them via:

```bash
pip install pandas numpy matplotlib statsmodels
```

---

## How to Run

```bash
python forecast_demand.py
```

This will:

- Read the sample data
- Forecast next 8 weeks of demand for each DC-product pair
- Save demand forecast plots in the same directory

---

## Example Output

For `DC_001 - PROD_A`:

- Actual demand: 110, 120, 135...
- Forecasted: 160, 165, 158...

![sample plot](./forecast_DC_001_PROD_A.png)

---

## Future Improvements

- Integrate ML-based forecasting models (XGBoost, Prophet, LSTM)
- Incorporate external regressors like promotions, holidays
- Deploy using AWS Lambda + S3 + QuickSight for BI reporting
- Add CI/CD + dbt for transformation orchestration

---

## Author

Kiran Ranganalli  
Data Engineer | Supply Chain + Cloud + ML Pipelines  
