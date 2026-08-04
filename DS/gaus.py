from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import numpy as np
# Load Iris dataset
iris = load_iris()

X = iris.data
y = iris.target

# Split dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2
)

# Create and train the model
model = GaussianNB()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Print predictions
print("Predicted:", y_pred)
print("Actual   :", y_test)

# Accuracy
print("Accuracy:", accuracy_score(y_test, y_pred))

# Confusion Matrix
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print(classification_report(y_test,y_pred))

sample1=np.array([[5.1,3.5,1.4,0.2]])
predic1=model.predict(sample1)
print(predic1)
print(iris.target_names[predic1])

sample2=np.array([[5.5,3.9,2.4,1.0]])
predic2=model.predict(sample2)
print(predic2)
print(iris.target_names[predic2])

sample3=np.array([[6.8,8.7,2.8,1.7]])
predic3=model.predict(sample3)
print(predic3)
print(iris.target_names[predic3])

