from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score

# Load the Iris dataset
data = load_iris()
features = data.data
labels = data.target

# Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2, random_state=42, stratify=labels)

# Initialize and train the Logistic Regression model
log_reg = LogisticRegression(max_iter=1000, solver='lbfgs')
log_reg.fit(X_train, y_train)

# Predict on test data
predictions = log_reg.predict(X_test)

# Calculate and display accuracy
acc = accuracy_score(y_test, predictions)
print(f"Model Accuracy: {acc:.2f}")