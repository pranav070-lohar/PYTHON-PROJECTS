import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import seaborn as sns
import matplotlib.pyplot as plt

# Step 1: Load the dataset
# For demonstration, we will create a synthetic dataset for spam detection
data = {
    'text': [
        'Free money now', 'Call me now', 'Limited time offer', 'Hello, how are you?',
        'Important information regarding your account', 'You won a lottery', 'Meeting at 10 AM',
        'Your invoice is attached', 'Congratulations, you are selected', 'This is not spam'
    ],
    'label': [1, 1, 1, 0, 1, 1, 0, 0, 1, 0]  # 1: spam, 0: not spam
}

df = pd.DataFrame(data)

# Step 2: Data Preprocessing
# Convert text to numerical features (for simplicity, we will use a basic approach)
df['text_length'] = df['text'].apply(len)
X = df[['text_length']]
y = df['label']

# Step 3: Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 4: Feature Scaling
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Step 5: Train the model
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Step 6: Make predictions
y_pred = model.predict(X_test)

# Step 7: Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)
class_report = classification_report(y_test, y_pred)

print(f"Accuracy: {accuracy:.2f}")
print("Classification Report:\n", class_report)

# Step 8: Visualize the confusion matrix
plt.figure(figsize=(8, 6))
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues', xticklabels=['Not Spam', 'Spam'], yticklabels=['Not Spam', 'Spam'])
plt.ylabel('Actual')
plt.xlabel('Predicted')
plt.title('Confusion Matrix')
plt.show()
