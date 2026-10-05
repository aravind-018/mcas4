from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics
import matplotlib.pyplot as plt

# Load Iris dataset
iris = load_iris()

x = iris.data
y = iris.target

# Split dataset into training and testing data
x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.25
)

# Create KNN model with k = 5
model = KNeighborsClassifier(n_neighbors=5)

# Train the model
model.fit(x_train, y_train)

# Predict test data
y_prediction = model.predict(x_test)

# Calculate accuracy
print(
    "Accuracy =",
    metrics.accuracy_score(y_test, y_prediction)
)

# Test with a new sample
sample = [[2.2, 2.2, 2.2, 2.2]]

# Predict the class of the new sample
pred = model.predict(sample)[0]

print(
    "New Sample belongs to:",
    iris.target_names[pred]
)

# -------------------------------
# Predicted Classification Graph
# -------------------------------

plt.subplot(1, 2, 1)

plt.scatter(
    x_test[:, 0],
    x_test[:, 1],
    c=y_prediction
)

plt.title("Predicted classification")
plt.xlabel("Petal length")
plt.ylabel("Petal width")


# -------------------------------
# Actual Classification Graph
# -------------------------------

plt.subplot(1, 2, 2)

plt.scatter(
    x_test[:, 0],
    x_test[:, 1],
    c=y_test
)

plt.title("Actual classification")
plt.xlabel("Petal length")
plt.ylabel("Petal width")

plt.show()