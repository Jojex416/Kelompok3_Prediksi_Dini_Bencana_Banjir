import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle

# 1. Load dataset
df = pd.read_csv("finalfinal.csv")

# 2. Tentukan fitur & target
X = df[['lat', 'lon', 'precip', 'pop']]  # fitur
y = df['class']  # target

# 3. Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. Train model baru
model = RandomForestClassifier()
model.fit(X_train, y_train)

# 5. Simpan model kompatibel
with open("model.pickle", "wb") as f:
    pickle.dump(model, f)

print("Model baru berhasil dibuat!")
