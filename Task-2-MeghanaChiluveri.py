# STEP 1: IMPORT LIBRARIES
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

# STEP 2: LOAD DATA
iris = load_iris()

X = iris.data
y = iris.target

print("       PROJECT 2: DATA CLASSIFICATION USING AI")

print("\n📊 DATASET OVERVIEW:")
print(f"   Total Samples   : {X.shape[0]}")
print(f"   Total Features  : {X.shape[1]}")
print(f"   Feature Names   : {iris.feature_names}")
print(f"   Classes         : {iris.target_names}")

print("\n🌸 First 5 rows of data:")
for i in range(5):
    print(f"   {X[i]} → {iris.target_names[y[i]]}")

# STEP 3: FEATURE SCALING
scaler = StandardScaler()

# STEP 4: TRAIN-TEST SPLIT
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    shuffle=True
)

print(f"\n✂️ DATA SPLIT:")
print(f"   Training samples : {len(X_train)} (80%)")
print(f"   Testing samples  : {len(X_test)} (20%)")

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

print("\n✅ Feature scaling applied (StandardScaler)")

# STEP 5: BUILD & TRAIN MODEL
model = KNeighborsClassifier(n_neighbors=5)
model.fit(X_train, y_train)

print("\n🤖 MODEL TRAINED: KNN with K=5")

# STEP 6: MAKE PREDICTIONS
predictions = model.predict(X_test)

# STEP 7: EVALUATE MODEL
accuracy = accuracy_score(y_test, predictions)

print("\n" + "=" * 55)
print("               OUTPUT: MODEL EVALUATION")
print("=" * 55)

print(f"\n🎯 Accuracy Score: {accuracy * 100:.2f}%")

print("\n📋 CONFUSION MATRIX:")
cm = confusion_matrix(y_test, predictions)
print(f"   Classes: {iris.target_names}")
print(cm)
print("   (Rows = Actual, Columns = Predicted)")

print("\n📊 FULL CLASSIFICATION REPORT:")
print(
    classification_report(
        y_test,
        predictions,
        target_names=iris.target_names
    )
)

# STEP 8: PREDICT A NEW FLOWER
print("=" * 55)
print("         BONUS: PREDICT A NEW FLOWER")
print("=" * 55)

new_flower = [[5.1, 3.5, 1.4, 0.2]]

new_flower_scaled = scaler.transform(new_flower)

result = model.predict(new_flower_scaled)
flower_name = iris.target_names[result[0]]

print(f"\n   New flower measurements: {new_flower[0]}")
print(f"   Predicted species      : 🌸 {flower_name.upper()}")