# 🚗 Vehicle Fuel Efficiency Prediction (Auto MPG)
### Technical Work Sample: Multiple Linear Regression & Predictive Modeling

## 📌 Project Overview
This project involves building a **Multiple Linear Regression** model to predict vehicle fuel efficiency (Miles Per Gallon). By analyzing technical specifications—including displacement, horsepower, weight, and acceleration—this analysis identifies the variables that most significantly impact fuel economy. This project serves as a practical demonstration of using **structured data** to generate automated, data-driven insights.

---

## 🛠️ Technical Stack
* **Language:** Python
* **Libraries:** Pandas, NumPy, Scikit-Learn, Matplotlib, Seaborn
* **Tools:** Google Colab, GitHub

---

## 📊 Methodology

### 1. Data Acquisition & Exploration
* **Exploratory Data Analysis (EDA):** Performed initial inspections using `.info()` and `.describe()` to understand data distributions and types.
* **Correlation Analysis:** Generated correlation matrices and scatter plots to identify relationships between vehicle weight, horsepower, and MPG.

### 2. Data Cleaning & Preprocessing
* **Missing Value Management:** Identified and handled null values within the 'horsepower' column to ensure model stability.
* **Feature Selection:** Selected independent variables (X) based on statistical significance to build a refined predictive pipeline.

### 3. Model Building & Evaluation
* **Implementation:** Developed a Multiple Linear Regression model utilizing a **train-test split (80/20)** to validate performance on unseen data.
* **Statistical Inference:** Interpreted model coefficients to quantify how specific specifications (e.g., weight) affect the target variable (MPG).

