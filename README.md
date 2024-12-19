# Video Game Sales Forecasting

## Table of Contents
1. [Project Overview](#project-overview)
2. [Business Problem](#business-problem)
3. [Data Analysis](#data-analysis)
4. [Our Approach](#our-approach)
5. [Model Testing](#model-testing)
6. [Tools We Used](#tools-we-used)
7. [What We Found](#what-we-found)
8. [Running the Project](#running-the-project)
9. [Wrapping Up](#wrapping-up)

## Project Overview
We built this project to predict video game sales each month for a local resale shop. Getting these predictions right helps the shop keep the right amount of games in stock - not too many, not too few.

## Business Problem
Game resellers face a tricky balance:
- Having too many games ties up money and shelf space
- Having too few means missing out on sales

Our team at Amdari needed to:
- Help the shop predict future sales
- Test different prediction methods
- Find patterns in past sales data

## Data Analysis
We started by:
- Loading sales history from our database
- Fixing dates and missing information
- Looking for sales patterns

What we noticed:
- Sales go up and down with seasons
- Different game systems sell differently
- Holiday sales make a big difference

## Our Approach
We cleaned up the data by:
- Making sure dates were in the right format
- Adding helpful information like months and seasons
- Marking holidays and sales events

## Model Testing
We tried three different ways to predict sales:

1. ARIMA Model
   - Prediction error (RMSE): 29,952
   - Good at catching short-term patterns

2. ETS Model
   - Prediction error (RMSE): 31,772
   - Handles seasonal changes well

3. Advanced SARIMA Model
   - Prediction error (RMSE): 30,456
   - Also looks at things like holidays and sales events

How different game systems performed (average sales):
- PC Games: 119,367
- Nintendo: 117,984
- Xbox: 108,868
- PlayStation: 102,825

Sales by quarter:
- January-March: 128,483
- April-June: 122,687
- July-September: 104,846
- October-December: 93,380

## Tools We Used
- Python for all our coding
- Pandas to handle data
- Matplotlib to make graphs
- Statsmodels for predictions
- Jupyter Notebook to put it all together

## What We Found
- ARIMA worked best for predictions
- Sales follow clear seasonal patterns
- Different game systems need different stock levels
- Special sales events help, but not as much as we thought

## Running the Project

1. Get the project files:
```bash
git clone https://github.com/your-repo-name/video-game-sales-forecast.git
cd video-game-sales-forecast
```

2. Install what you need:
```bash
pip install -r requirements.txt
```

3. Open and run the notebook:
```bash
jupyter notebook "Forecasting Video Games Inventory Sales.ipynb"
```

## Wrapping Up
We found that we can predict game sales pretty well using ARIMA. The shop should:
- Stock up before busy seasons
- Keep different amounts for different game systems
- Plan ahead for quarterly changes

Thanks to everyone at Amdari who helped with this project!






