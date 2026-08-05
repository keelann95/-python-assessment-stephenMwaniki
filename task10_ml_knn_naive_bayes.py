

import sklearn
print("a. scikit-learn version:", sklearn.__version__)

import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
)

# b. Load dataset with Pandas, display first 5 rows
iris = load_iris()
iris_df = pd.DataFrame(iris.data, columns=iris.feature_names)
iris_df["target"] = iris.target
print("\nb. First 5 rows of the Iris dataset:")
print(iris_df.head())

# c. Prepare features (X) and labels (y); split into train/test sets
X = iris_df.drop(columns=["target"])
y = iris_df["target"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
print("\nc. Training samples:", len(X_train), "| Testing samples:", len(X_test))

# d. KNN: instantiate, fit, predict
knn_model = KNeighborsClassifier(n_neighbors=3)
knn_model.fit(X_train, y_train)
knn_predictions = knn_model.predict(X_test)

# e. KNN: evaluate accuracy and classification report
knn_accuracy = accuracy_score(y_test, knn_predictions)
print("\nd/e. KNN Results:")
print("   Accuracy:", knn_accuracy)
print("   Classification report:")
print(classification_report(y_test, knn_predictions))


# g. Naive Bayes: instantiate, fit, predict
nb_model = GaussianNB()
nb_model.fit(X_train, y_train)
nb_predictions = nb_model.predict(X_test)

# h. Naive Bayes: evaluate accuracy and confusion matrix
nb_accuracy = accuracy_score(y_test, nb_predictions)
print("\ng/h. Naive Bayes Results:")
print("   Accuracy:", nb_accuracy)
print("   Confusion matrix:")
print(confusion_matrix(y_test, nb_predictions))
