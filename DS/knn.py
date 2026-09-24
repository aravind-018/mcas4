from sklearn.datasets import load_iris

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn import neighbors

load=load_iris
X=load.data
y=load.target

classif=neighbors.kNeig