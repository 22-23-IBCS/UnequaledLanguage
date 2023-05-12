import pandas as pd
from sklearn.neighbors import KNeighborsClassifier

# Load the training data
train_data = pd.read_csv('CrocAlliTraining.csv')

# Drop the "animal" column from the training data
X_train = train_data.drop('animal', axis=1)
y_train = train_data['animal']

# Fit the classifier to the training data
clf = KNeighborsClassifier(n_neighbors=3)
clf.fit(X_train, y_train)


# Load the new data
new_data = pd.read_csv('CrocAlliTest1.csv')

# Separate the features from the target variable
X_new = new_data[['length', 'mass']]

# Make predictions on the new data
pred_animal = clf.predict(X_new)
probs = clf.predict_proba(X_new)

# Print the predicted species and corresponding probabilities
for i, animal in enumerate(pred_animal):
    print(f"Sample {i+1}: {animal}, Probabilities: {probs[i]}")


print(type(pred_animal))
print(type(probs))
