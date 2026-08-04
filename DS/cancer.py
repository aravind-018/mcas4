from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import numpy as np

bc=load_breast_cancer()
X=bc.data
y=bc.target
X_train,X_test,y_train,y_test=train_test_split(X, y, test_size=0.2,random_state=42)

model=GaussianNB()
model.fit(X_train,y_train)

y_pred=model.predict(X_test)

print("predicted:-",y_pred)
print("actual:-",y_test)

print("Accuracy:", accuracy_score(y_test, y_pred))

print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print(classification_report(y_test,y_pred))

sample=X_test[0].reshape(1,-1)
prediction=model.predict(sample)
print("predicted classes",bc.target_names[prediction])



