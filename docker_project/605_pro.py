import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report
import matplotlib.pyplot as plt
from sklearn.tree import plot_tree
from sklearn.metrics import confusion_matrix
import seaborn as sns
import numpy as np

# Load the dataset
# Re-load the dataset using semicolon as the delimiter
data = pd.read_csv('bank.csv', delimiter=';')

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report

# Splitting the dataset into training and testing sets
train_data, test_data = train_test_split(data, test_size=0.2, random_state=42)

# Separating the features and the target variable
X_train = train_data.drop('y', axis=1)
y_train = train_data['y']
X_test = test_data.drop('y', axis=1)
y_test = test_data['y']

# Training a Decision Tree model
model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)

# Making predictions
predictions = model.predict(X_test)

# Evaluating the model
accuracy = accuracy_score(y_test, predictions)
report = classification_report(y_test, predictions)

print('Accuracy is :',accuracy)

# Plotting the decision tree
plt.figure(figsize=(20,10))
plot_tree(model, filled=True, feature_names=X_train.columns, class_names=['no', 'yes'], max_depth=3)
plt.title('Decision Tree - Top Levels')
plt.savefig('Decision_Tree_Visualization.png')
plt.close()

# Plotting the confusion matrix
cm = confusion_matrix(y_test, predictions)
plt.figure(figsize=(8,6))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=['Predicted No', 'Predicted Yes'], yticklabels=['Actual No', 'Actual Yes'])
plt.title('Confusion Matrix')
plt.savefig('Confusion_Matrix.png')
plt.close()

# Plotting feature importance
importances = model.feature_importances_
indices = np.argsort(importances)[::-1]
plt.figure(figsize=(10,7))
sns.barplot(x=importances[indices], y=X_train.columns[indices])
plt.title('Feature Importance')
plt.xlabel('Relative Importance')
plt.savefig('Feature_Importance.png')
plt.close()