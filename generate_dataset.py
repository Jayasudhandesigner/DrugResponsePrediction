import pandas as pd
import numpy as np

np.random.seed(42)
n_samples = 1000
data = {
    'patient_id': range(1, n_samples + 1),
    'age': np.random.randint(18, 81, n_samples),
    'genetic_marker': np.random.uniform(0, 1, n_samples),
    'blood_level': np.random.uniform(0, 100, n_samples),
    'response': np.where((np.random.uniform(0, 1, n_samples) > 0.5) & 
                         (np.random.uniform(0, 1, n_samples) > 0.3), 1, 0)  
}
df = pd.DataFrame(data)
df.to_csv('biomarker_response_data.csv', index=False)
print("Synthetic dataset saved as 'biomarker_response_data.csv'")
print(df.head())
