import numpy as np
import pandas as pd
import streamlit as st
from sklearn.preprocessing import OneHotEncoder

df  = pd.read_csv(r'C:\Users\DevenShah\Desktop\test\SunHacks2022\stress_classification\Reddit_Title.csv')
df.head()

from sklearn.preprocessing import LabelEncoder
 
# Creating a instance of label Encoder.
le = LabelEncoder()
 
# Using .fit_transform function to fit label
# encoder and return encoded label
label = le.fit_transform(df['title'])
 
# printing label
print(label)

# removing the column 'Purchased' from df
# as it is of no use now.
df.drop("title", axis=1, inplace=True)
 
# Appending the array to our dataFrame
# with column name 'Purchased'
df["title"] = label
 
# printing Dataframe
print(df)

swap_list  = ["title","label"]
df = df.reindex(columns=swap_list)
df

X = df.iloc[:, :-1].values
y = df.iloc[:, -1].values

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

print(X_train)

print(X_test)

from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier(n_neighbors = 5, metric = 'minkowski', p = 2)
classifier.fit(X_train, y_train)

y_pred = classifier.predict(X_test)
print(np.concatenate((y_pred.reshape(len(y_pred),1), y_test.reshape(len(y_test),1)),1))

from sklearn.metrics import confusion_matrix, accuracy_score
cm = confusion_matrix(y_test, y_pred)
print(cm)
accuracy_score(y_test, y_pred)

st.write("Accuracy of the model is: ", accuracy_score(y_test, y_pred))

from sklearn.tree import DecisionTreeClassifier
classifier = DecisionTreeClassifier(criterion = 'entropy', random_state = 0)
classifier.fit(X_train, y_train)

y_pred = classifier.predict(X_test)
print(np.concatenate((y_pred.reshape(len(y_pred),1), y_test.reshape(len(y_test),1)),1))

from sklearn.metrics import confusion_matrix, accuracy_score
cm = confusion_matrix(y_test, y_pred)
print(cm)
accuracy_score(y_test, y_pred)

st.write("Accuracy of the model is: ", accuracy_score(y_test, y_pred))
st.write("Confusion Matrix of the model is: ", cm)