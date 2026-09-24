from sklearn import datasets
from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

iris = datasets.load_iris()

X, y = iris.data, iris.target

classifier = tree.DecisionTreeClassifier()

x_train, x_test, y_train, y_test = train_test_split(
    X, y, train_size=0.7
)

classifier.fit(x_train, y_train)

tree.plot_tree(classifier)
plt.show()

result = classifier.predict(x_test)

accuracy = accuracy_score(y_test, result) * 100

print(f"Accuracy is {accuracy}")

features = [[int(i) for i in input(
    f"Enter {iris.feature_names}: "
).split()]]

result = classifier.predict(features)

print(iris['target_names'][result])