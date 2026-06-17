#Importing the required modules from scikit-learn as per workflow blueprint

#To load the iris dataset.
from sklearn.datasets import load_iris
#To split the dataset into training and testing sets. 
from sklearn.model_selection import train_test_split 
#To perform feature scaling on the dataset (The Gatekeeper).
from sklearn.preprocessing import StandardScaler
#To create a KNN classifier model.
from sklearn.neighbors import KNeighborsClassifier
#For output validation and diagnosis.
from sklearn.metrics import confusion_matrix , f1_score 

#phase 1: Load the dataset
print ("Loading the iris benchmark dataset.")
iris_data = load_iris()
X = iris_data.data
y = iris_data.target

print ("Applying the Gatekeeper Rule : Feature Scaling via StandardScaler.")
# Initializing the scaler to make Mean = 0 and Variance = 1 to remove raw data bias.
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
print ("Feature scaling completed.")
#phase 2 : process phase 
print ("Maintaining Structural Integrity : Splitting data")

#Shuffling and splitting the data to remove order bias and ensure a fair testing phase.  
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42 , stratify=y )
print ("Data splitting completed.")

print ("Tuning the Engine : Initializing and Training the KNN Classifier Model.")
# Initializing the KNN with k=5.
knn_model = KNeighborsClassifier(n_neighbors=5)

# Training the model.
knn_model.fit(X_train, y_train)
print ("Model training completed.")

# Making predictions on the test set.
y_pred = knn_model.predict(X_test)
print ("Predictions completed.")

#phase 3 : output phase
print ("\n Output Validation and system diagnosis :")
print("=" * 50)

#Calculating the F1 score to evaluate absolute precision and model quality.
macro_f1 = f1_score(y_test, y_pred, average='macro')
print(f"Absolute System Precision (Macro F1-score): {macro_f1 * 100:.2f}%")

#Generate the confusion matrix diagnostic tool to inspect alignment and misclassification.
cof_matrix = confusion_matrix(y_test, y_pred)
print("\n Diagnostic Tool - Confusion Matrix:")
print(cof_matrix)
print("\n System Diagnosis: ")
print ("- Diagonal values represent absolute accurate classifications.")
print("- Values outside the diagonal indicate misclassifications or cross-class confusion.")
print("=" * 50)
print("Project 2 Pipeline Executed Successfully! Ready for Deployment.")
