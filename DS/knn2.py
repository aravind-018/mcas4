from sklearn.datasets import load_iris

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

from sklearn import neighbors
load=load_iris()
X=load.data
y=load.target

classif=neighbors.KNeighborsClassifier(n_neighbors=3)
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)

classif.fit(X_train,y_train)

y_pred=classif.predict(X_test)
accuracy=accuracy_score(y_test,y_pred)


print("Accuracy:", accuracy)

sample=[[.2,.5,7,9]]
prediction=classif.predict(sample)
print("predicted classes",load.target_names[prediction])



#write  a python program to predict diabetes using knn classification