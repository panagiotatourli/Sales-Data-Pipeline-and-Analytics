import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score

# --- 1. DATA ACQUISITION & PREPARATION ---
# Loading the cleaned dataset generated from the SQL ETL process
file_path = r"C:\Users\tourl\OneDrive\Υπολογιστής\2026 Portfolio Projects\1st Project\Sales Dataset\clean_sales_dataset.csv"
df = pd.read_csv(file_path)

# Standardizing column names for consistency
df.columns = df.columns.str.strip().str.lower()

# Applying One-Hot Encoding to categorical variables (productline)
df_encoded = pd.get_dummies(df, columns=['productline'], drop_first=True)

# Defining features and target variable for the regression task
features = ['quantityordered', 'priceeach', 'month_id', 'msrp']
X = pd.concat([df_encoded[features], df_encoded.filter(like='productline_')], axis=1)
y = df_encoded['sales']

# Splitting the data into training (80%) and testing (20%) sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# --- 2. MODEL EVALUATION ---
# Initializing and training Linear Regression
model_lr = LinearRegression()
model_lr.fit(X_train, y_train)
preds_lr = model_lr.predict(X_test)

# Initializing and training Random Forest for comparison
model_rf = RandomForestRegressor(n_estimators=100, random_state=42)
model_rf.fit(X_train, y_train)
preds_rf = model_rf.predict(X_test)

# Calculating R2 scores to measure predictive accuracy
score_lr = r2_score(y_test, preds_lr)
score_rf = r2_score(y_test, preds_rf)

# --- 3. PERFORMANCE VISUALIZATION ---
# Using seaborn theme for professional aesthetics
sns.set_theme(style="whitegrid")
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

# Plot 1: Linear Regression Actual vs Predicted
sns.scatterplot(ax=ax1, x=y_test, y=preds_lr, color='royalblue', alpha=0.6)
ax1.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], '--r', lw=2)
ax1.set_title(f'Linear Regression Analysis\nR2 Score: {score_lr:.2f}', fontsize=12)
ax1.set_xlabel('Actual Sales')
ax1.set_ylabel('Predicted Sales')

# Plot 2: Random Forest Actual vs Predicted
sns.scatterplot(ax=ax2, x=y_test, y=preds_rf, color='forestgreen', alpha=0.6)
ax2.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], '--r', lw=2)
ax2.set_title(f'Random Forest Analysis\nR2 Score: {score_rf:.2f}', fontsize=12)
ax2.set_xlabel('Actual Sales')
ax2.set_ylabel('Predicted Sales')

plt.tight_layout()

# Exporting results for GitHub Portfolio documentation
plt.savefig('model_performance_report.png', dpi=300)
print("Visualization complete. 'model_performance_report.png' has been saved.")
plt.show()