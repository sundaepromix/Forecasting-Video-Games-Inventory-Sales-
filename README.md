# Video Game Inventory Sales Forecasting

## **Table of Contents**
1. [Project Overview](#project-overview)
2. [Business Problem](#business-problem)
3. [Data Preparation and Exploration](#data-preparation-and-exploration)
4. [Methodology](#methodology)
5. [Technologies Used](#technologies-used)
6. [Results and Insights](#results-and-insights)
7. [How to Run the Project](#how-to-run-the-project)
8. [Conclusion](#conclusion)
9. [Acknowledgments](#acknowledgments)


## 1. Project Overview

This project forecasts monthly video game sales for a local resale company. Accurate forecasting helps optimize inventory management, ensuring that supply meets customer demand without overstocking or understocking.

## 2. Business Problem

Businesses that resell video games need to balance inventory with demand. Poor inventory planning can lead to:

#### Overestimation: Excess inventory, increased costs, and wasted resources.
#### Underestimation: Lost sales opportunities and dissatisfied customers.
#### Objective
The Data Science Team at Amdari has been tasked to:
Provide actionable insights to synchronize inventory with expected demand.
Evaluate the performance of predictive models.

## 3. Data Preparation and Exploration
### 3.1 Data Loading
Loaded historical sales data using Pandas.
### 3.2 Data Cleaning
Converted date columns to datetime format.
Checked for missing values and outliers.
Ensured the dataset was suitable for time series analysis.
### 3.3 Exploratory Data Analysis (EDA)
Analyzed trends, seasonality, and patterns in the data.
Visualized sales trends over time using Matplotlib and Seaborn.

### Key Observations:

Sales exhibit seasonal patterns, likely due to holidays or new game releases.
There are occasional spikes in sales, indicating high-demand periods.

## 4. Methodology
The following steps were performed to build the forecasting model:

#### Data Preprocessing:

Prepared the data to meet time series requirements.
Feature Engineering:

Extracted features such as month, year, and seasonality trends.

## 5. Technologies Used
Python
Jupyter Notebook
Pandas: Data manipulation and cleaning.
Matplotlib and Seaborn: Data visualization.
Statsmodels: Time series analysis and modeling.
Scikit-learn: Evaluation and validation of models.

## 6. Results and Insights

Sales showed significant peaks during specific months, likely related to customer behavior around holidays and promotions.

#### Visualizations:
The notebook includes detailed plots such as:

Sales trends over time.

## 7. How to Run the Project
Follow these steps to run the project on your local system:

Clone the Repository
git clone https://github.com/your-repo-name/video-game-sales-forecast.git

cd video-game-sales-forecast

Install Required Libraries

Run the Jupyter Notebook
#### Open the notebook in Jupyter and execute the cells:

jupyter notebook "Forecasting Video Games Inventory Sales.ipynb"
View Results
The notebook will generate visualizations and predictions for video game sales.

## 8. Conclusion
This project highlights the value of time series forecasting in inventory management. By accurately predicting future sales, businesses can:

Minimize excess inventory costs.
Ensure products are available when customers need them.
Make data-driven decisions to improve overall performance.

## 9. Acknowledgments
Special thanks to the Data Science Team at Amdari for their collaboration and contributions to this project.













