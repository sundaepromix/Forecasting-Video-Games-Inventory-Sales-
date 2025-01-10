# Video Game Sales Forecasting System

## 📊 Project Overview
An advanced time series forecasting system analyzing gaming sales from 2002-2023. The system provides sales predictions across major gaming platforms with a 4-month forecasting window.

**Supported Platforms:**
- Nintendo
- PC
- PlayStation
- Xbox

## 🔧 Model Architecture 

### ARIMA Configuration
```python
model = ARIMA(train['Monthly Sales'], 
             order=(0, 1, 1))  # (p,d,q)
```

### SARIMAX Configuration
```python
model = SARIMAX(train['Monthly Sales'], 
               order=(1, 0, 1), 
               seasonal_order=(0, 1, 1, 12))
```

### ETS Configuration
```python
model = ExponentialSmoothing(train, 
                           trend="additive", 
                           seasonal="additive", 
                           seasonal_periods=12, 
                           damped=True)
```

## 📈 Performance Metrics

| Model   | RMSE    | Description                |
|---------|---------|----------------------------|
| ARIMA   | [VALUE] | Basic trend analysis       |
| SARIMAX | [VALUE] | Better for seasonal patterns|
| ETS     | [VALUE] | Strong with long-term trends|

## 🗄️ Dataset Features
- Category (Game Genre)
- Monthly Sales
- Platform Distribution
- Holiday Flags
- Promotional Events
- Quarterly Metrics

## 🛠️ Quick Start

```bash
# Clone repository
git clone https://github.com/sundaepromix/Forecasting-Video-Games-Inventory-Sales-

# Install requirements
pip install pandas numpy statsmodels sklearn matplotlib

# Run forecasting
python forecast.py
```

## 📝 Basic Usage

### ARIMA Model
```python
# Data preparation
train = data[:-12]
test = data[-12:]

# Model fitting
model = ARIMA(train['Monthly Sales'], order=(0, 1, 1))
results = model.fit()

# Forecasting
forecast = results.forecast(steps=4)
```

### SARIMAX Model
```python
# Model fitting
model = SARIMAX(train['Monthly Sales'], 
               order=(1, 0, 1), 
               seasonal_order=(0, 1, 1, 12))
results = model.fit()

# Forecasting
forecast = results.get_forecast(steps=4)
```

### ETS Model
```python
# Model fitting
model = ExponentialSmoothing(train, 
                           trend="additive", 
                           seasonal="additive", 
                           seasonal_periods=12)
results = model.fit()

# Forecasting
forecast = results.forecast(steps=4)
```

## 🔄 Data Processing Pipeline
1. Date Formatting
2. Missing Value Treatment
3. Outlier Detection
4. Feature Engineering

## 📊 Validation Framework
- 12-month test period
- Cross-validation implementation
- Error metrics calculation (RMSE, MAPE, MAE)
- Model comparison and selection

## 🚀 Future Enhancements
- External factor integration
- Deep learning implementation
- Automated retraining pipeline
- Hybrid model development

## 👥 Contributing
1. Fork repository
2. Create feature branch
3. Submit pull request

## 📚 Dependencies
- pandas
- numpy
- statsmodels
- scikit-learn
- matplotlib

*Last updated: January 2025*
