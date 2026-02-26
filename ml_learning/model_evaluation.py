"""
Model Evaluation: Train/Val/Test Split, Confusion Matrix, Precision, Recall
"""
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, precision_score, recall_score, f1_score, classification_report

# Load data
iris = load_iris()
X = iris.data
y = iris.target

print("=" * 60)
print("Model Evaluation Pipeline")
print("=" * 60)
print()

# Step 1: Split into train (60%) and temp (40%)
X_train, X_temp, y_train, y_temp = train_test_split(
    X, y, test_size=0.4, random_state=42
)

# Step 2: Split temp into val (20%) and test (20%)
X_val, X_test, y_val, y_test = train_test_split(
    X_temp, y_temp, test_size=0.5, random_state=42
)

print(f"Train set: {X_train.shape[0]} samples")
print(f"Validation set: {X_val.shape[0]} samples")
print(f"Test set: {X_test.shape[0]} samples")
print()

# Train model
print("Training logistic regression...")
model = LogisticRegression(max_iter=200, random_state=42)
model.fit(X_train, y_train)
print("✓ Training complete")
print()

# Validate
print("=" * 60)
print("VALIDATION METRICS")
print("=" * 60)
y_val_pred = model.predict(X_val)
print(f"Accuracy: {model.score(X_val, y_val):.4f}")
print(f"Precision (macro): {precision_score(y_val, y_val_pred, average='macro'):.4f}")
print(f"Recall (macro): {recall_score(y_val, y_val_pred, average='macro'):.4f}")
print(f"F1 Score (macro): {f1_score(y_val, y_val_pred, average='macro'):.4f}")
print()

# Test
print("=" * 60)
print("TEST METRICS (Final Evaluation)")
print("=" * 60)
y_test_pred = model.predict(X_test)
print(f"Accuracy: {model.score(X_test, y_test):.4f}")
print(f"Precision (macro): {precision_score(y_test, y_test_pred, average='macro'):.4f}")
print(f"Recall (macro): {recall_score(y_test, y_test_pred, average='macro'):.4f}")
print(f"F1 Score (macro): {f1_score(y_test, y_test_pred, average='macro'):.4f}")
print()

# Confusion matrix
print("=" * 60)
print("CONFUSION MATRIX (Test Set)")
print("=" * 60)
cm = confusion_matrix(y_test, y_test_pred)
print(cm)
print()
print("(Rows: true labels, Columns: predicted labels)")
print()

# Full classification report
print("=" * 60)
print("DETAILED CLASSIFICATION REPORT")
print("=" * 60)
print(classification_report(y_test, y_test_pred, target_names=iris.target_names))
