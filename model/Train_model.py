import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
import joblib, os

# Create synthetic dataset
np.random.seed(0)
n = 1000
data = pd.DataFrame({
    'amount': np.random.exponential(scale=200, size=n),
    'is_foreign': np.random.binomial(1, 0.05, size=n),
    'is_high_risk_country': np.random.binomial(1, 0.02, size=n),
    'num_recent_transactions': np.random.poisson(2, size=n)
})
# simple heuristic label for demo purposes (not real world)
data['is_fraud'] = ((data['amount'] > 800) & (data['is_foreign'] == 1)).astype(int)
# add some noise
data.loc[data.sample(frac=0.02, random_state=1).index, 'is_fraud'] = 1

X = data[['amount','is_foreign','is_high_risk_country','num_recent_transactions']]
y = data['is_fraud']

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)

os.makedirs(os.path.join(os.path.dirname(__file__), '..', 'models'), exist_ok=True)
model_path = os.path.normpath(os.path.join(os.path.dirname(__file__), '..', 'models', 'Fraud_model.pkl'))
joblib.dump(model, model_path)
print(f"Model trained and saved to {model_path}")