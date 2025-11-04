# Importing the necessary libraries
import numpy as np
from sklearn.datasets import load_breast_cancer
from  sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import f1_score, classification_report, accuracy_score
# Loading the breast cancer dataset and storing it in a variable named cancer
cancer= load_breast_cancer()

#Separating the features(X) and target(Y) variables from the dataset
X= cancer.data
Y= cancer.target
#Printing to take a peek on what the features and target variable contain
print("Features are:")
print(X)

print("Target variables are:")
print(Y)

#Splitting the data into train and test splits by using the train_test_split() function from sklearn
# we will have X_train,X_test and Y_train and Y_split and our test data will be 20% and the train data will be 80%
X_train, X_test, Y_train, Y_test= train_test_split(X,Y, test_size=0.2, random_state=42)

#Initializing the random forest classifier
rf_classifier=RandomForestClassifier(n_estimators=100, random_state=42)

# Training and fitting the model to learn patterns from the training data
rf_classifier.fit( X_train, Y_train)
print("Completed training the model successfully")

# Making predictions on the test data and storing it in a variable named Y_pred
Y_pred= rf_classifier.predict(X_test)

#Calculating the f1 score for the positive class(1= Benign)
f1_binary= f1_score(Y_test,Y_pred,average='binary' )

#Calculating tthe weighted F1 score
f1_weighted= f1_score(Y_test,Y_pred, average='weighted')
#Printing the detailed classification report for comparison
print(classification_report(Y_test,Y_pred, target_names=cancer.target_names))
