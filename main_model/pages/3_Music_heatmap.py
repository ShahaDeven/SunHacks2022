import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import cross_val_score, cross_val_predict
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
import numpy as np
import streamlit as st

features_for_mood = ['energy', 'liveness', 'tempo', 'speechiness',
                                     'acousticness', 'instrumentalness', 'danceability', 'duration_ms',
                                     'loudness', 'valence']

data = pd.read_csv(r'C:\Users\DevenShah\Desktop\test\SunHacks2022\music_classification\tracks7.csv')
hyper_opt = False

#split into trainval and test
trainx, testx, trainy, testy = train_test_split(data[features_for_mood], data['mood'], test_size = 0.33,
                                                random_state = 42, stratify=data['mood'])

scaler = StandardScaler()
train_scaled = scaler.fit_transform(trainx)

nn = MLPClassifier(max_iter = 15000, alpha=1.0, hidden_layer_sizes=8)
scores = cross_val_score(nn, train_scaled, trainy, cv=5)
print ("cv score: " + str(scores.mean()))

if hyper_opt:
    params = {"alpha": np.logspace(-4, 2, 7), 'hidden_layer_sizes': [1, 2, 5, 10, 20, 50, 100]}
    clf = GridSearchCV(nn, params)
    clf.fit(train_scaled, trainy)
    print("hyperparam optimized score : " + str(clf.best_score_))
    import pdb
    pdb.set_trace()

from sklearn.model_selection import cross_validate

results = cross_validate(nn, train_scaled, trainy, return_train_score=True)

results

nn = MLPClassifier(hidden_layer_sizes=8, max_iter=15000, alpha=1.0)

nn.fit(train_scaled, trainy)
test_preds = nn.predict(scaler.transform(testx))
accuracy_score(test_preds, testy)

st.write("Accuracy: ", accuracy_score(test_preds, testy))

import seaborn as sn
from sklearn.metrics import confusion_matrix

conf_matrix = confusion_matrix(testy, test_preds, labels = data['mood'].unique().tolist())

labels = data['mood'].unique().tolist()
import csv
print(test_preds)
with open('Predictions.csv', 'w', newline = '') as csvfile:
    my_writer = csv.writer(csvfile, delimiter = '\n')
    my_writer.writerow(test_preds)

plt.rcParams['figure.figsize'] = (7,5)
ax = plt.subplot()
sn.heatmap(conf_matrix, annot=True)
#labels = data['mood'].tolist()
ax.set_xlabel('Predicted labels')
ax.set_ylabel('True labels')
ax.set_title('Confusion Matrix')
ax.xaxis.set_ticklabels(labels)
ax.yaxis.set_ticklabels(labels)
plt.show()
st.markdown('## Confusion Matrix')
st.pyplot()

