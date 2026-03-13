import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score

# --- 1. PREPARE DATA ---
df = pd.read_csv(r"C:\Users\tourl\OneDrive\Υπολογιστής\2026 Portfolio Projects\1st Project\Sales Dataset\clean_sales_dataset.csv")
df.columns = df.columns.str.strip().str.lower()

# Convert text categories to numbers (One-Hot Encoding)
df_encoded = pd.get_dummies(df, columns=['productline'], drop_first=True)

# Select simple features for the models
features = ['quantityordered', 'priceeach', 'month_id', 'msrp']
X = pd.concat([df_encoded[features], df_encoded.filter(like='productline_')], axis=1)
y = df_encoded['sales']

# Split data: 80% to learn, 20% to test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# --- 2. TRAIN MODELS ---
# Simple model (Linear Regression)
model_lr = LinearRegression()
model_lr.fit(X_train, y_train)

# Advanced model (Random Forest)
model_rf = RandomForestRegressor(n_estimators=100, random_state=42)
model_rf.fit(X_train, y_train)

# --- 3. COMPARE & RESULTS ---
# See how well they did
score_lr = r2_score(y_test, model_lr.predict(X_test))
score_rf = r2_score(y_test, model_rf.predict(X_test))

print(f"Linear Regression Score: {score_lr:.2f}")
print(f"Random Forest Score:     {score_rf:.2f}")

# --- 4. Predictions for all the TEST SET ---

# Request from models to predict all the X_test (approximately 560 lines)
all_preds_lr = model_lr.predict(X_test)
all_preds_rf = model_rf.predict(X_test)

# Table creation for comparison
comparison_df = pd.DataFrame({
    'Actual_Sales': y_test.values,
    'LR_Predicted': all_preds_lr,
    'RF_Predicted': all_preds_rf
})

# First 10 lines for comparison
print("\n--- Συνολική Σύγκριση (Πρώτες 10 γραμμές) ---")
print(comparison_df.head(10))


