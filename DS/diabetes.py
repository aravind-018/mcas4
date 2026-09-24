#write  a python program to predict diabetes using knn classification

from sklearn.datasets import load_diabetes
from sklearn.metrics import mean_squared_error,r2_score
from sklearn.model_selection import train_test_split
from sklearn import neighbors

diabetes=load_diabetes()
X=diabetes.data
y=diabetes.target


X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2)

classifier=neighbors.KNeighborsRegressor(n_neighbors=8)


classifier.fit(X_train,y_train)
y_pred=classifier.predict(X_test)
m=mean_squared_error(y_test,y_pred)
r2=r2_score(y_test,y_pred)

print("Mean Squared Error:", m)
print("R2 Score:", r2)



# print(diabetes.data.shape)
# print(diabetes.target.shape)
# print(diabetes.feature_names)
# print(diabetes.target)
print(diabetes.data[0])

#write a program to create a 2D array using numpy and print it
